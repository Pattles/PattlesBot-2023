import datetime
from datetime import datetime, timezone

import discord
import asyncio
from discord import app_commands
from discord.ext import commands

from functions import *
from bot import *

preferences = load_json('./info/preferences.json')

class Management(commands.Cog):
    def __init__(self, bot:PattlesBot):
        self.bot = bot
    
    @commands.hybrid_command(description='Adds a role to a member.')
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, role:discord.Role, member:discord.Member):
        await member.add_roles(role)
        
        embed = discord.Embed(title='Successfully added role to member.', description=f'Added {role.mention} to {member.mention}.', color=self.bot.color)
        await ctx.send(embed=embed)

    @commands.hybrid_command(description='Deletes a specified amount of messages in the channel.', aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount:int):
        embed = discord.Embed(description='Working...', color=self.bot.color)
        msg = await ctx.send(embed=embed)
        await msg.delete()

        embed = discord.Embed(description=f"Successfully deleted `{amount}` messages.", color=self.bot.color)

        await ctx.channel.purge(limit=amount + 1)
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(2)
        await msg.delete()


async def setup(bot):
    await bot.add_cog(Management(bot))