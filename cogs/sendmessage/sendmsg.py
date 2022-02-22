import disnake as discord
from disnake.ext import commands
import asyncio
from asyncio import sleep
import cogs.config
from cogs.config import watermark,modList
class sendmsg(commands.Cog):
  def __init__(self, client):
    self.client = client

    print("Loading memcount module")


#send message
  @commands.command()
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def sendmsg(self,ctx,channel,*,content):
    if ctx.message.author.guild_permissions.manage_messages or ctx.author.id in modList:  
      channel = self.client.get_channel(int(channel))
      await channel.send(content)
    else:
      await ctx.send("``PERMISSION DENIED!``")

  
def setup(client):
  client.add_cog(sendmsg(client))
