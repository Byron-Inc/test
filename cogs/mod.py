#external modules
import discord
from discord.ext import commands
from replit import db

#interal modules
import data as d
import functions as f

class Mod(commands.Cog):
	def __init__ (self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("[COG] [Mod] Ready!")
	
	#kick
	@commands.command(aliases = f.alias("kick"))
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, user : commands.MemberConverter, *, reason = None):
		await user.kick(reason = f"{ctx.author.name}: reason")
		await ctx.send(f"{user.name} had been kicked from this server.")

	#ban
	@commands.command(aliases = f.alias("ban"))
	@commands.has_permissions(kick_members=True)
	async def ban(self, ctx, user : commands.MemberConverter, *, reason = None):
		await user.ban(reason = f"{ctx.author.name}: reason")
		await ctx.send(f"{user.name} had been banned from this server.")

	#warn
	@commands.command(aliases = f.alias("warn"))
	@commands.has_permissions(kick_members=True)
	async def warn(self, ctx, user : commands.MemberConverter, *, reason = None):
		await user.send(f"You had just received a warn in {ctx.guild}. \n> Moderator: {ctx.author.name}\n> Reason: {reason}")
		await ctx.send(f"{user.name} had been warned.")

	#purge
	@commands.command(aliases = f.alias("purge", "delete", ))
	@commands.has_permissions(manage_messages = True)
	async def purge(self, ctx, amount : int):
		await ctx.channel.purge(limit=amount)
		await ctx.send(f"{amount} messages deleted.")


def setup(bot):
	bot.add_cog(Mod(bot))