import asyncio
import discord
import os

from discord.ext import commands
from keep_alive import keep_alive
from replit import db

import data as d
import functions as f
bot = commands.Bot(command_prefix=["yo ", "Yo ", "YO "])

@bot.event
async def on_ready():
	print("[MAIN] Ready!")

@bot.event
async def on_command_error(ctx, error):
	await ctx.send(f"An error occured! If this is not a user-side issue, please use the feedback command to report this issue to us!\n```{error}```")
	raise error

	
if "status_no" not in db.keys():
	db["status_no"] = 1

@commands.Cog.listener()
async def presence():
	await bot.wait_until_ready()
	statuses = [["l", "yo help"], ["w", f"on {len(bot.guilds)} servers"], ["p", f"{len(d.help_dict)} commands"]]
	while not bot.is_closed():
		status = statuses[db["status_no"] - 1]
		if status[0] == "p":
	  		await bot.change_presence(activity=discord.Game(name=status[1]))
		elif status[0] == "l":
	  		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status[1]))
		elif status[0] == "w":
	  		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status[1]))
		await asyncio.sleep(15)
		db["status_no"] += 1
		db["status_no"] %= len(statuses)
	

bot.loop.create_task(presence())

bot.remove_command("help")

bot.load_extension("cogs.about")
bot.load_extension("cogs.help")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.generate")
bot.load_extension("cogs.mod")
bot.load_extension("cogs.messages")
bot.load_extension("cogs.translate")
bot.load_extension("cogs.utils")

keep_alive()
bot.run(os.getenv("TOKEN"))