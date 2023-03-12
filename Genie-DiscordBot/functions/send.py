import discord
from discord.ext import commands
from component.confirmModal import Confirm


class Send(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def send(self, ctx, *args) -> None:
        from_id = ctx.author.id
        from_name = ctx.author.name
        from_discriminator = ctx.author.discriminator
        from_avatar = ctx.author.avatar

        args = list(args)
        view = Confirm()
        await ctx.reply(f"TEST MSG {str(args)}", view=view)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Send(bot))
