#external modules
import discord
from discord.ext import commands

#interal modules
import data as d
import functions as f

class About(commands.Cog):
	def __init__ (self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("[COG] [About] Ready!")
		

def setup(bot):
	bot.add_cog(About(bot))