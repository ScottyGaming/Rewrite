import disnake as discord
from disnake.ext import commands
from cogs.config.variables import watermark,ownername
 
class nocom(commands.Cog):
  def __init__(self, client):
    self.client = client
    print("Loading No Command error handler module") 
  
  @commands.Cog.listener() 
  async def on_command_error(self, ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
      em = discord.Embed(title=f"Error", description=f"Command doesnt exist.", color=ctx.author.color)
      em.set_footer(text=f"{watermark} by {ownername}") 
      await ctx.send(embed=em)
    

def setup(client):
  client.add_cog(nocom(client))