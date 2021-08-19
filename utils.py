#external modules
import datetime
import discord
import random
import sympy
from discord.ext import commands

#interal modules
import data as d
import functions as f

class Utilities(commands.Cog):
	def __init__ (self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("[COG] [Utils] Ready!")

	#hello
	@commands.command(aliases = f.alias("hello", "hi", "greet"))
	async def hello(self, ctx, *, target = "human"):
		await ctx.send(random.choice(d.say_hi).format(target=target))
	
	#roll
	@commands.command(aliases=f.alias("roll", "die"))
	async def roll(self, ctx, *args):
		results = []
		total = 0
		if len(args) == 2:
			for i in range(0, int(args[0])):
				rand = random.randint(1, int(args[1]))
				results.append(str(rand))
				total += rand
		else:
			for i in range(0, len(args)):
				rand = random.randint(1, int(args[i]))
				results.append(str(rand))
				total += rand
		await ctx.send(f"The total of your dice rolls is... `{total}`!\n```{', '.join(results)}```")

	#ping
	@commands.command(aliases=f.alias("ping", "latency"))
	async def ping(self, ctx):
		await ctx.send(f":ping_pong: Pong! The latency is {self.bot.latency * 1000:.2f} ms.")

	#choice
	@commands.command(aliases=f.alias("choice"))
	async def choice(self, ctx, question, *choices):
		await ctx.send(random.choice(choices))

	#8ball
	@commands.command(aliases=["8ball", "8Ball", "8BALL"])
	async def _8ball(self, ctx, *, question):
		await ctx.send(random.choice(d.eightball_list))


	#calc
	@commands.command(aliases=f.alias("calc"))
	async def calc(self, ctx, *, expression: str):
		expression = "".join(expression.strip("`").split("\\"))
		await ctx.send(f"I counted it up. ```{expression} = {sympy.simplify(sympy.sympify(expression))}```")


	#poll
	@commands.command(aliases=f.alias("poll"))
	async def poll(self, ctx, question, *poll):
		sel = "\n".join([f":regional_indicator_{d.alphabet[i]}: {poll[i]}" for i in range(len(poll))])
		Embed = discord.Embed(title="Poll")
		Embed.set_author(name=ctx.author, icon_url = ctx.author.avatar_url)
		Embed.add_field(name=question, value=sel)
		message = await ctx.send(embed=Embed)
		for j in range(0, len(poll)):
			await message.add_reaction(d.alphabet_fancy[j])
            
	#userinfo
	@commands.command(alias=f.alias("userinfo", "ui"))
	async def userinfo(self, ctx, member : discord.User):
		embed=discord.Embed(title=member.name, color=member.color)
		embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
		embed.set_thumbnail(url=member.avatar_url)
		embed.add_field(name="Nickname", value=member.display_name,inline=True)
		embed.add_field(name="Is Bot?", value=member.bot, inline=True)
		embed.add_field(name="ID", value=member.id,inline=False)
		embed.add_field(name="Date Created", value=member.created_at.strftime("%B %d, %Y | %H:%M:%S (UTC)"), inline=False)
		try:
			embed.add_field(name="Joined Server At", value=member.joined_at.strftime("%B %d, %Y | %H:%M:%S (UTC)"), inline=False)
		except:
			pass
		await ctx.send(embed=embed)
		

def setup(bot):
	bot.add_cog(Utilities(bot))