#external modules
import discord
import random as rand
from discord.ext import commands

#interal modules
import data as d
import functions as f

class Generate(commands.Cog):
	def __init__ (self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("[COG] [Generate] Ready!")
		
	@commands.command(aliases = f.alias("xkcd", "comic"))
	async def xkcd (self, ctx, number = "latest"):
		if number == "random":
			total = f.request("xkcd", "latest")["num"]
			jsondata = f.request("xkcd", rand.randint(1, total))
		elif number == "latest":
			jsondata = f.request("xkcd", "latest")
		else:
			jsondata = f.request("xkcd", number)
		embed = discord.Embed(title=jsondata["safe_title"], description=f'Comic {jsondata["num"]}', color=0x8af542)
		embed.add_field(name=jsondata["alt"], value=" ​​​​​​", inline=False)
		embed.set_footer(text=f'Published on {jsondata["day"]}/{jsondata["month"]}/{jsondata["year"]}')
		embed.set_image(url=jsondata["img"])
		await ctx.send(embed=embed)

	@commands.command(aliases=f.alias("gif"))
	async def gif(self, ctx, *, txt):
		gif_post = f.request("giphy", txt)
		embed = discord.Embed(title=txt.title(), color = ctx.author.color)
		embed.set_image(url = f'https://media.giphy.com/media/{gif_post["data"][rand.randint(0, 9)]["id"]}/giphy.gif')
		await ctx.send(embed=embed)

	@commands.command(aliases=f.alias("fact", "facts"))
	async def fact(self, ctx):
		await ctx.send(f.request("fact", "lol")["text"])

	@commands.command(aliases=f.alias("joke", "jokes"))
	async def joke(self, ctx):
		data = f.request("joke", "punch")
		await ctx.send(f"{data['setup']}\n{data['punchline']}")

	@commands.command(aliases = f.alias("motivate", "inspire", "motiv"))
	async def motivate(self, ctx):
		await ctx.send(f.request("zenquotes", "random"))

def setup(bot):
	bot.add_cog(Generate(bot))