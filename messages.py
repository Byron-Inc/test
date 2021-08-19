#external modules
import datetime
import discord
from discord.ext import commands

#interal modules
import data as d
import functions as f

class Messages(commands.Cog):
	def __init__ (self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("[COG] [Messages] Ready!")

	#private
	@commands.command(aliases=f.alias("private"))
	async def private(self, ctx, member:discord.User, *, msg):
		file_list = [await i.to_file() for i in ctx.message.attachments]
		await member.send(content = msg, files = file_list)
		await ctx.author.send(f"Sent a message to {member.name}.")
		await ctx.channel.purge(limit=1)
		await ctx.send("Message sent.")

	#message
	@commands.command(aliases=f.alias("message", "msg"))
	async def message(self, ctx, member:commands.MemberConverter, *, msg):
		now = datetime.now()
		file_list = [await i.to_file() for i in ctx.message.attachments]
		await member.send(content = f"```{msg}```\nSent by {ctx.author.name} in {ctx.guild}, {now.strftime('%Y/%m/%d, %H:%M:%S (UTC)')}", files = file_list)
		await ctx.send(f"A message is sent to {member.mention}.")

	#say
	@commands.command(aliases=f.alias("say"))
	async def say(self, ctx, *, text):
		file_list = [await i.to_file() for i in ctx.message.attachments]
		await ctx.send(content = text, files = file_list)

	#secret
	@commands.command(aliases=f.alias("secret"))
	async def secret(self, ctx, *, text):
		file_list = [await i.to_file() for i in ctx.message.attachments]
		await ctx.channel.purge(limit=1)
		await ctx.send(content = text, files = file_list)
		

def setup(bot):
	bot.add_cog(Messages(bot))