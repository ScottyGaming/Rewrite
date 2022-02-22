import disnake as discord
from disnake.ext import commands
import asyncio
from asyncio import sleep
snipe_message_author = {}
snipe_message_content = {} 

class snipe(commands.Cog):
  def __init__(self, client):
    self.client = client

    print("Loading snipe module")
    
#snipe saving
  @commands.Cog.listener()
  async def on_message_delete(self, message):

      global snipe_message_author
      global snipe_message_content
      snipe_message_author[message.channel.id] = message.author
      snipe_message_content[message.channel.id] = message.content
      await asyncio.sleep(60)
      del snipe_message_author[message.channel.id]
      del snipe_message_content[message.channel.id]

#snipe bot
  @commands.command()
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def snipe(self, ctx):
        channel = ctx.channel 
        try:
            snipeEmbed = discord.Embed(title=f"Last deleted message in #{channel.name}",description = snipe_message_content[channel.id])
            snipeEmbed.set_footer(text=f"Deleted by {snipe_message_author[channel.id]}")
            await ctx.send(embed = snipeEmbed)
        except:
            await ctx.send(f"There are no deleted messages in #{channel.name}")
  
def setup(client):
  client.add_cog(snipe(client))

