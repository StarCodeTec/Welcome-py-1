import discord
from discord.ext import commands
import textwrap
import io
import traceback
import os
import sys
sys.path.append('../..')
from passcodes import main
sudoPassword=main.dbc
sys.path.append('busboy/bot')
import traceback
from contextlib import redirect_stdout

def cleanup_code(content):
    """Automatically removes code blocks from the code in the eval command."""
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    # remove `foo`
    return content.strip('` \n')

class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True, name='eval', aliases=['e'])
    async def _eval(self, ctx, *, body: str):
        """Runs Python code."""
        if ctx.author.id != 599059234134687774:
            return
            
        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': None
        }

        env.update(globals())

        body = cleanup_code(body)
        
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                await ctx.send(f'```py\n{value}{ret}\n```')
