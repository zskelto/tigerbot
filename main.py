import discord
import asyncio
import configparser
from Imgur import Imgur
from triggered import *

config = configparser.ConfigParser()
config.read('config.cfg')
username = config.get('bot','username')
userid = config.get('bot','userid')
token = config.get('bot','token')

client = discord.Client()

imgur = Imgur()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        args = message.content.split(' ')

        if args[0] == '!ping':
            await client.send_message(message.channel, 'Pong!')

        elif args[0] == '!i':
            pic = imgur.get()
            await client.send_message(message.channel, pic)

        elif args[0] == '!clear':
            if len(args) == 1:
                await client.purge_from(message.channel, limit=3)
            else:
                try:
                    await client.purge_from(message.channel, limit=int(args[1]))
                except ValueError:
                    await client.send_message(message.channel, 'Second argument must be an integer... :zzz:')

        elif args[0] == '!help':
            await client.send_message(message.channel, """```Current commands:\n
                                                            !ping - Test to see if the bot is working\n
                                                            !i - Shows a random imgur link, warning: NSFW\n
                                                            !clear *count - clears the last <count> messages, default: 3```""")

        elif args[0] == '!triggered':
            with open(triggered(14), 'rb') as f:
                await client.send_file(message.channel, f)

client.run(token)
