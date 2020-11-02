# bot.py
import os

import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

def remove_sub_emojis(all_emojis):
    stripped_emojis = [i for i in all_emojis if i.managed == False]
    return stripped_emojis

async def emoji_dump(message):
    emoji_dump = str()
    stripped_emojis = remove_sub_emojis(client.emojis)
    for emoji in stripped_emojis:
            emoji_dump += str(emoji) + " "

    await message.channel.send(emoji_dump)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    list_of_cheese = ["<:CHEESE:746596359280263209>", ":cheese:", "<:cheese:767272983214686228>"]
    if "cheese" in message.content.lower():
        await message.add_reaction(random.choice(list_of_cheese))

    if "!emojis" in message.content:
        await emoji_dump(message)

client.run(TOKEN)