import json

credits_dict = {
    "Byron#2098":
    "The one and only developer, for coding me. Just call him Byron.",
    "Discord": "For making the wonderful website.",
    "w3schools":
    "The website Byron uses to learn Python. (Fun fact: Byron hadn't learnt Python when he started me!)",
    "freecodecamp.org":
    "For teaching Byron to set me up, as well as introducing me to repl.it and uptimerobot.com.",
    "repl.it": "The website Byron used to code me in Python.",
    "uptimerobot.com": "The server Byron used to host me.",
    "zenquotes.io": "The source of the quotes in bb!motivate",
    "giphy": "For the bb!gif function.",
    "imgflip": "The API is used to make the facts memes.",
    "Randall Munroe": "For making XKCD comics.",
    "Lucas":
    "https://www.youtube.com/channel/UCR-zOCvDCayyYy1flR5qaAg \n Taught Byron to code with discord.py.",
    "TonyBrown148": "Thanks for the help with the translating code.",
    "red herring":
    "Thanks for helping Byron in the making of multipage commands.",
    "You": "For using my bot.",
    "Suggestors": "For suggesting new functions to my bot."
}

eightball_list = [
    "It is certain.", 
	"It is decidedly so.", 
	"Without a doubt.",
    "Yes – definitely.", 
	"You may rely on it.", 
	"As I see it, yes.",
    "Most likely.", 
	"Outlook good.", 
	"Yes.", 
	"Signs point to yes.",
    "Reply hazy, try again.", 
	"Ask again later.", 
	"Better not tell you now.",
    "Cannot predict now.", 
	"Concentrate and ask again.", 
	"Don't count on it.",
    "My reply is no.", 
	"My sources say no.", 
	"Outlook not so good.",
    "Very doubtful."
]

pfp = "https://cdn.discordapp.com/avatars/777349645629653003/0b4024d3a49e7170c79d3c19dabfb124.png"

inv_link = "https://discord.com/api/oauth2/authorize?client_id=777349645629653003&permissions=2448911478&scope=bot"

alphabet = "abcdefghijklmnopqrstuvwxyz"

alphabet_fancy = "🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿"

typable = "`1234567890-=~!@#$%^&*()_+qwertyuiop[]\\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:\"zxcvbnm,./ZXCVBNM<>? \n"

say_hi = ["Hi!", "Hello!", "Hello, {target}.", "Hi, {target}!", "What's up, {target}?", "Yo, how's it going?", ]

slap_list = [
    "{slapper} tried to slap {slapped} but missed. {slapped} slapped {slapper} at their greatest might as revenge!",
    "{slapper} and {slapped} did a small and quick Hi-5. It hurts.",
    "{slapper} patted {slapped}. Does {slapper} think {slapped} is a pet?",
    "{slapper} slapped {slapped} lightly. {slapped} don't feel any pain.",
    "{slapper} slapped {slapped} hard. Ouch! I can hear the sound.",
    "{slapper} used a cane to slap {slapped}. {slapped} was sent to emergency room. {slapped}'s family sued {slapper}.",
    "{slapper} and {slapped} slapped each others. The police saw it and put them in jail for a month.",
    "{slapper} tried to slap {slapped} but {slapped}'s dog leapt up and killed {slapper}.",
    "{slapper} took a knife and diced {slapped} into 42 pieces.",
    "{slapper} had a thought of slapping {slapped}, but ended up not doing so and bought ice-cream for {slapped} instead. Happy ending.",
    "{slapper} slapped {slapped} on the cheeks. It is still red and painful when I last saw them.",
    "{slapper} attempted to slap {slapped}, but {slapped} is an undercover taekwondo master! {slapped} kicked {slapper} in his- \n Well, I shouldn't say that word out."
]

with open("help.json", "r") as f:
    help_dict = json.load(f)