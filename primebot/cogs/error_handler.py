import discord
import math
from discord.ext import commands


class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # my log channel
        errorChannel = self.bot.get_channel(799848546823307295)
        await errorChannel.send('Unhandled Message: {} \n Content: {} \n Error: {}\n'.format(ctx.message, ctx.message.content, error))
        with open('error.log', 'a') as f:
            f.write('Unhandled Message: {} \n Content: {} \n Error: {}\n'.format(ctx.message, ctx.message.content, error))
        if isinstance(error, commands.CheckFailure):
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=":x: You don't have the permission to execute this bot command!"))
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=":x: The bot command doesn't exist!"))
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=":x: The command is incomplete, missing one or more parameters!"))
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=":x: The command was entered incorrectly, one or more parameters are wrong or in the wrong place!"))
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("This command is on cooldown, please retry in {}s.".format(math.ceil(error.retry_after)))


def setup(bot):
    bot.add_cog(Error(bot))
