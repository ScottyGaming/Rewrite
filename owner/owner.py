import disnake as discord
from disnake.ext import commands
import asyncio
from asyncio import sleep
import cogs.config
from cogs.config import watermark,modList

class owner(commands.Cog):
  def __init__(self, client):
    self.client = client

    print("Loading owner module")

  #serverlist
  @commands.command()
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def serverlist(self,ctx):
    client=self.client
    if ctx.author.id == modList:
      embed = discord.Embed(title="Owner Only Module", description="Server list", color=ctx.author.color)
      for guild in client.guilds:
        embed.add_field(name= f"Guild Name : Guild ID : Shard ID", value=f"``**{guild.name}**: {guild.id}, {guild.shard_id}``")
      await ctx.send(embed=embed)    
    else:
      await ctx.send("``You dont have the permission to access this bot-owner only module!``")

  #leave guild
  @commands.command()
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def leave(self,ctx, guild_id):
    if ctx.author.id == modList:
      await self.client.get_guild(int(guild_id)).leave()
      await ctx.send(f'``Leaving The Selected Server``')
    else:
      await ctx.send("``You dont have the permission to access this bot-owner only module!``")

  

  #enable/disable command
  @commands.command()
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def toggle(self,ctx, *,command):
    if ctx.author.id == modList:
      command = self.client.get_command(command)

      if command is None:
        await ctx.send('``Invalid Command Name!``')
      
      elif ctx.command == command:
        await ctx.send('``This breaks the bot functions so you cant disable this command!``')
      
      else:
        command.enabled = not command.enabled
        thingwhereitsaysenabdisab = 'enabled' if command.enabled else 'disabled'
        await ctx.send(f'``I have {thingwhereitsaysenabdisab} the command named {command.qualified_name}``')
    else:
      await ctx.send("``You dont have the permission to access this bot-owner only module!``")

def setup(client):
  client.add_cog(owner(client))