#external modules
import asyncio
import discord
import math
from discord.ext import commands

#internal modules
import data as d
import functions as f

class About(commands.Cog):
	def __init__ (self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("[COG] [About] Ready!")
		
	#invite
	@commands.command(aliases=f.alias("invite", "inv"))
	async def invite(self, ctx):
		await ctx.send(d.inv_link)

	@commands.command(aliases=f.alias("credits, credit"))
	async def credits(self, ctx, arg=None):
		#finds page number
		pages = math.ceil(len(d.credits_dict) / 5)
		if arg == None or int(arg) > pages:
			cur_page = 1
		else:
			cur_page = int(arg)
		#retrieves the page of credits
		def get_credit(page):
			listed_credits = list(d.credits_dict)
			embed = discord.Embed(title="Credits", description="Credit to these people/organisations/websites for help in the production of me.", color=0x888B91)
			embed.set_author(name="Grayson", icon_url=d.pfp)
			if cur_page * 5 - 1 > len(listed_credits):
				x = len(listed_credits)
			else:
				x = cur_page * 5 - 1
			for i in range(cur_page * 5 - 5, x):
				key = listed_credits[i]
				embed.add_field(name=key, value=d.credits_dict[key], inline=False)
			return embed
			
		#react to scroll mechanism
		#check for reacts
		message = await ctx.send(embed=get_credit(cur_page))
		await message.add_reaction("◀️")
		await message.add_reaction("▶️")
		def check(reaction, user):
			return str(reaction.emoji) in ["◀️", "▶️"] and user != self.bot.user
		#move pages
		while True:
			try:
				reaction, user = await self.bot.wait_for("reaction_add", timeout=120, check=check)
				#next page
				if str(reaction.emoji) == "▶️" and cur_page != pages:
					cur_page += 1
					await message.edit(embed=get_credit(cur_page))
				#last page
				elif str(reaction.emoji) == "◀️" and cur_page > 1:
					cur_page -= 1
					await message.edit(embed=get_credit(cur_page))
				await message.remove_reaction(reaction, user)
				#timeout
			except asyncio.TimeoutError:
				await message.edit(content = ":x: Command time out!")
				break

	#feedback
	@commands.command(aliases=f.alias("feedback"))
	async def feedback(self, ctx, *, feedback):
		feedback_channel = self.bot.get_channel(841618437063049266)
		await feedback_channel.send(feedback)
		await ctx.send("Feedback sent.")

def setup(bot):
	bot.add_cog(About(bot))