import disnake as discord
from disnake.ext import commands
import asyncio
from asyncio import sleep
import cogs.config
from cogs.config import watermark,modList
class serverinfo(commands.Cog):
  def __init__(self, client):
    self.client = client

    print("Loading serverinfo module")

  #serverinfo
  @commands.command(name='serverinfo')
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def serverinfo(self,ctx):
    client=self.client
    if ctx.message.author.guild_permissions.manage_messages or ctx.author.id in modList:
      guild = ctx.guild
      description = guild.description
      owner = guild.owner
      id = guild.id
      url = guild.icon
      memberCount = guild.member_count
      description = guild.description
      total_text_channels = len(guild.text_channels)
      total_voice_channels = len(guild.voice_channels)
      total_channels = total_text_channels + total_voice_channels
      roles = len(guild.roles) - 1
      shard_id = ctx.guild.shard_id
      shard = client.get_shard(shard_id)
      shard_ping = shard.latency
      shard_servers = len([guild for guild in client.guilds if guild.shard_id == shard_id])
      embed = discord.Embed(title=" Server Information",color=discord.Color.blue())
      embed.set_thumbnail(url=url)
      embed.add_field(name="Owner", value=owner)
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name="Server Name", value=guild)
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name="Member Count", value=memberCount)
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name="Server ID", value=id)
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name="Total Number Of Channels", value=total_channels)
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name="Server Description", value=description)
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name="No of roles", value=roles)
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name="Latency", value=f'{int(client.latency*10)} ms')
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name = chr(173), value = chr(173))
      embed.set_footer(text=f"{watermark} by Scottminer22Gaming")
      await ctx.send(embed=embed)
      embed = discord.Embed(title=" Shard Information",color=discord.Color.blue())
      embed.set_thumbnail(url=url)
      embed.add_field(name="Shard ID", value=shard_id)
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name="Shard Latency", value=f'{int(shard_ping*10)} ms')
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name = chr(173), value = chr(173))
      embed.add_field(name="Same Shard Servers", value=f'{shard_servers-1} more servers run in the same shard')
      embed.set_footer(text=f"{watermark} by Scottminer22Gaming")
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(serverinfo(client))
