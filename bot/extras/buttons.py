import discord

class YesNo(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = False
        self.timeout = 20
        self.ctx = None

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
            if self.ctx.author.id != interaction.user.id:
                await interaction.response.send_message("These buttons aren't yours to press! :wink:", ephemeral=True)
                return False
            else:
                return True
    
    @discord.ui.button(label='Yes', style=discord.ButtonStyle.red)
    async def _yes(self, button: discord.ui.Button, interaction: discord.Interaction):
        
        self.value = True

        for child in self.children:
            child.disabled = True
        
        self.stop()

    @discord.ui.button(label='No', style=discord.ButtonStyle.grey)
    async def _no(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.value = False
        
        for child in self.children:
            child.disabled = True

        self.stop()