import disnake
from disnake.ext import commands
import asyncio
from asyncio import sleep
from cogs.config.variables import watermark,owner,ownername
import aiohttp
import random
import requests
import json

class fun(commands.Cog):
  def __init__(self, client):
    self.client = client

    print("Loading fun module")

  #shipmeter
  @commands.command()
  @commands.cooldown(2,5,commands.BucketType.guild)
  async def ship(self, ctx, personne1, personne2):
      love_rate = str(random.randrange(0, 100))
      if '@' in personne1 or '@' in personne2:
        await ctx.send("``Use Plain text names! Dont use mentions!``")
      else:
          embed = disnake.Embed(title="Ship Rate", description="Measures love between two people!", color=ctx.author.color)
          embed.add_field(name= f"The ship between {personne1} and {personne2}", value=f"is **{love_rate}%** <:flushed:830502924479758356>")
          embed.set_footer(text=f"{watermark} by {ownername}")
          await ctx.send(embed = embed)

  #8ball
  @commands.command(name='8ball')
  @commands.cooldown(2,5,commands.BucketType.guild)
  async def eightball(self,ctx,*,question):
    responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.","Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.","Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.","Yes.", "Yes – definitely.", "You may rely on it."]
    await ctx.send(f':8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)}')

  #poll
  @commands.command()
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def poll(self,ctx, *,message):
    embed=disnake.Embed(title="Polling Time!", description=f'{message}', color=ctx.author.color)
    embed.set_footer(text=f"{watermark} by {ownername}")
    msg = await ctx.channel.send(embed = embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    await msg.add_reaction('🖖')


  #emojify
  @commands.command()
  @commands.cooldown(2,10,commands.BucketType.guild)
  async def emojify(self,ctx,*,text):
    emojis = []
    for s in text.lower():
      if s.isdecimal():
        num2emo = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
        emojis.append(f':{num2emo.get(s)}:')
      elif s.isalpha():
        emojis.append(f':regional_indicator_{s}:')
      else:
        emojis.append(s)
    await ctx.send(''.join(emojis))


  #cat
  @commands.command()
  @commands.cooldown(2,5,commands.BucketType.guild)
  async def cat(self,ctx):
        response = requests.get('https://aws.random.cat/meow')
        data = response.json()
        embed = disnake.Embed(
            title = 'Kitty Cat 🐈',
            description = 'Cats :star_struck:',
            color=ctx.author.color
            )
        embed.set_image(url=data['file'])            
        embed.set_footer(text=f"{watermark} by {ownername}")
        await ctx.send(embed=embed)

  #dog
  @commands.command()
  @commands.cooldown(2,5,commands.BucketType.guild)
  async def dog(self,ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/dog')
        dogjson = await request.json()
        request2 = await session.get('https://some-random-api.ml/facts/dog')
        factjson = await request2.json()

    embed = disnake.Embed(title="Doggo!", color=ctx.author.color)
    embed.set_image(url=dogjson['link'])
    embed.set_footer(text=factjson['fact']+f'\n{watermark} by {ownername}')
    await ctx.send(embed=embed)

  #dadjokes
  @commands.command()
  @commands.cooldown(2,5,commands.BucketType.guild)
  async def dadjoke(self,ctx):
    api = 'https://icanhazdadjoke.com/'
    async with aiohttp.request('GET', api, headers={'Accept': 'text/plain'}) as r:
      result = await r.text()
      await ctx.send('``' + result + '``')

  #memer
  @commands.command(name='meme')
  @commands.cooldown(2,5,commands.BucketType.guild)
  async def meme(self,ctx):
    async with aiohttp.ClientSession() as session:
      url = "https://meme-api.herokuapp.com/gimme"
      async with session.get(url) as response:
        response = await response.json()
        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
        embed = disnake.Embed(title= response['title'],url = response['postLink'],color = random.choice(colors))
        embed.set_image(url=response['url'])
        embed.set_footer(text=f"r/{response['subreddit']} | Meme Requested by {ctx.author.name} | Enjoy your dank memes! | {watermark} by {ownername}")
        await ctx.send(embed=embed)

#avatar
  @commands.command()
  async def avatar(self,ctx, member: disnake.Member=None):
      if member is None:
          member = ctx.author

      favatar = disnake.Embed(title=f"{member.name}'s avatar", color=0x000000)
      favatar.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator} | {watermark} by {ownername}")
      favatar.set_image(url='{}'.format(member.avatar.url))

      await ctx.send(embed = favatar)
      await ctx.message.delete()
 

def setup(client):
  client.add_cog(fun(client))
