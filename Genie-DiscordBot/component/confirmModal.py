import discord
import webbrowser
from discord.ui import Button


class Confirm(discord.ui.View):
    def __init__(self, url="", confirm_button_msg="", user=None):
        super().__init__()
        self.url = url
        self.user = user

        confirm_button = Button(
            label=confirm_button_msg, style=discord.ButtonStyle.green
        )
        confirm_button.callback = self.confirm_callback

        cancel_button = Button(label="Cancel", style=discord.ButtonStyle.grey)
        cancel_button.callback = self.cancel_callback

        self.add_item(confirm_button)
        self.add_item(cancel_button)

    async def confirm_callback(self, interaction):
        if interaction.user == self.user:
            await interaction.response.edit_message(view=None)
            webbrowser.open_new_tab(self.url)

    async def cancel_callback(self, interaction):
        if interaction.user == self.user:
            await interaction.response.edit_message(view=None)
