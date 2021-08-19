import discord
import google_trans_new
import random
from discord.ext import commands
from google_trans_new import google_translator
from google_trans_new.constant import LANGUAGES

#interal modules
import data as d
import functions as f

trans = google_translator()

class Translate(commands.Cog):
	def __init__ (self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("[COG] [Translate] Ready!")

	#translator
	@commands.command(aliases = f.alias("translate", "trans"))
	async def translate(self, ctx, lang_src="en", lang_dest="zh-cn", to_trans="Hello world."):
		translate_text = trans.translate(to_trans, lang_src=lang_src, lang_tgt=lang_dest)
		await ctx.send(translate_text)

	#languagelist
	@commands.command(aliases = f.alias("languagelist", "langlist"))
	async def languagelist(self, ctx):
		lang_list = ", ".join(["{} - {}".format(_, google_trans_new.LANGUAGES[_]) for _ in google_trans_new.LANGUAGES])
		await ctx.send(lang_list)

	#badtranslator
	@commands.command(aliases = f.alias("badtranslator", "bt"))
	async def badtranslator(self, ctx, times=20, *, text="Hello world"):
		bt_res = text
		message = await ctx.send("Generating, please wait...")
		for x in range(1, int(times)):
			bt_res = trans.translate(bt_res, lang_tgt=random.choice(list(google_trans_new.LANGUAGES)))
		print(trans.translate(bt_res, lang_tgt="en"))
		await message.edit(content = trans.translate(bt_res, lang_tgt="en"))

def setup(bot):
	bot.add_cog(Translate(bot))