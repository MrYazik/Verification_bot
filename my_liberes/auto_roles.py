import discord # Подключаем библиотеку
from discord.ext import commands
from main import *



# Роли #

@bot.event
async def on_raw_reaction_add(payload): # Если кто-то поставил реакцию
    member = payload.member
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

# Имена emoji #
    global python_emoji, java_emoji, cs_emoji, c_plus_plus_emoji, go_emoji, javascript_emoji, php_emoji, html_emoji, css_emoji, rust_emoji, swift_emoji, ruby_emoji, kotlin_emoji, sql_emoji, lua_emoji, arduino_emoji
    python_emoji = payload.emoji.name == 'python'
    java_emoji = payload.emoji.name == 'java'
    cs_emoji = payload.emoji.name == 'cs'
    c_plus_plus_emoji = payload.emoji.name == 'c_plus_plus'
    go_emoji = payload.emoji.name == 'go'
    javascript_emoji = payload.emoji.name=='java_script'
    php_emoji = payload.emoji.name == 'php'
    html_emoji = payload.emoji.name == 'html'
    css_emoji = payload.emoji.name == 'css'
    rust_emoji = payload.emoji.name == 'rust'
    swift_emoji = payload.emoji.name == 'swift'
    ruby_emoji = payload.emoji.name == 'ruby'
    kotlin_emoji = payload.emoji.name == 'kotlin'
    sql_emoji = payload.emoji.name == 'sql'
    lua_emoji = payload.emoji.name == 'lua'
    arduino_emoji = payload.emoji.name == 'arduino'

# Откат #
@bot.event
async def on_raw_reaction_add(payload): # Если кто-то поставил реакцию
    member = payload.member
    if payload.message_id == 1074248067538223114: # И если это сообщение с выдачей авто ролей
        if (auto_roles.python_emoji or 
        auto_roles.java_emoji or 
        auto_roles.cs_emoji or 
        auto_roles.c_plus_plus_emoji or 
        auto_roles.go_emoji or 
        auto_roles.javascript_emoji or 
        auto_roles.php_emoji or 
        auto_roles.html_emoji or 
        auto_roles.css_emoji or 
        auto_roles.rust_emoji or 
        auto_roles.swift_emoji or 
        auto_roles.ruby_emoji or 
        auto_roles.kotlin_emoji or 
        auto_roles.sql_emoji or 
        auto_roles.lua_emoji or 
        auto_roles.arduino_emoji):

            if auto_roles.python_emoji:
                await member.add_roles(auto_roles.python) # Выдаёт роль пользователю

            elif auto_roles.java_emoji:
                await member.add_roles(auto_roles.java) # Выдаёт роль пользователю
            
            elif auto_roles.cs_emoji:
                await member.add_roles(auto_roles.cs)

            elif auto_roles.c_plus_plus_emoji:
                await member.add_roles(auto_roles.c_plus_plus)
            
            elif auto_roles.go_emoji:
                await member.add_roles(auto_roles.go)

            elif auto_roles.javascript_emoji:
                await member.add_roles(auto_roles.javascript)

            elif auto_roles.php_emoji:
                await member.add_roles(auto_roles.php)

            elif auto_roles.html_emoji:
                await member.add_roles(auto_roles.html)

            elif auto_roles.css_emoji:
                await member.add_roles(auto_roles.css)

            elif auto_roles.rust_emoji:
                await member.add_roles(auto_roles.rust)

            elif auto_roles.swift_emoji:
                await member.add_roles(auto_roles.swift)

            elif auto_roles.ruby_emoji:
                await member.add_roles(auto_roles.ruby)

            elif auto_roles.kotlin_emoji:
                await member.add_roles(auto_roles.kotlin)
            
            elif auto_roles.sql_emoji:
                await member.add_roles(auto_roles.sql)

            elif auto_roles.lua_emoji:
                await member.add_roles(auto_roles.lua)

            elif auto_roles.arduino_emoji:
                await member.add_roles(auto_roles.arduino)