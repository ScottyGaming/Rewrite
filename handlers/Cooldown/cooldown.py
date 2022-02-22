import disnake as discord
from disnake.ext import commands
from cogs.config.variables import watermark,ownername

class cool(commands.Cog):
  def __init__(self, client):
    self.client = client
    print("Loading Missing arguement error handler module")

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    global watermark
    if isinstance(error, commands.CommandOnCooldown):
      em = discord.Embed(title="This command is on cooldown for {:.2f}s".format(error.retry_after), color=ctx.author.color) 
      em.set_footer(text=f"{watermark} by {ownername}")
      await ctx.channel.send(embed=em)
def setup(client):
  client.add_cog(cool(client))