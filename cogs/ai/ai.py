#aiimports

import requests
from disnake.ext import commands

class ai(commands.Cog):
  def __init__(self, client):
    self.client = client
    print("Loading ai module")

  @commands.command(name='ai')
  async def _ai(self,ctx,arg):  
      url = "http://api.brainshop.ai/get?bid=161236&key=m02EGuDJ4TMMWIj5&uid=123456&msg="
      url += arg
      response = requests.request("GET", url)
      responseedit1 = response.text[8::]
      responseeditfinal = responseedit1[0:-2]
      await ctx.channel.send(f"``{responseeditfinal}``")


def setup(client):
  client.add_cog(ai(client))

#if it works then dont put too much effort - sun tzu the art of war
#let this remain here
#Flouse was here