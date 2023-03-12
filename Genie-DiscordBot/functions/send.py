from discord.ext import commands
from discord.ui import View


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

        await ctx.send(f"Hello {from_id}")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Send(bot))
