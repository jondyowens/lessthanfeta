# bot.py
import os

import discord
from dotenv import load_dotenv
import random
import time

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

    if "!gift" in message.content:
        await message.channel.send("<https://www.amazon.com/hz/wishlist/ls/1OOMA2I6EJA26?ref_=wl_share>")

    if "!onlyfans" in message.content:
        await message.channel.send("onlyfans.com/ľ̸͓͕̒̊̽̏̒̚ ̸̘̟̤̒s̶̡̰̖̦͈̰̀̎̒̀̈́͆̔͛ș̷̺̟̟͊̐̌̓̄̋ṫ̸͇̠̻̹̝̪́̏͗͘h̶̩̗͓̬̻̓̿̂ ̷̟͔͖̊͘ ̵̖̝̤̌̏̆͌b̵̦͕̃̈́̽͝͠r̵̝̮̻̯̍͋̋͛̊͝ ̴͔̝̲̠͇̹̦̯́͆̈́̈̔͐ę̴̗͓̬̤̻̗̔̽̈́̋̀͛̐͜͠.. Error: Segmentation fault.")

    if "!socials" in message.content:
        await message.channel.send(content="Instagram: <https://www.instagram.com/lessthanbrie> \nTwitter: <https://www.twitter.com/lessthanbrie> \nTwitch: <https://twitch.tv/lessthanbrie>")
        
    if "!purge" in message.content:
        msg = await message.channel.send("Purging all channels in 3 seconds...")
        time.sleep(1)
        await msg.edit(content="Purging all channels in 2 seconds...")
        time.sleep(1)
        await msg.edit(content="Purging all channels in 1 second...")
        time.sleep(1)
        await msg.edit(content="P̸̡͇̺̝͖͓̬̞̻̮̱̖̎̅ͅu̸͓̫̳͙̯̖͔̗̱͚̬̜͋͜ŗ̸͎͇͔͉͔͈̝̠̲̻̻͌͑̿̋̓͝g̵̛̼̰̼̩͉̱̜̣̮̻̝̃̊̆̔ḯ̴̫͔̘͉͗͂̃ņ̸̭̣͋͒̀̾́͛g̸̡̠̪̟̖͚̙̝͖͕̩̤̫̮̒͋̇̃̎ ̷̠̳̖̼̩̩̺̓̓̃̅͋̀́̉͑́͐̄͝å̶̢͚͎̭̗̱̻̥̝̩̼̫͈̆̂̿̿̒͆́̀͋̓̽̓̚̕ͅl̵͓͌l̷͍͉̦͉̣͓̬̮̞̙̤̍̋̂̓̅̂͒̃ ̶̺̗̰̪̖̩͚̗͕͎̲̋̄̇̈́̒͊̄c̷̜̯̯̪̰̬̣̝̹̫̮̰͎̃͜͝h̶̨̧̙̣͍̘̫͕͕̫̭̟͐́̃̋́́̋̏̐̾̕͠͝ͅȃ̷̜͖̱͇̙̮̠͚̓͆͠ņ̸̱̐͛̈́͌̃̐́̏̾̚͝n̷̛̯̯͂̀̃͑͋̌̉͒̌̽̓̈́̓͝e̷̡̢̛͎̺̻͖̫̙̪͈̙̹͑́̐̆̈́͜l̷̛̻͕͈̞̤͎̺̥̮͂̊̇͗͊̀͒̍͊̉͘͝͝͠s̶̢̡̢̞̮̮̻̩̼̫̳̖͇͒̈́͂͂̒̎͒͗͑")
        
client.run(TOKEN)