import os
import discord
from discord.ext import commands
from component.confirmModal import Confirm
from utils.api_call import check_social_account


class Send(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def send(self, ctx, *args) -> None:
        from_id = ctx.author.id
        from_name = ctx.author.name
        from_discriminator = ctx.author.discriminator
        from_avatar = ctx.author.avatar

        if not check_social_account(from_id, str(ctx.author)):
            await ctx.reply(
                "Please try again."
            )
            return

        args = list(args)
        
        if len(args) == 2 and (args[0] == "token" or args[0] == "nft"):
            to_user = discord.utils.get(ctx.message.mentions, id=int(args[1].strip('<@!>')))

            if not check_social_account(to_user.id, str(to_user)):
                await ctx.reply(
                    "Please try again."
                )
                return

            view = Confirm(
                url=f"{os.environ['FRONTEND_ENDPOINT']}/solana/send{args[0]}?snsName=Discord&from={from_id}&to={to_user.id}",
                confirm_button_msg="Go",
                user=ctx.author,
            )
            await ctx.reply(
                f"Hey {from_name}#{from_discriminator} ! Go to Genie for sending assets to {args[1]} :genie:\n"
                f"This message disappear after 10 seconds.",
                view=view,
                delete_after=10.0,
            )

        else:
            await ctx.reply(
                "Please try again."
            )

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Send(bot))
