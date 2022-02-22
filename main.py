#main.py
import disnake
from cogs.config.variables import token,prefix,owner,watermark,status
from handlers.keep_alive.keep_alive import keep_alive
from disnake.ext import commands,tasks

keep_alive()
intents= disnake.Intents.default()
intents.members = True
client = commands.AutoShardedBot(shard_count=4, command_prefix= prefix, help_command=None, intents=intents)

@client.event
async def on_ready():
    #bot status
    await client.change_presence(activity=disnake.Game(name=status))
    #import commands
    client.load_extension("cogs.help.helpmenu")
    client.load_extension("cogs.secret.secrets")
    client.load_extension("cogs.ai.ai")
    client.load_extension("cogs.channelchange.create_delete")
    client.load_extension("cogs.fun.fun")
    client.load_extension("cogs.reminder.reminder")
    client.load_extension("cogs.sendmessage.sendmsg")
    client.load_extension("cogs.stats.serverinfo")
    #import handlers
    client.load_extension("handlers.Cooldown.cooldown")
    client.load_extension("handlers.MissingArguements.missingarg")
    client.load_extension("handlers.MissingCommands.nocom")
    print("End of Initialisation")
    #inport links
    client.load_extension("links.links")
    #import experiments
    client.load_extension("experimental.snipe")
    #import owner commands
    client.load_extension("owner.owner")
    #import music module
    client.load_extension("music.music")
@client.command()
async def unloadcog(ctx, cog: str):
    if ctx.author.id == owner:
        try:
            client.unload_extension(f'{cog}')
        except Exception:
            await ctx.send("Couldnt Unload Cog")
            return
        await ctx.send("Unloaded Cog!")


@client.command()
async def loadcog(ctx, cog: str):
    if ctx.author.id == owner:
        try:
            client.load_extension(f'{cog}')
        except Exception:
            await ctx.send("Couldnt load Cog")
            return
        await ctx.send("loaded Cog!")


@client.command()
async def reloadcog(ctx, cog: str):
    if ctx.author.id == owner:
        try:
            client.unload_extension(f'{cog}')
            client.load_extension(f'{cog}')
        except Exception:
            await ctx.send("Couldnt reload Cog")
            return
        await ctx.send("reloaded Cog!")

@client.command()
async def importcog(ctx, cog: str):
    if ctx.author.id == owner:
        try:
            client.load_extension(f'{cog}')
        except Exception:
            await ctx.send("Couldnt load Cog")
            return
        await ctx.send("Imported Cog!")


client.run(token)
