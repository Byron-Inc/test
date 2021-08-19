#external modules
import asyncio
import csv
import discord
import json
from discord.ext import commands

#interal modules
import data as d
import functions as f

types = ["About", "Fun", "Generate", "Message", "Mod", "Translate", "Utilities"]



def fetch_page(page):
	embed = discord.Embed(title="Help", description = types[page], color=0x82858c)
	embed.set_author(name = "Grayson", icon_url = d.pfp)
	for i in d.help_dict:
		if d.help_dict[i]['type'] == types[page]:
			embed.add_field(name = d.help_dict[i]["name"], value = d.help_dict[i]["description"], inline = False)
	embed.set_footer(text=f"You're in Page {page + 1}/{len(types)}")
	return embed
			
def find(item):
	embed = discord.Embed(title=d.help_dict[item]["name"], description = d.help_dict[item]["description"], color=0x7c7f86)
	embed.set_author(name = "Grayson", icon_url = d.pfp)
	embed.add_field(name = "Type", value = d.help_dict[item]["type"])
	embed.add_field(name = "Usage", value = f'yo {d.help_dict[item]["usage"]}')
	if d.help_dict[item]["alias"] != "":
		embed.add_field(name = "Alias", value = d.help_dict[item]["alias"])
	if d.help_dict[item]["note"] != "":
		embed.add_field(name = "Note", value = d.help_dict[item]["note"])
	return embed

class Help(commands.Cog):
	def __init__ (self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print("[COG] [Help] Ready!")
	#help
	@commands.command()
	async def help(self, ctx, arg : int = 1):
		pages = len(types)
		if int(arg) > pages:
			cur_page = 1
		else:
			cur_page = int(arg)
		message = await ctx.send(embed=fetch_page(cur_page - 1))

		await message.add_reaction("◀️")
		await message.add_reaction("▶️")

		def check(reaction, user):
			return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

		while True:
			try:
				reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)

				if str(reaction.emoji) == "▶️" and cur_page != pages:
					cur_page += 1
				elif str(reaction.emoji) == "◀️" and cur_page > 1:
					cur_page -= 1
				await message.edit(embed=fetch_page(cur_page - 1))
				await message.remove_reaction(reaction, user)
				
			except asyncio.TimeoutError:
				await message.edit(content = ":x: Command time out!")
				break

	@commands.command(aliases=f.alias("search", "find"))
	async def search(self, ctx, cmd):
		await ctx.send(embed=find(cmd))

def setup(bot):
	bot.add_cog(Help(bot))