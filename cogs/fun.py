#external modules
import discord
import random
from discord.ext import commands

#interal modules
import data as d
import functions as f

class Fun(commands.Cog):
	def __init__ (self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print(f"[COG] [Fun] Ready!")

	@commands.command(aliases=f.alias("ship"))
	async def ship(self, ctx, personA, personB):
		await ctx.send(f"I ship it!{personA[:int(round((len(personA) / 2)))] + personB[int(round((len(personB) / 2))):]}")

	@commands.command(aliases=f.alias("spam"))
	async def spam(self, ctx, len):
		await ctx.send("".join([random.choice(d.typable) for i in range(int(len))]))
		
	@commands.command(aliases=f.alias("slap"))
	async def slap(self, ctx, *, slapped):
		await ctx.send(":hand_splayed: " + random.choice(d.slap_list).format(slapper=ctx.author.display_name, slapped=slapped))

	@commands.command(aliases=f.alias("grayson"))
	async def grayson(self, ctx):
		await ctx.send("Did you call me?")

def setup(bot):
	bot.add_cog(Fun(bot))