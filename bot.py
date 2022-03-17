import discord

client = discord.Client()

targetList = []

cursed_word = ":emoji_24::emoji_24::emoji_24::emoji_24::emoji_24::emoji_24:"

@client.event
async def on_message(message):
    if message.author in targetList:
        await message.channel.send(cursed_word)
    else if message.content[:4] == "_add":
        targetList.append(message.content[5:]
        await message.channel.send("curse them!!")
    else if message.content[:4] == "_curse":
        cursed_word = message .content[5:]
        await message.channel.send(cursed_word)
