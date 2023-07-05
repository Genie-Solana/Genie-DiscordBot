import os
from discord.ext import commands
from component.confirmModal import Confirm
from utils.api_call import check_social_account


class Wallet(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def register(self, ctx) -> None:
        from_id = ctx.author.id
        from_name = ctx.author.name
        from_discriminator = ctx.author.discriminator
        from_avatar = ctx.author.avatar
        
        if not check_social_account(from_id, str(ctx.author), from_avatar):
            await ctx.reply(
                "Please try again."
            )
            return

        view = Confirm(
            url=f"{os.environ['FRONTEND_ENDPOINT']}/mypage?snsName=Discord&discordId={from_id}",
            confirm_button_msg="Go",
            user=ctx.author,
        )
        await ctx.reply(
            f"Hey {from_name}#{from_discriminator} ! Go to Genie for register wallet :genie:\nThis message disappear "
            f"after 10 seconds.",
            view=view,
            delete_after=10.0,
        )

    @commands.command()
    async def unregister(self, ctx) -> None:
        from_id = ctx.author.id
        from_name = ctx.author.name
        from_discriminator = ctx.author.discriminator
        from_avatar = ctx.author.avatar
        
        if not check_social_account(from_id, str(ctx.author), from_avatar):
            await ctx.reply(
                "Please try again."
            )
            return

        view = Confirm(
            url=f"{os.environ['FRONTEND_ENDPOINT']}/mypage?snsName=Discord&discordId={from_id}",
            confirm_button_msg="Go",
            user=ctx.author,
        )
        await ctx.reply(
            f"Hey {from_name}#{from_discriminator} ! Go to Genie for unregister wallet :genie:\nThis message disappear "
            f"after 10 seconds.",
            view=view,
            delete_after=10.0,
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Wallet(bot))
