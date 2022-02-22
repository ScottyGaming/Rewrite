import disnake
from disnake.ext import commands
import asyncio
from asyncio import sleep

from cogs.config.variables import watermark,ownername

class links(commands.Cog):
  def __init__(self, client):
    self.client = client

    print("Loading links module")

  #invite
  @commands.command()
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def invite(self,ctx):
      embed = disnake.Embed(title="Bot Invite", description="Use this link to invite the bot to your server", color=ctx.author.color)
      embed.add_field(name= f"INVITE LINK", value="https://discord.com/oauth2/authorize?client_id=910852830884147200&permissions=8&scope=bot\n")
      embed.set_footer(text=f"{watermark} by {ownername}")
      await ctx.send(embed = embed)

  #support
  @commands.command()
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def support(self,ctx):
    embed = disnake.Embed(title="Bot Support", description="Use this invite to go to the support server!", color=ctx.author.color)
    embed.add_field(name= f"INVITE LINK", value="https://discord.gg/gCJ8T5BHbn\n")
    embed.set_footer(text=f"{watermark} by {ownername}")
    await ctx.send(embed = embed)
    

  
def setup(client):
  client.add_cog(links(client))
