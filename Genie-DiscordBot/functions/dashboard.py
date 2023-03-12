import os
from discord.ext import commands
from component.confirmModal import Confirm


class Dashboard(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def dashboard(self, ctx) -> None:
        from_id = ctx.author.id
        from_name = ctx.author.name
        from_discriminator = ctx.author.discriminator
        from_avatar = ctx.author.avatar

        view = Confirm(
            url=f"{os.environ['FRONTEND_ENDPOINT']}/dashboard",
            confirm_button_msg="Go",
            user=ctx.author,
        )
        await ctx.reply(
            f"Hey {from_name}#{from_discriminator} ! Go to Genie Dashboard :genie:\nThis message disappear "
            f"after 10 seconds.",
            view=view,
            delete_after=10.0,
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Dashboard(bot))
