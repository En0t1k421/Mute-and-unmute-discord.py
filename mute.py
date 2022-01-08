import discord
from discord.ext import commands, tasks
import asyncio
import datetime


#mute
@client.command()
@commands.has_permissions(view_audit_log=True)
async def mute(ctx,member:discord.Member,time: int, reason):
    role = discord.utils.get(ctx.guild.roles,id=813847909845041154)
    channel = client.get_channel(817829676772360192)
    await member.add_roles(role)
    emb = discord.Embed(title="Пользователь получил мут!",color=0xc25151)
    emb.add_field(name='Модератор/админ:',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель:',value=member.mention,inline=False)
    emb.add_field(name='Причина:',value=reason,inline=False)
    emb.add_field(name="Время:",value=time,inline=False)
    emb.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/813129913409601550/817735685841747978/08e7aac43809d99b.png')
    emb.set_footer (text = f'Вызвано: {ctx.message.author}', icon_url = ctx.message.author.avatar_url)
    await channel.send(embed = emb)
    await asyncio.sleep(time*60 )

@client.command()
@commands.has_permissions(view_audit_log=True)
async def unmute(ctx,member:discord.Member):
    role = discord.utils.get(ctx.guild.roles,id=813847909845041154)
    channel = client.get_channel(817829676772360192)

    emb = discord.Embed(title="С пользователя был снят мут!",color=0xc25151)
    emb.add_field(name='Модератор/админ:',value= ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель:',value=member.mention,inline=False)
    emb.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/813129913409601550/817735685841747978/08e7aac43809d99b.png')
    emb.set_footer (text = f'Вызвано: {ctx.message.author}', icon_url = ctx.message.author.avatar_url)
    await channel.send(embed=emb)
    await member.remove_roles(role)



@mute.error
async def mute_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            emb = discord.Embed(title = f"Ошибка!", description = f'Пользователь не найден.', colour = 0xce0000)
            emb.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = emb)
        else:
            if isinstance(error, commands.MissingPermissions):
                await ctx.send(embed = discord.Embed(title = f"❌ в доступе отказано!", description = f"{ctx.author.name}, у вас нету нужных прав!" , color = ERROR))
            else:
                if isinstance(error, commands.MissingRequiredArgument):
                    await ctx.send(embed = discord.Embed(title = f"Ошибка!", description = f" {ctx.author.name}, укажите аргумент!" , color = ERROR ))

@unmute.error
async def unmute_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            emb = discord.Embed(title = f"Ошибка!", description = f'Пользователь не найден.', colour = 0xce0000)
            emb.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = emb)



"""BY EN0T1K421"""