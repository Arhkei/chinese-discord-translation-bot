import discord
from googletrans import Translator
# create discord client
client = discord.Client()
translator = Translator()

# token from https://discordapp.com/developers
token = ''
translation_channel = 718543716482023505
general_channel = 718347361151090710
# bot is ready
@client.event
async def on_ready():
	try:
		print(client.user.name)
		print(client.user.id)
		print('Discord.py Version: {}'.format(discord.__version__))

	except Exception as e:

		print(e)

@client.event

async def on_message(message):
	# if the message is from the bot itself ignore it
	if message.author == client.user:
		pass
	else:
		detection = translator.detect(message.content).lang
		if detection == 'en':
			if str(message.channel) != "translation":
				translation = translator.translate(message.content, dest='zh-CN').text
				channel = client.get_channel(translation_channel)
			else:
				translation = message.content
				channel = client.get_channel(general_channel)
		elif detection == 'zh-CN':
			if str(message.channel) != "general":
				translation = translator.translate(message.content, dest='en').text
				channel = client.get_channel(general_channel)
			else:
				translation = message.content
				channel = client.get_channel(translation_channel)
		name = str(message.author)[:-5]
		await channel.send(f"{name}: {translation}")
client.run(token)
