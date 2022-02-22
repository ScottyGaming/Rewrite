import disnake
from disnake.ext import commands
import asyncio
from asyncio import sleep
from cogs.config.variables import watermark,ownername

class secret(commands.Cog):
  def __init__(self, client):
    self.client = client

    print("Loading secret module")

  #dounasecret
  @commands.command()
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def douna(self,ctx):
      embed = disnake.Embed(title="Secret Command", description="this command is a secret obviously", color=ctx.author.color)
      embed.add_field(name= f"Dounasiudb...", value="We dont talk abt him anymore but he is still in our hearts!\n")
      embed.set_footer(text=f"{watermark} by {ownername}")
      await ctx.send(embed = embed)

  #scottysecret
  @commands.command()
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def scotty(self,ctx):
      embed = disnake.Embed(title="Secret Command", description="this command is a secret obviously", color=ctx.author.color)
      embed.add_field(name= f"Scotty aka Scottminer22 Gaming aka DarkScarlet", value="The Brilliant Creator of this Bot! Also likes pineapple on pizza!\n")
      embed.set_footer(text=f"{watermark} by {ownername}")
      await ctx.send(embed = embed)

  #tokosecret
  @commands.command()
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def toko(self,ctx):
      embed = disnake.Embed(title="Secret Command", description="this command is a secret obviously", color=ctx.author.color)
      embed.add_field(name= f"Toko Says:", value="I was wondering why the frisbee kept getting bigger and bigger, but then it hit me.\n")
      embed.add_field(name= f"Toko Says:", value="Coughing has finally overtaken speaking Arabic as the most taboo thing to do in an airport.")
      embed.add_field(name= f"Toko Says:", value="Chameleons are supposed to blend well, but I think it's ruined this smoothie.")
      embed.set_footer(text=f"{watermark} by {ownername}")
      await ctx.send(embed = embed)

  #fatriosecret
  @commands.command()
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def fatrio(self,ctx):
      embed = disnake.Embed(title="Secret Command", description="this command is a secret obviously", color=ctx.author.color)
      embed.add_field(name= f"Fatrio...", value="Fat\n")
      embed.set_footer(text=f"{watermark} by {ownername}")
      await ctx.send(embed = embed)
  
  #flousesecret
  @commands.command()
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def flouse(self,ctx):
      embed = disnake.Embed(title="Secret Command", description="this command is a secret obviously", color=ctx.author.color)
      embed.add_field(name= f"Flouse", value="is a good friend and owner of cool discord server windows support community join now!\n")
      embed.set_footer(text=f"{watermark} by {ownername}")
      await ctx.send(embed = embed)


def setup(client):
  client.add_cog(secret(client))