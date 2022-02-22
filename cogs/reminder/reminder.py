import disnake as discord
from disnake.ext import commands
import asyncio
from asyncio import sleep
import cogs.config
from cogs.config import watermark

class reminder(commands.Cog):
  def __init__(self, client):
    self.client = client

    print("Loading reminder module")

  @commands.command()
  async def remindme(self,ctx,time,*,task):
    def convert(time):
      pos = ['s','m','h','d']
      time_dict = {'s':1,'m':60,'h':3600,'d':3600*24}
      unit = time[-1]
      if unit not in pos:
        return -1
      try:
        val = int(time[:-1])
      except:
        return -2
      return val * time_dict[unit]

    converted_time = convert(time)
    if converted_time == -1:
      await ctx.send("You didnt set time correctly!")
      return
    if converted_time == -2:
      await ctx.send("Time must be a number")

    embed = discord.Embed(title="⏰ Reminder ⏰",color=discord.Color.red())
    embed.add_field(name= f"Hey there {ctx.author.name}", value=f"Reminder Started for **{task}** and will last for **{time}**\n")
    embed.set_footer(text=f"{watermark} by Scottminer22Gaming")
    await ctx.send(embed = embed)
    
    await asyncio.sleep(converted_time)
    await ctx.send(f"{ctx.author.mention}, You have a message!")
    embed = discord.Embed(title="⏰ Reminder ⏰",color=discord.Color.red())
    embed.add_field(name= f"Hey there {ctx.author.name}", value=f"Your Reminder for **{task}** has been finished!\n")
    embed.set_footer(text=f"{watermark} by Scottminer22Gaming")
    await ctx.send(embed = embed)

def setup(client):
  client.add_cog(reminder(client))
