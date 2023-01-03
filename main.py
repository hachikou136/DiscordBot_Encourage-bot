import discord
import os

Intents = discord.Intents.default()
client = discord.Client(intents=Intents)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  print('printf')
  await message.channel.send('Hello!')

  if message.content.startswith('hello'):
    await message.channel.send('Hello!')
    print('send hello')


client.run(os.environ['TOKEN'])
