import html
import json
import os
import requests

def alias(*arg):
	aliases = []
	i = 0
	for al in arg:
		aliases.append(al.upper())
		aliases.append(al.capitalize())
		if i > 0:
			aliases.append(al)
		i += 1
	return aliases

def get_time(time_input):
	time_input = int(time_input)
	time_in_sec = time_input % 60
	time_rem = time_input - time_in_sec
	time_in_min = (time_rem / 60) % 60 
	time_rem = time_rem - time_in_min * 60
	time_in_hrs = time_rem / 60 / 60
	return(f"{round(time_in_hrs)} hours, {round(time_in_min)} minutes, {round(time_in_sec)} seconds")

def request(src, targ):
	if src == "zenquotes":
		response = requests.get(f"https://zenquotes.io/api/{targ}")
		json_data = json.loads(response.text)
		return f"> {json_data[0]['q']}\n - {json_data[0]['a']}"
	elif src == "xkcd":
		if targ == "random":
			return requests.get("https://xkcd.com/random/comic/").json()
		elif targ == "latest":
			return requests.get("https://xkcd.com/info.0.json").json()
		else:
			return (requests.get(f"https://xkcd.com/{targ}/info.0.json")).json()
	elif src == "giphy":
		return json.loads(requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={os.getenv('GIPHY_API')}&q={html.escape(targ)}&limit=10&offset=0&rating=g&lang=en").text)
	elif src == "fact":
		return json.loads(requests.get("https://uselessfacts.jsph.pl/random.json?language=en").text)
	elif src == "joke":
		return json.loads(requests.get("https://official-joke-api.appspot.com/jokes/random").text)

def check_int(str):
	try:
		x = int(str)
		return True
	except:
		return False