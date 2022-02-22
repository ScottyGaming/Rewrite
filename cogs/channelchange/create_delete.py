import disnake
from disnake.ext import commands
import asyncio
from asyncio import sleep
from cogs.config.variables import watermark,owner,ownername

class create_delete(commands.Cog):
  def __init__(self, client):
    self.client = client

    print("Loading c/d channel module")


#Delete channel
  @commands.command(name='delete-channel')
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def delete_channel(self, ctx, channel_name):
    if ctx.message.author.guild_permissions.manage_channels or ctx.author.id in owner:  
      guild = ctx.guild
      existing_channel = disnake.utils.get(guild.channels, name=channel_name)
      # if the channel exists
      if existing_channel is not None:
        await existing_channel.delete()
        embed = disnake.Embed(title="Channel Deletor", description="Deletes channel!", color=ctx.author.color)
        embed.add_field(name= f"Progress", value= f"``Channel Deleted!``")
        embed.set_footer(text=f"{watermark} by {ownername}")
        await ctx.send(embed = embed)
      # if the channel does not exist, inform the user
      else:
        embed = disnake.Embed(title="Channel Deletor", description="Deletes channel!", color=ctx.author.color)
        embed.add_field(name= f"Progress", value= f"``No channel named {channel_name} was found``")
        embed.set_footer(text=f"{watermark} by {ownername}")
        await ctx.send(embed = embed)
    else:
      await ctx.send("``PERMISSION DENIED!``")

  #create channel
  @commands.command(name='create-channel')
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def create_channel(self,ctx, channel_name):
    if ctx.message.author.guild_permissions.manage_channels or ctx.author.id in owner:
      guild = ctx.guild
      existing_channel = disnake.utils.get(guild.channels, name=channel_name)
      #if the channel not exists
      if existing_channel is None:
        await guild.create_text_channel(channel_name)
        embed = disnake.Embed(title="Channel Creator", description="Creates channel!", color=ctx.author.color)
        embed.add_field(name= f"Progress", value= f"``Channel {channel_name} Created!``")
        embed.set_footer(text=f"{watermark} by {ownername}")
        await ctx.send(embed = embed)
      #if exists
      else:
        embed = disnake.Embed(title="Channel Creator", description="Creates channel!", color=ctx.author.color)
        embed.add_field(name= f"Progress", value= f"``Channel {channel_name} already exists!``")
        embed.set_footer(text=f"{watermark} by {ownername}")
        await ctx.send(embed = embed)
    else:
      await ctx.send("``PERMISSION DENIED!``")


def setup(client):
  client.add_cog(create_delete(client))
