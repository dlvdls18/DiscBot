import discord
import random
import time

def now():
  return round(time.time() * 1000)

class DiscbotClient(discord.Client):
  async def on_connect(self):
    print('Connected to server')
  async def on_disconnect(self):
    print('Disconnected to server')
  async def on_message(self, msg):
    self.author = msg.author
    if msg.author == self.user: return
    async def sendMsg(text):
      m = await msg.channel.send(text)
      return m.id
    async def editMsg(id, text):
      m = await msg.channel.fetch_message(id)
      await m.edit(content=text)
    async def isEdited(id):
      m = await msg.channel.fetch_message(id)
      return m.edited_at != None
    $1

bot = DiscbotClient()
bot.run('$2')