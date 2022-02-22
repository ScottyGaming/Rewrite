import disnake as discord
from disnake.ext import commands
from cogs.config.variables import watermark,ownername

class missarg(commands.Cog):
  def __init__(self, client):
    self.client = client
    print("Loading Missing arguement error handler module")

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    global prefix
    if isinstance(error, commands.MissingRequiredArgument):
      em = discord.Embed(title=f"Error", description=f"Please Mention All Arguments!", color=ctx.author.color)
      em.set_footer(text=f"{watermark} by {ownername}") 
      await ctx.send(embed=em)

def setup(client):
  client.add_cog(missarg(client))