from my_liberes.settings import * # Импортируем настройки (Токен и т.д)
import discord # Подключаем библиотеку
from discord.ext import commands
import colorama # Библиотека для изменения цвета текста
from colorama import Fore, Back, Style

colorama.init() # Инициализируем библиотеку для изменения цвета текста

intents = discord.Intents.all() # Выдаём все права


# Проверка на токен

if token == " ":
    print(Fore.RED + "Вы не указали токен в папке ./my_liberes/setting.py" + Style.RESET_ALL)
    print("")
    

# Задаём префикси интетнты

bot = commands.Bot(command_prefix='/', intents=intents)


# Выдача ролей по реакции

@bot.event

async def on_member_join(member):
    channel = bot.get_channel(1072220205469667339) # Канал "верификация"
    role1 = member.guild.get_role(1057384839759798342) # Роль "NOT VIRIFIED"
    await member.add_roles(role1) # При входе даём роль: NOT VIRIFIED
    await channel.send(embed = discord.Embed( # Отправляем эмбет
        title = 'Новый путник',
        description = f'Путник под никнеймом "{member} - " ступил на наш сервер',
        colour = discord.Colour.from_rgb(106, 192, 245)))


@bot.event
async def on_raw_reaction_add(payload): # Если кто-то поставил реакцию

    if payload.message_id == 1057580872997535754: # Если сообщение есть то:
        member = payload.member # Пользыватель
        if payload.emoji.name == 'verifi': # Если поставленная реакция то:
            role = discord.utils.get(member.guild.roles, id=1061643162176733264) # Роль "UNDECIDED"
            role1 = discord.utils.get(member.guild.roles, id=1057384839759798342) # Роль "NOT VIRIFIED"
            await member.add_roles(role) # Выдаёт роль пользователю
            await member.remove_roles(role1) # Удаляет роль у пользывателя

# Команда /say #
@bot.command()
async def say(ctx, message):
    member = ctx.message.author
    member_id = member.id
    if member_id == 1050826802660114523: # Если id пользывателя который отправил команду совпадает с моим то выполнить:
        await ctx.send(message)
        await ctx.message.delete()
    else: # Если нет то:
        await ctx.send("У вас нету прав")
        await ctx.message.delete()

# Авто-роли #

@bot.event
async def on_raw_reaction_add(payload): # Если кто-то поставил реакцию
    member = payload.member
    if payload.message_id == 1076433780832743464: # И если это сообщение с выдачей авто ролей
        if payload.emoji.name == 'python' or payload.emoji.name == 'java' or payload.emoji.name=='cs' or payload.emoji.name=='c_plus_plus' or payload.emoji.name=='go' or payload.emoji.name=='java_script' or payload.emoji.name=='php' or payload.emoji.name=='html' or payload.emoji.name=='css' or payload.emoji.name=='rust' or payload.emoji.name=='swift' or payload.emoji.name=='ruby' or payload.emoji.name=='kotlin' or payload.emoji.name=='sql' or payload.emoji.name=='lua' or payload.emoji.name=='arduino':
            global python, java, cs, c_plus_plus, go, javascript, php, html, css, rust, swift, ruby, kotlin, sql, lua, arduino
            python = discord.utils.get(member.guild.roles, id=1074265237198479361) # Python
            java = discord.utils.get(member.guild.roles, id=1074968802103656448) # Java
            cs = discord.utils.get(member.guild.roles, id=1074969023063797770) # C#
            c_plus_plus = discord.utils.get(member.guild.roles, id=1061647568519581726) # C++
            go = discord.utils.get(member.guild.roles, id=1074969472420552736) # Golang
            javascript = discord.utils.get(member.guild.roles, id=1061646954129530900) # javascript
            php = discord.utils.get(member.guild.roles, id=1074969749076840530) # php
            html = discord.utils.get(member.guild.roles, id=1074969875551879239) # html
            css = discord.utils.get(member.guild.roles, id=1074969917511700501) # css
            rust = discord.utils.get(member.guild.roles, id=1074970030564982784) # rust
            swift = discord.utils.get(member.guild.roles, id=1074970381745651753) # swift
            ruby = discord.utils.get(member.guild.roles, id=1074970307024134184) # ruby
            kotlin = discord.utils.get(member.guild.roles, id=1074970425651638332) # kotlin
            sql = discord.utils.get(member.guild.roles, id=1074970587950223430) # sql
            lua = discord.utils.get(member.guild.roles, id=1074970668443127818) # lua
            arduino = discord.utils.get(member.guild.roles, id=1061647161026162698) # arduino ide
            if payload.emoji.name == 'python':
                await member.add_roles(python) # Выдаёт роль пользователю
            elif payload.emoji.name == 'java':
                await member.add_roles(java) # Выдаёт роль пользователю
            elif payload.emoji.name == 'cs':
                await member.add_roles(cs)
            elif payload.emoji.name == 'c_plus_plus':
                await member.add_roles(c_plus_plus)
            elif payload.emoji.name == 'go':
                await member.add_roles(go)
            elif payload.emoji.name == 'java_script':
                await member.add_roles(javascript)
            elif payload.emoji.name == 'php':
                await member.add_roles(php)
            elif payload.emoji.name == 'html':
                await member.add_roles(html)
            elif payload.emoji.name == 'css':
                await member.add_roles(css)
            elif payload.emoji.name == 'rust':
                await member.add_roles(rust)
            elif payload.emoji.name == 'swift':
                await member.add_roles(swift)
            elif payload.emoji.name == 'ruby':
                await member.add_roles(ruby)
            elif payload.emoji.name == 'kotlin':
                await member.add_roles(kotlin)
            elif payload.emoji.name == 'sql':
                await member.add_roles(sql)
            elif payload.emoji.name == 'lua':
                await member.add_roles(lua)
            elif payload.emoji.name == 'arduino':
                await member.add_roles(arduino)
@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if payload.message_id == 1076433780832743464: # И если это сообщение с выдачей авто ролей
        if (payload.emoji.name == 'python' or
        payload.emoji.name == 'java' or
        payload.emoji.name == 'cs' or
        payload.emoji.name == 'c_plus_plus' or
        payload.emoji.name == 'go' or
        payload.emoji.name == 'java_script' or
        payload.emoji.name == 'php' or
        payload.emoji.name == 'html' or
        payload.emoji.name == 'css' or
        payload.emoji.name == 'rust' or
        payload.emoji.name == 'swift' or
        payload.emoji.name == 'ruby' or
        payload.emoji.name == 'kotlin' or 
        payload.emoji.name == 'sql' or
        payload.emoji.name == 'lua' or
        payload.emoji.name == 'arduino'
        ):
            if payload.emoji.name == 'python':
                await member.remove_roles(python)
            elif payload.emoji.name == 'java':
                await member.remove_roles(java)
            elif payload.emoji.name == 'cs':
                await member.remove_roles(cs)
            elif payload.emoji.name == 'c_plus_plus':
                await member.remove_roles(c_plus_plus)
            elif payload.emoji.name == 'go':
                await member.remove_roles(go)
            elif payload.emoji.name == 'java_script':
                await member.remove_roles(javascript)
            elif payload.emoji.name == 'php':
                await member.remove_roles(php)
            elif payload.emoji.name == 'html':
                await member.remove_roles(html)
            elif payload.emoji.name == 'css':
                await member.remove_roles(css)
            elif payload.emoji.name == 'rust':
                await member.remove_roles(rust)
            elif payload.emoji.name == 'swift':
                await member.remove_roles(swift)
            elif payload.emoji.name == 'ruby':
                await member.remove_roles(ruby)
            elif payload.emoji.name == 'kotlin':
                await member.remove_roles(kotlin)
            elif payload.emoji.name == 'sql':
                await member.remove_roles(sql)
            elif payload.emoji.name == 'lua':
                await member.remove_roles(lua)
            elif payload.emoji.name == 'arduino':
                await member.remove_roles(arduino)
            
            

            





bot.run(token) # Запускаем бота