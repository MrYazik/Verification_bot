from settings import *
import discord # Подключаем библиотеку
from discord.ext import commands

intents = discord.Intents.all()


# Задаём префикси интетнты

bot = commands.Bot(command_prefix='/', intents=intents)

# Выдача ролей по реакции

@bot.event

async def on_member_join(member):
    channel = bot.get_channel(1072220205469667339)
    role = member.guild.get_role(1057384839759798342)
    await member.add_roles(role)
    await channel.send(embed = discord.Embed(
        title = 'Новый путник',
        description = f'Путник под никнеймом "{member} - " ступил на наш сервер',
        colour = discord.Colour.from_rgb(106, 192, 245)))


@bot.event
async def on_raw_reaction_add(payload):

    if payload.message_id == 1057580872997535754: # Если сообщение есть то:
        member = payload.member # Пользыватель
        if payload.emoji.name == '🟢': # Если поставленная реакция то:
            role = discord.utils.get(member.guild.roles, id=1061643162176733264) # Роль "UNDECIDED"
            role1 = discord.utils.get(member.guild.roles, id=1057384839759798342) # Роль "NOT VIRIFIED"
            await member.add_roles(role) # Выдаёт роль пользователю
            await member.remove_roles(role1) # Удаляет роль у пользывателя
        


bot.run(token)