import discord
from bs4 import BeautifulSoup
from cleverbot import async_ as cleverbot
import aiohttp
import json
import sqlite3
import math
import time
import datetime
from discord.ext import commands
import os
import random
import webbrowser as web
from time import sleep as offset
startup_extensions = ["Music"]
import requests
from discord.ext.commands import Bot
prefix = "/"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")
client = discord.Client()
bot.remove_command("help")
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="AQ3D Community ~ Melodia Bot", description="Here you will find all the help you need. Not satisfied? Tag one of the mods or staff members", color=0x00a0ea)
    embed.add_field(name="Character Page".format("null"), value="Use /char for your AQ3D Character profile. Example /char Artix")
    embed.add_field(name="AQ3D Servers Status".format("null"), value="Use /status to see AQ3D's servers current status.")
    embed.add_field(name="Wiki".format("null"), value="Use /item ItemName to fetch info from an AQ3D item. Example: /item Alpha Knight Armor. (Note: This feature is in progress)")
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/579170793020325888/586399925202583561/ER21_Logo.png")
    embed.set_footer(text="Melodia Bot © ~ Developed with ❤ for the AQ3D Community")
    await bot.say(embed=embed)     
cb = cleverbot.Cleverbot('YOUR_API_KEY', cs='76nxdxIJ02AAA', timeout=60, tweak1=0, tweak2=100, tweak3=100)
try:
    cb.say("Hello")
except cleverbot.APIError as error:
    print(error.error, error.status)
cb.close()

@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '337343219128074240':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)
@bot.command()
async def ping(ctx):
    await bot.say('Pong! {0}'.format(round(bot.latency, 1)))
@bot.command()
async def shopcmd():
    await bot.say("wiki.daily ~ daily cash rewards")
    await bot.say("wiki.shop ~ opens the shop")
    await bot.say("wiki.cash ~ displays your cash amount")
    await bot.say("wiki.inventory ~ displays your inventory")
    await bot.say("wiki.buy \"itemname\" ~ buys an item")
@bot.command()
async def dashboard():
    embed=discord.Embed(title="Dashboard", url="https://helixbotdashboard.herokuapp.com/", description="Click Dashboard to access HelixBot web dashboard.", color=0x463dfc)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def suggest(ctx, member : discord.Member, *, content: str):
    await bot.send_message(member, content)
@bot.command()
async def news():
    await bot.say("https://www.aq3d.com/news")

global categories
categories = ["helms", "shoulders", "armors", "boots", "gloves", "belts", "capes"]
@bot.command()
async def say(*, mess: str):
    await bot.say(mess)
@bot.command()
async def invite():
    await bot.say("Invite me with this link: https://discordapp.com/oauth2/authorize?client_id=441753103721824257&scope=bot")
@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))
@bot.command()
async def servers():
    embed = discord.Embed(title="Bot Server Count", description="Servers the bot is in.", color=0x00ff00)
    embed.add_field(name="Servers: ", value=len(bot.servers))
    await bot.say(embed=embed)
letter_a = ["Alpha Knight Armor"]
letter_b = ["Basic Armor", "Battleon Militia", "Beta Berserker", "Blood Knight", "Blue Eye Leather Robe", "Blue Eye Leather Outfit", "Blue Villager Clothing", "Boreal Robe" ]
letter_c_1 = ["Campy Rogue", "Campy Warrior", "Chewed Mystic Robes", "Chewed Warrior Armor", "Chiropteran Armor", "Campy Mage", "Crimson Mage Robes"]
letter_c_2 = ["Chronomancer Armor", "Clawed Rogue Outfit", "Common Darkovian Clothes", "Common Darkovian Dress", "Crimson Battle Mage Robe", "Crusty Inn Keeper Clothes"]
letter_d_1 = ["Dark Defender Armor", "David's Coat", "Defender Guardian Armor", "Defender Knight Armor", "Defender Mage Robes", "Defender Rogue Armor"]
letter_d_2 = [ "Dragon Berserker Armor", "Dragon Champion Armor", "Dragon Stalker Flame Tabard", "Dragon Stalker Gold Tabard", "Dragon Stalker Sky Tabard" "Dragon SLayer Armor"]
letter_d_3 = ["Drake Hunter Flame Tabard", "Drake Hunter Gold Tabard", "Drake Hunter Sky Tabard", "Dread Hood Armor", "Dricken Feathered Robe"]
letter_d_4 = ["Dricken Scaled Armor", "Dusk Hunters Tunic", "Dwarven Foreman Armor", "Dwarven Miner Armor"]
letter_e = ["Ebon Talon Armor", "Elite Dragon Champion", "Elvenguard Armor", "Eternal Chronomancer Armor"]
letter_f = ["Forest Tunic", "Fire Mage Robe", "Fire Rogue Outfit"]
@bot.command(pass_context=True)
async def armors(ctx):
    embed = discord.Embed(title="Armors", description="Current armors listed in the wiki bot.", color=0x00a0ea)
    embed.set_thumbnail(url="https://thumb.ibb.co/jnBPB7/descarga.png")
    embed.add_field(name="Letter A", value=letter_a)
    embed.add_field(name="Letter B", value=letter_b)
    embed.add_field(name="Letter C", value=letter_c_1)           
    embed.add_field(name="Letter C", value=letter_c_2)
    embed.add_field(name="Letter D", value=letter_d_1)
    embed.add_field(name="Letter D", value=letter_d_2)
    embed.add_field(name="Letter D", value=letter_d_3)
    embed.add_field(name="Letter D", value=letter_d_4)
    embed.add_field(name="Letter E", value=letter_e)
    embed.add_field(name="Letter F", value=letter_f)
    await bot.say(embed=embed)
    

    
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))    
 
belts1 = ['adventurersbelt','alphaknightbelt', 'alphapiratebelt', 'ancientevilwrap', 'ashbrandbelt']
belts2 = ['betaberserkerbelt', 'burntsash', 'campybelt', 'chiropteranbelt', 'chronomancerbelt']
belts3 = ['crimsonbattlemagebelt', 'davidsbelt', 'defenderroguebelt', 'dragonberserkerbelt', 'dragonchampionwrap']
belts4 = ['dragonstalkerbelt', 'dragonslayerbelt', 'drakehunterbelt', 'drickenscaledbelt', 'drickentrophy'] 
belts5 = ['dwarvenminerbelt', 'elitedragonchampionwrap', 'elvenguardbelt', 'eternalchronomancerbelt','firemagesash']
belts6 = ['fireroguebelt', 'frostdefenderbelt', 'frostlornmagebelt']
@bot.command(pass_context=True)
async def belts(ctx):
    embed = discord.Embed(title="belts", description="Current belts listed in the wiki bot.", color=0x00a0ea)
    embed.set_image(url="https://thumb.ibb.co/hheFjx/ndice.png")
    embed.add_field(name="Belts List", value=belts1)
    embed.add_field(name="Belts List", value=belts2)
    embed.add_field(name="Belts List", value=belts3)             
    embed.add_field(name="Belts List", value=belts4)
    embed.add_field(name="Belts List", value=belts5)
    embed.add_field(name="Belts List", value=belts6)
    await bot.say(embed=embed) 
@bot.command()
async def status():
    async with aiohttp.ClientSession() as session: 
        async with session.get("http://game.aq3d.com/api/game/ServerList") as response:
            parsed = json.loads(await response.text())
            embed = discord.Embed(title="AQ3D Server Status", description="Artix Entertainment :copyright:", color=0x00ff00)
            embed.add_field(name="Total Online :earth_americas:", value=parsed[0]["UserCount"] + parsed[2]["UserCount"])
            embed.add_field(name="Red Dragon :red_circle:", value=parsed[0]["UserCount"])
            embed.add_field(name="Blue Dragon :large_blue_circle:", value=parsed[2]["UserCount"])
            await bot.say(embed=embed)
@bot.command(pass_context=True)
async def rootrealm(ctx):
    await bot.say('http://game.aq3d.com/api/game/ServerList')
chronomancer_armor = {
    'chronomancer armor', 'Chronomancer armor', 'Chronomancer Armor'
}
alpha_knight_armor = {
    'Alpha Knight Armor', 'Alpha knight armor', 'alpha knight armor'
}
battleon_militia_armor = {
    'Battleon Militia Armor', 'Battleon militia armor', 'battleon militia armor'
}
beta_berserker = {
    'Beta Berserker Armor', 'Beta berserker armor', 'beta berserker armor'

}
blood_knight_armor = {
    'Blood Knight Armor', 'Blood knight armor','blood knight armor'
}
campy_rogue = {
    'Campy Rogue', 'Campy rogue', 'campy rogue'
}
campy_warrior = {
    'Campy Warrior', 'Campy warrior', 'campy warrior'
}
chewed_mystic_robes = {
    'Chewed Mystic Robes', 'Chewed mystic robes', 'chewed mystic robes'
}
chewed_warrior_armor = {
    'Chewed warrior armor', 'Chewed Warrior Armor', 'chewed warrior armor'
}
chiropteran_armor = {
    'Chiropteran Armor', 'Chiropteran armor', 'chiropteran armor'
}
clawed_rogue_outfit = {
    'Clawed Rogue Outfit', 'Clawed rogue outfit', 'clawed rogue outfit'
}
commondarkovianclothes = {
    'Common Darkovian Clothes', 'Common darkovian clothes',
}
commondarkoviandress = {
    'Common Darkovian Dress', 'Common darkovian dress', 'common darkovian dress'
}
crimsonbattlemagerobe = {
    'Crimson Battle Mage Robe', 'Crimson battle mage robe', 'crimson battle mage robe'
}
crimsonmagerobes = {
    'Crimson Mage Robes', 'Crimson mage robes', 'crimson mage robes'
}
crustyinnkeepersclothes = {
    'Crusty inn keepers clothes'
}
darkdefenderarmor = {
    'Dark Defender Armor', 'Dark defender armor', 'dark defender armor'
}
davidscoat = {
    'Davids Coat', 'Davids coat', 'davids coat', 'david\'s coat'
}
drakehuntergoldtabard = {
    'Drake Hunter Gold Tabard', 'Drake hunter gold tabard', 'drake hunter gold tabard'
}
drakehunterskytabard = {
    'Drake Hunter Sky Tabard', 'Drake hunter sky tabard', 'drake hunter sky tabard'
}
defenderguardianarmor = {
    'Defender Guardian Armor', 'Defender guardian armor', 'defender guardian armor'
}
drakehunterflametabard = {
    'Drake Hunter Flame Tabard', 'Drake hunter flame tabard', 'drake hunter flame tabard'
}
drickenfeatheredrobe = {
    'Dricken Feathered Robe', 'Dricken feathered robe', 'dricken feathered robe'
}
defenderknightarmor = {
    'Defender Knight Armor', 'Defender knight armor', 'defender knight armor'
}
defendermagerobes = {
    'Defender Mafe Robes', 'Defender mage robes', 'defender mage robes'
}
defenderroguearmor = {
    'Defender Rogue Armor', 'Defender rogue armor', 'defender rogue armor'
}
dragonberserkerarmor = {
    'Dragon Berserker Armor', 'Dragon berserker armor', 'dragon berserker armor'
} 
dragonslayerarmor = {
    'Dragon Slayer Armor', 'DragonSlayer Armor', 'Dragon slayer armor', 'Dragonslayer armor', 'dragon slayer armor', 'dragonslayer armor'
}
dragonchampionarmor = {
    'Dragon Champion Armor', 'Dragon champion armor', 'dragon champion armor'
}
dragonstalkerflametabard = {
    'Dragon Stalker Flame Tabard', 'Dragon stalker flame tabard', 'dragon stalker flame tabard'
}
dragonstalkerskytabard = {
    'Dragon Stalker Sky Tabard', 'Dragon stalker sky tabard', 'dragon stalker sky tabard'
}
dreadhoodarmor = {
    'Dread Hood Armor', 'Dread hood armor', 'dread hood armor', 'dreadhood armor'
}
drickenfeatheredarmor = {
    'Dricken Feathered Armor', 'Dricken feathered armor', 'dricken feathered armor'
}
drickenscaledarmor = {
    'Dricken Scaled Armor', 'Dricken scaled armor', 'dricken scaled armor'
}
duskhunterstunic = {
    'Dusk Hunters Tunic', 'Dusk hunters tunic', 'dusk hunters tunic' 
}
dwarvenforemanarmor = {
    'Dwarven Foreman Armor', 'Dwarven foreman armor', 'dwarven foreman armor' 
}
dwarvenminerarmor = {
    'Dwarven Miner Armor', 'Dwarven miner armor', 'dwarven miner armor'
}
ebontalonarmor = {
    'Ebon Talon Armor', 'Ebon talon armor', 'ebon talon armor'
}
elitedragonchampionarmor = {
    'Elite Dragon Champion Armor', 'Elite dragon champion armor', 'elite dragon champion armor'
}
elvenguardarmor = {
    'Elvenguard Armor', 'Elvenguard armor', 'elvenguard armor' 
}
eternalchronomancerarmor = {
    'Eternal Chronomancer Armor', 'Eternal chronomancer armor', 'eternal chronomancer armor' 
}
firemagerobe = {
    'Fire Mage Robe', 'Fire mage robe', 'fire mage robe'
}
firerogueoutfit = {
    'Fire Rogue Outfit', 'Fire rogue outfit', 'fire rogue outftit'
}
foresttunic = {
    'Forest Tunic', 'Forest tunic', 'forest tunic'
}
dragonstalkergoldtabard = {
    'Dragon Stalker Gold Tabard', 'Dragon stalker gold tabard', 'dragon stalker gold tabard'
}
 
@bot.command()
async def item(*, message: str):
    if message in chronomancer_armor:
        embed = discord.Embed(title="Chronomancer Armor", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/d1KVnH/a_PQt3ht_1.png")
        embed.add_field(name="Price", value="2017 calendar")
        embed.add_field(name="Sellback", value="0 gold")
        embed.add_field(name="Level", value="1")
        embed.add_field(name="Health Stats", value="+47")
        embed.add_field(name="Attack Stats", value="+24")
        embed.add_field(name="Armor Stats", value="+39")
        embed.add_field(name="Evasion Stats", value="+19")
        embed.add_field(name="Crit Stats", value="+15")
        embed.add_field(name="Found on: ", value="2017 Calendar Shop - Yulgar's Inn")
        await bot.say(embed=embed)
    elif message in alpha_knight_armor:
        embed = discord.Embed(title="Alpha Knight Armor", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/gMcF4H/MflPmCe.png")
        embed.add_field(name="Price", value="2 gold")
        embed.add_field(name="Level", value="1")
        embed.add_field(name="Found on: ", value="Melodia's Shop, Founders Sanctuary")
        await bot.say(embed=embed)
        
    elif message in blood_knight_armor:
        embed = discord.Embed(title="Bloodknight Armor", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/bxb67H/Blood_Knight_Armor_MF_1.png")
        embed.add_field(name="Price", value="Drop, Shrade Minions")
        embed.add_field(name="Sellback", value="1 gold")
        embed.add_field(name="Level", value="5")
        embed.add_field(name="Health Stats", value="+67")
        embed.add_field(name="Attack Stats", value="+21")
        embed.add_field(name="Armor Stats", value="+48")
        embed.add_field(name="Evasion Stats", value="+16")
        embed.add_field(name="Crit Stats", value="+24")
        embed.add_field(name="Found on: ", value="Camp Gonnagetcha")
        await bot.say(embed=embed)
    elif message in campy_rogue:
        embed = discord.Embed(title="Campy Rogue", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/jVVHzx/Dp_K7_Xa_D_1.png")
        embed.add_field(name="Price", value="Craftable, Craft Badge x50, 500 gold")
        embed.add_field(name="Sellback", value="10 gold")
        embed.add_field(name="Level", value="1")
        embed.add_field(name="Health Stats", value="N/A")
        embed.add_field(name="Attack Stats", value="N/A")
        embed.add_field(name="Armor Stats", value="N/A")
        embed.add_field(name="Evasion Stats", value="N/A")
        embed.add_field(name="Crit Stats", value="N/A")
        embed.add_field(name="Found on: ", value="Dricken Uniforms - Camp Gonnagetcha")
        await bot.say(embed=embed)
    elif message in campy_warrior:
        embed = discord.Embed(title="Campy Warrior", color=0x00a0ea)
        embed.add_field(name="Price", value="Craftable, Craft Badge x50, 500 gold")
        embed.add_field(name="Sellback", value="10 gold")
        embed.add_field(name="Level", value="1")
        embed.add_field(name="Health Stats", value="N/A")
        embed.add_field(name="Attack Stats", value="N/A")
        embed.add_field(name="Armor Stats", value="N/A")
        embed.add_field(name="Evasion Stats", value="N/A")
        embed.add_field(name="Crit Stats", value="N/A")
        embed.add_field(name="Found on: ", value="Frogzard Uniforms - Camp Gonnagetcha")
        await bot.say(embed=embed)
        await bot.say("Image unavailable :anger:")
    elif message in chewed_mystic_robes:
        embed = discord.Embed(title="Chewed Mystic Robes", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/cMO4ex/Fmymv7v_1.png")
        embed.add_field(name="Price", value="Dropped by Mystic Bones")
        embed.add_field(name="Sellback", value="10 gold")
        embed.add_field(name="Level", value="4")
        embed.add_field(name="Health Stats", value="+58")
        embed.add_field(name="Attack Stats", value="+26")
        embed.add_field(name="Armor Stats", value="+44")
        embed.add_field(name="Evasion Stats", value="+20")
        embed.add_field(name="Crit Stats", value="+20")
        embed.add_field(name="Found on: ", value="Mystics Cave")
        await bot.say(embed=embed)
    elif message in chewed_warrior_armor:
        embed = discord.Embed(title="Chewed Warrior Armor ", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/eNtjCH/9_WHLh_TD_1.png")
        embed.add_field(name="Price", value="Dropped by Direwolf, Forest wolf, Lycan Guard, Lycan Prowler, Umbral wolf, Warwolf, Warwolf Chieftain")
        embed.add_field(name="Sellback", value="10 gold")
        embed.add_field(name="Level", value="18")
        embed.add_field(name="Health Stats", value="+193")
        embed.add_field(name="Attack Stats", value="+58")
        embed.add_field(name="Armor Stats", value="+149")
        embed.add_field(name="Evasion Stats", value="+44")
        embed.add_field(name="Crit Stats", value="+58")
        embed.add_field(name="Found on: ", value="Darkovia Forest, Deepclaw Caverns, Dimgrove")
        await bot.say(embed=embed)
    elif message in chiropteran_armor:
        embed = discord.Embed(title="Chiropteran Armor", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/fFw7zx/t_HNKy_ZY_1.png")
        embed.add_field(name="Price", value="Dropped by Ancient Evil (in darkhurt only)")
        embed.add_field(name="Sellback", value="10 gold")
        embed.add_field(name="Level", value="18")
        embed.add_field(name="Health Stats", value="+175")
        embed.add_field(name="Attack Stats", value="+87")
        embed.add_field(name="Armor Stats", value="+127")
        embed.add_field(name="Evasion Stats", value="+74")
        embed.add_field(name="Crit Stats", value="+61")
        embed.add_field(name="Found on: ", value="Darkhurst Town")
        await bot.say(embed=embed)
    elif message in clawed_rogue_outfit:
        embed = discord.Embed(title="Clawed Rogue Outfit", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/gfurux/PFj25_Tw_1.png")
        embed.add_field(name="Price", value="Dropped by Cave Ghoul, Ghoul Minion")
        embed.add_field(name="Sellback", value="10 gold")
        embed.add_field(name="Level", value="18")
        embed.add_field(name="Health Stats", value="+147")
        embed.add_field(name="Attack Stats", value="+77")
        embed.add_field(name="Armor Stats", value="+133")
        embed.add_field(name="Evasion Stats", value="+57")
        embed.add_field(name="Crit Stats", value="+62")
        embed.add_field(name="Found on: ", value="Darkovia Forest, Shadowsong Crypt")
        await bot.say(embed=embed)
    elif message in commondarkovianclothes:
        embed = discord.Embed(title="Common Darkovian Clothes", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/hmdHZx/QAk7urn_1.png")
        embed.add_field(name="Price", value="Dropped by Lord Anemis, Vampire Knight, Werewolf")
        embed.add_field(name="Sellback", value="10 gold")
        embed.add_field(name="Level", value="18")
        embed.add_field(name="Health Stats", value="+181")
        embed.add_field(name="Attack Stats", value="+70")
        embed.add_field(name="Armor Stats", value="+126")
        embed.add_field(name="Evasion Stats", value="+65")
        embed.add_field(name="Crit Stats", value="+59")
        embed.add_field(name="Found on: ", value="Darkhurst Town")
        await bot.say(embed=embed)
    elif message in commondarkoviandress:
        embed = discord.Embed(title="Common Darkovian Dress", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/iaLEEx/p63t1_V0_1.png")
        embed.add_field(name="Price", value="Dropped by Lord Anemis, Vampire Knight, Werewolf")
        embed.add_field(name="Sellback", value="10 gold")
        embed.add_field(name="Level", value="18")
        embed.add_field(name="Health Stats", value="+173")
        embed.add_field(name="Attack Stats", value="+77")
        embed.add_field(name="Armor Stats", value="+135")
        embed.add_field(name="Evasion Stats", value="+58")
        embed.add_field(name="Crit Stats", value="+58")
        embed.add_field(name="Found on: ", value="Darkhurst Town")
        await bot.say(embed=embed)
    elif message in crimsonbattlemagerobe:
        embed = discord.Embed(title="Crimson Battle Mage Robe ", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/ezqxZx/VUU6w_SJ_1.png")
        embed.add_field(name="Price", value="Craftable, Lava Core x2, Molten Ingot x1, Flame Runed Cloth x10, 2,000 Gold")
        embed.add_field(name="Sellback", value="25 gold")
        embed.add_field(name="Level", value="16")
        embed.add_field(name="Health Stats", value="+159")
        embed.add_field(name="Attack Stats", value="+63")
        embed.add_field(name="Armor Stats", value="+107")
        embed.add_field(name="Evasion Stats", value="+60")
        embed.add_field(name="Crit Stats", value="+55")
        embed.add_field(name="Found on: ", value=" Crimson Battle Mage Craft Shop - DragonSlayer Camp")
        await bot.say(embed=embed)
    elif message in crimsonmagerobes:
        embed = discord.Embed(title="Crimson Mage Robes ", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/fYGknH/Mk3_Gcro_1.png")
        embed.add_field(name="Price", value="Craftable, 100 Dragon Crystals, Burnt Cloth x10, Glowing Coals x5, Evil Tear x1, 300 gold")
        embed.add_field(name="Sellback", value="10 gold")
        embed.add_field(name="Level", value="6")
        embed.add_field(name="Health Stats", value="+68")
        embed.add_field(name="Attack Stats", value="+31")
        embed.add_field(name="Armor Stats", value="+50")
        embed.add_field(name="Evasion Stats", value="+21")
        embed.add_field(name="Crit Stats", value="+29")
        embed.add_field(name="Found on: ", value=" Balis' Craft Shop - Heartwood Forest")
        await bot.say(embed=embed)
    elif message in crustyinnkeepersclothes:
        embed = discord.Embed(title="Crusty Innkeeper's Clothes", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/hx0pEx/90w1w_MH_1.png")
        embed.add_field(name="Price", value="Dropped by Boogerling, Slime Lord")
        embed.add_field(name="Sellback", value="10 gold")
        embed.add_field(name="Level", value="11")
        embed.add_field(name="Health Stats", value="+99")
        embed.add_field(name="Attack Stats", value="+49")
        embed.add_field(name="Armor Stats", value="+75")
        embed.add_field(name="Evasion Stats", value="+32")
        embed.add_field(name="Crit Stats", value="+41")
        embed.add_field(name="Found on: ", value="Yulgar's Sinkhole")
        await bot.say(embed=embed)
    elif message in darkdefenderarmor:
        embed = discord.Embed(title="Dark Defender Armor", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/nyABSH/WRfxz_RK_1.png")
        embed.add_field(name="Price", value="Craftable, Defender Medal x200, Elite Defender Medals x5, 200 Gold")
        embed.add_field(name="Sellback", value="20 gold")
        embed.add_field(name="Level", value="1")
        embed.add_field(name="Health Stats", value="N/A")
        embed.add_field(name="Attack Stats", value="N/A")
        embed.add_field(name="Armor Stats", value="N/A")
        embed.add_field(name="Evasion Stats", value="N/A")
        embed.add_field(name="Crit Stats", value="N/A")
        embed.add_field(name="Found on: ", value=" Dark Defender Crafting - Battleon")
        await bot.say(embed=embed)
    elif message in davidscoat:
        embed = discord.Embed(title="David's Coat", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/e0CNmc/TAGPpc_R_1.png")
        embed.add_field(name="Price", value="Dropped by David")
        embed.add_field(name="Sellback", value="0 gold")
        embed.add_field(name="Level", value="18")
        embed.add_field(name="Health Stats", value="+196")
        embed.add_field(name="Attack Stats", value="+87")
        embed.add_field(name="Armor Stats", value="+152")
        embed.add_field(name="Evasion Stats", value="+66")
        embed.add_field(name="Crit Stats", value="+66")
        embed.add_field(name="Found on: ", value="Shadowsong Crypt")
        await bot.say(embed=embed)
    elif message in defenderguardianarmor:
        embed = discord.Embed(title="Defender Gaurdian Armor", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/dybwex/n_MF7z_Lp_1.png")
        embed.add_field(name="Price", value="Craftable, Defender Medal x25, Gaurdian Defender Medal x1, 30 gold")
        embed.add_field(name="Sellback", value="12 gold")
        embed.add_field(name="Level", value="1")
        embed.add_field(name="Health Stats", value="N/A")
        embed.add_field(name="Attack Stats", value="N/A")
        embed.add_field(name="Armor Stats", value="N/A")
        embed.add_field(name="Evasion Stats", value="N/A")
        embed.add_field(name="Crit Stats", value="N/A")
        embed.add_field(name="Found on: ", value="Defender Armor Craft Shop - Battleon")
        await bot.say(embed=embed)
    elif message in defenderknightarmor:
        embed = discord.Embed(title="Defender Knight Armor", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/kunE1c/X4d_Qf6m_1.png")
        embed.add_field(name="Price", value="Craftable, Defender Medal x25, 30 gold")
        embed.add_field(name="Sellback", value="12 gold")
        embed.add_field(name="Level", value="1")
        embed.add_field(name="Health Stats", value="N/A")
        embed.add_field(name="Attack Stats", value="N/A")
        embed.add_field(name="Armor Stats", value="N/A")
        embed.add_field(name="Evasion Stats", value="N/A")
        embed.add_field(name="Crit Stats", value="N/A")
        embed.add_field(name="Found on: ", value="Defender Armor Craft Shop - Battleon")
        await bot.say(embed=embed)
    elif message in defendermagerobes:
        embed = discord.Embed(title="Defender Mage Robes", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/n3707H/M06_Q2_Ml_1.png")
        embed.add_field(name="Price", value="Craftable, Defender Medal x25, 30 gold")
        embed.add_field(name="Sellback", value="12 gold")
        embed.add_field(name="Level", value="1")
        embed.add_field(name="Health Stats", value="N/A")
        embed.add_field(name="Attack Stats", value="N/A")
        embed.add_field(name="Armor Stats", value="N/A")
        embed.add_field(name="Evasion Stats", value="N/A")
        embed.add_field(name="Crit Stats", value="N/A")
        embed.add_field(name="Found on: ", value="Defender Armor Craft Shop - Battleon")
        await bot.say(embed=embed)
    elif message in defenderroguearmor:
        embed = discord.Embed(title="Defender Rogue Armor", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/doBhMc/u_VFw_P7_U_1.png")
        embed.add_field(name="Price", value="Craftable, Defender Medal x25, 30 gold")
        embed.add_field(name="Sellback", value="12 gold")
        embed.add_field(name="Level", value="1")
        embed.add_field(name="Health Stats", value="N/A")
        embed.add_field(name="Attack Stats", value="N/A")
        embed.add_field(name="Armor Stats", value="N/A")
        embed.add_field(name="Evasion Stats", value="N/A")
        embed.add_field(name="Crit Stats", value="N/A")
        embed.add_field(name="Found on: ", value="Defender Armor Craft Shop - Battleon")
        await bot.say(embed=embed) 
    elif message in dragonberserkerarmor:
        embed = discord.Embed(title="Dragon Berserker Armor", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/btkEZx/qdk_Nr_Qn_1.png")
        embed.add_field(name="Price", value="Craftable, Dragon Trophy x3, Scale Slayer Armor, 5,000 gold")
        embed.add_field(name="Sellback", value="10 gold")
        embed.add_field(name="Level", value="20")
        embed.add_field(name="Health Stats", value="+232")
        embed.add_field(name="Attack Stats", value="+145")
        embed.add_field(name="Armor Stats", value="+203")
        embed.add_field(name="Evasion Stats", value="+87")
        embed.add_field(name="Crit Stats", value="+87")
        embed.add_field(name="Found on: ", value="Dragon Berserker - Mount Ashfall Camp")
        await bot.say(embed=embed)
    elif message in dragonchampionarmor:
        embed = discord.Embed(title="Dragon Champion Armor", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/jKKmgc/VC0m25j_1.png")
        embed.add_field(name="Price", value="Craftable, Dragon Trophy x4, Obsidian Ingot x20, 30 gold")
        embed.add_field(name="Sellback", value="10 gold")
        embed.add_field(name="Level", value="20")
        embed.add_field(name="Health Stats", value="+231")
        embed.add_field(name="Attack Stats", value="+103")
        embed.add_field(name="Armor Stats", value="+179")
        embed.add_field(name="Evasion Stats", value="+77")
        embed.add_field(name="Crit Stats", value="+77")
        embed.add_field(name="Found on: ", value="Dragon Champion - Mount Ashfall Camp")
        await bot.say(embed=embed)
    elif message in dragonstalkerflametabard:
        embed = discord.Embed(title="Dragon Stalker Flame Tabard", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/gR6hMc/Zr_IQq_Z2_1.png")
        embed.add_field(name="Price", value="Craftable, Obsidian Ingot x10, Flame Essence x1, Thick Drakimp Fur x10, 4,000 gold")
        embed.add_field(name="Sellback", value="0 gold")
        embed.add_field(name="Level", value="16")
        embed.add_field(name="Health Stats", value="+169")  
        embed.add_field(name="Attack Stats", value="+53")
        embed.add_field(name="Armor Stats", value="+118")
        embed.add_field(name="Evasion Stats", value="+60")
        embed.add_field(name="Crit Stats", value="+44")
        embed.add_field(name="Found on: ", value="Dragon Stalker Craft Shop - DragonSlayer Camp")
        await bot.say(embed=embed)
    elif message in dragonstalkergoldtabard:
        embed = discord.Embed(title="Dragon Stalker Gold Tabard", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/kepf7H/EGqcu_Ia_1.png")
        embed.add_field(name="Price", value="Craftable, Obsidian Ingot x10, Flame Essence x1, Thick Drakimp Fur x10, 4,000 gold")
        embed.add_field(name="Sellback", value="0 gold")
        embed.add_field(name="Level", value="15")
        embed.add_field(name="Health Stats", value="+144")
        embed.add_field(name="Attack Stats", value="+78")
        embed.add_field(name="Armor Stats", value="+108")
        embed.add_field(name="Evasion Stats", value="+54")
        embed.add_field(name="Crit Stats", value="+61")
        embed.add_field(name="Found on: ", value="Dragon Stalker Craft Shop - DragonSlayer Camp")
        await bot.say(embed=embed)
    elif message in dragonstalkerskytabard:
        embed = discord.Embed(title="Dragon Stalker Sky Tabard", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/gmBJSH/Dag6f9b_1.png")
        embed.add_field(name="Price", value="Craftable, Obsidian Ingot x10, Flame Essence x1, Thick Drakimp Fur x10, 4,000 gold")
        embed.add_field(name="Sellback", value="0 gold")
        embed.add_field(name="Level", value="16")
        embed.add_field(name="Health Stats", value="+133")
        embed.add_field(name="Attack Stats", value="+55")
        embed.add_field(name="Armor Stats", value="+117")
        embed.add_field(name="Evasion Stats", value="+50")
        embed.add_field(name="Crit Stats", value="+47")
        embed.add_field(name="Found on: ", value="Dragon Stalker Craft Shop - DragonSlayer Camp")
        await bot.say(embed=embed)
    elif message in dragonslayerarmor:
        embed = discord.Embed(title="DragonSlayer Armor", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/h1v9HH/j_SVU0_DH_1.png")
        embed.add_field(name="Price", value="Reward from the DragonSlayer Equipment Quests")
        embed.add_field(name="Sellback", value="0 gold")
        embed.add_field(name="Level", value="1")
        embed.add_field(name="Health Stats", value="N/A")
        embed.add_field(name="Attack Stats", value="N/A")
        embed.add_field(name="Armor Stats", value="N/A")
        embed.add_field(name="Evasion Stats", value="N/A")
        embed.add_field(name="Crit Stats", value="N/A")
        embed.add_field(name="Found on: ", value="DragonSlayer Equipment - Mount Ashfall Camp")
        await bot.say(embed=embed)
    elif message in drakehunterflametabard:
        embed = discord.Embed(title="Drake Hunter Flame Tabard", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/gqbVrc/Bea_BWI1_1.png")
        embed.add_field(name="Price", value="200 Dragon Crystals, Craftable, Lava Hide x15, Obsidian x10, 4,000 gold ")
        embed.add_field(name="Sellback", value="20 gold")
        embed.add_field(name="Level", value="15")
        embed.add_field(name="Health Stats", value="+136")
        embed.add_field(name="Attack Stats", value="+69")
        embed.add_field(name="Armor Stats", value="+111")
        embed.add_field(name="Evasion Stats", value="+53")
        embed.add_field(name="Crit Stats", value="+42")
        embed.add_field(name="Found on: ", value="Drake Hunter Craft Shop - DragonSlayer Camp, Senna's Craft Shop - DragonSlayer Camp ")
        await bot.say(embed=embed)
    elif message in drakehuntergoldtabard:
        embed = discord.Embed(title="Drake Hunter Gold Tabard", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/hNbS4x/pqg_A0_W6_1.png")
        embed.add_field(name="Price", value="200 Dragon Crystals, Craftable, Lava Hide x15, Obsidian x10, 4,000 gold ")
        embed.add_field(name="Sellback", value="20 gold")
        embed.add_field(name="Level", value="15")
        embed.add_field(name="Health Stats", value="+149")
        embed.add_field(name="Attack Stats", value="+61")
        embed.add_field(name="Armor Stats", value="+110")
        embed.add_field(name="Evasion Stats", value="+59")
        embed.add_field(name="Crit Stats", value="+36")
        embed.add_field(name="Found on: ", value="Drake Hunter Craft Shop - DragonSlayer Camp, Senna's Craft Shop - DragonSlayer Camp ")
        await bot.say(embed=embed)
    elif message in drakehunterskytabard:
        embed = discord.Embed(title="Drake Hunter Sky Tabard", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/iCvRxH/s_VRf_EVx_1.png")
        embed.add_field(name="Price", value="200 Dragon Crystals, Craftable, Lava Hide x15, Obsidian x10, 4,000 gold ")
        embed.add_field(name="Sellback", value="20 gold")
        embed.add_field(name="Level", value="15")
        embed.add_field(name="Health Stats", value="+138")
        embed.add_field(name="Attack Stats", value="+66")
        embed.add_field(name="Armor Stats", value="+101")
        embed.add_field(name="Evasion Stats", value="+51")
        embed.add_field(name="Crit Stats", value="+52")
        embed.add_field(name="Found on: ", value="Drake Hunter Craft Shop - DragonSlayer Camp, Senna's Craft Shop - DragonSlayer Camp ")
        await bot.say(embed=embed)
    elif message in dreadhoodarmor:
        embed = discord.Embed(title="Dread Hood Armor", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/mnBDBc/Ch0_JXF5_1.png")
        embed.add_field(name="Price", value="Craftable, Darkovia Creature Sample x40, 2,000 gold ")
        embed.add_field(name="Sellback", value="10 gold")
        embed.add_field(name="Level", value="18")
        embed.add_field(name="Health Stats", value="+161")
        embed.add_field(name="Attack Stats", value="+101")
        embed.add_field(name="Armor Stats", value="+137")
        embed.add_field(name="Evasion Stats", value="+51")
        embed.add_field(name="Crit Stats", value="+74")
        embed.add_field(name="Found on: ", value=" Darkovia Forest Crafts - Darkovia Forest")
        await bot.say(embed=embed)
    elif message in drickenfeatheredrobe:
        embed = discord.Embed(title="Dricken Feathered Robe", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/cH1Qe7/3_Zi_Hc_NJ_1.png")
        embed.add_field(name="Price", value="Dropped by Mother Hen")
        embed.add_field(name="Sellback", value="1 gold")
        embed.add_field(name="Level", value="1")
        embed.add_field(name="Health Stats", value="N/A")
        embed.add_field(name="Attack Stats", value="N/A")
        embed.add_field(name="Armor Stats", value="N/A")
        embed.add_field(name="Evasion Stats", value="N/A")
        embed.add_field(name="Crit Stats", value="N/A")
        embed.add_field(name="Found on: ", value="Dricken Cave")
        await bot.say(embed=embed)
    elif message in drickenscaledarmor:
        embed = discord.Embed(title="Dricken Scaled Armor", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/jH0U6n/Vn_INQFK_1.png")
        embed.add_field(name="Price", value="300 Dragon Crystals")
        embed.add_field(name="Sellback", value="30 gold")
        embed.add_field(name="Level", value="1")
        embed.add_field(name="Health Stats", value="N/A")
        embed.add_field(name="Attack Stats", value="N/A")
        embed.add_field(name="Armor Stats", value="N/A")
        embed.add_field(name="Evasion Stats", value="N/A")
        embed.add_field(name="Crit Stats", value="N/A")
        embed.add_field(name="Found on: ", value="Feathered Shop - Dricken Cave")
        await bot.say(embed=embed)
    elif message in duskhunterstunic:
        embed = discord.Embed(title="Dust Hunter's Tunic", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/m2B8z7/GZuu_Zp_D_1.png")
        embed.add_field(name="Price", value="9 gold")
        embed.add_field(name="Sellback", value="1 gold")
        embed.add_field(name="Level", value="2")
        embed.add_field(name="Health Stats", value="+48")
        embed.add_field(name="Attack Stats", value="+21")
        embed.add_field(name="Armor Stats", value="+34")
        embed.add_field(name="Evasion Stats", value="+17")
        embed.add_field(name="Crit Stats", value="+18")
        embed.add_field(name="Found on: ", value="Robina's Shop - Greenguard")
        await bot.say(embed=embed)
    elif message in dwarvenforemanarmor:
        embed = discord.Embed(title="Dwarven Foreman Armor", color=0x00a0ea)
        embed.set_image(url="https://image.ibb.co/jU8oz7/1_Wb_UVx7_1.png")
        embed.add_field(name="Price", value="Craftable, Lava Core 1x, Dwarven Miner Armor 1x, Dwarven Iron Ingot 5x, 3,000 gold")
        embed.add_field(name="Sellback", value="25 gold")
        embed.add_field(name="Level", value="16")
        embed.add_field(name="Health Stats", value="+144")
        embed.add_field(name="Attack Stats", value="+78")
        embed.add_field(name="Armor Stats", value="+177")
        embed.add_field(name="Evasion Stats", value="+43")
        embed.add_field(name="Crit Stats", value="+62")
        embed.add_field(name="Found on: ", value="Dwarven Crafts - Magma Mines")
        await bot.say(embed=embed)
    else:
        await bot.say("Fatal Error! :anger:Please re-try or check your grammar, if problem persists contact bot owner.")
@bot.command()
async def instructions():
    await bot.say("Type wiki.\"category\" for a list of all items listed on the category")
    await bot.say("For a list of categories use wiki.categories.")
    await bot.say("Type wiki.item \"item name\" to search for an item")
@bot.command()
async def categories():
    embed = discord.Embed(title="Categories", color=0x00a0ea)
    embed.set_image(url="https://thumb.ibb.co/hheFjx/indice.png")
    embed.add_field(name="=======", value="\"helms\", \"shoulders\", \"armors\", \"boots\", \"gloves\", \"belts\", \"capes\"")
    await bot.say(embed=embed)

@bot.command()
async def echo(*, msg: str):
    await bot.say(msg)
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
shop_items = {
     "Alpha Knight Armor", "Alpha knight armor", "alpha knight armor"
 }



       

   
alphaknightboots = {
    'Alpha Knight Boots', 'Alpha knight boots', 'alpha knight boots'
}

alphapirateboots = {
    'Alpha Pirate Boots', 'Alpha pirate boots', 'alpha pirate boots'
}
ancientevilboots = {
    'Ancient Evil Boots', 'Ancient evil boots', 'ancient evil boots'
}
ashbrandboots = {
    'Ashbrand Boots', 'Ashbrand boots', 'ashbrand boots'
}
ashenplateboots = {
    'Ashen Plate Boots', 'Ashen plate boots', 'ashen plate boots'
}
battleonmilitiaboots = {
    'Battleon Militia Boots', 'Battleon militia boots', 'battleon militia boots'
}
betaberserkerboots = {
    'Beta Berserker Boots', 'Beta berserker boots', 'beta berserker boots'
}
bloodknightboots = {
    'BloodKnight Boots', 'Bloodknight boots', 'bloodknight boots'
}
campyboots = {
    'Campy Boots', 'Campy boots', 'campy boots'
}
chewedzardscaleboots = {
    'Chewed Zardscale Boots', 'Chewed zardscale boots', 'chewed zardscale boots'
}
chiropteranboots = {
    'Chiropteran Boots', 'Chiropteran boots', 'chiropteran boots'
}
chronomancerboots = {
    'Chronomancer Boots', 'Chronomancer boots', 'chronomancer boots'
}
crimsonbattlemageboots = {
    'Crimson Battle Mage Boots', 'Crimson battle mage boots', 'crimson battle mage boots'
}
darkdefenderboots = {
    'Dark Defender Boots', 'Dark defender boots', 'dark defender boots'
}
darkleatherboots = {
    'Dark Leather Boots', 'Dark leather boots', 'dark leather boots'
}
defenderknightboots = {
    'Defender Knight Boots', 'Defender knight boots', 'defender knight boots'
}
defendermageboots = {
    'Defender Mage Boots', 'Defender mage boots', 'defender mage boots'
}
defenderrogueboots = {
    'Defender Rogue Boots', 'Defender rogue boots', 'defender rogue boots'
}
dragonberserkerboots = {
    'Dragon Berserker Boots', 'Dragon berserker boots', 'dragon berserker boots'
}
dragonchampiongreaves = {
    'Dragon Champion Greaves', 'Dragon champion greaves', 'dragon champion greaves'
}
dragonstalkerboots = {
    'Dragon Stalker Boots', 'Dragon stalker boots', 'dragon stalker boots'
}
dragonslayerboots = {
    'DragonSlayer Boots', 'Dragonslayer boots', 'dragonslayer boots'
}
drakehunterboots = {
    'Drake Hunter Boots', 'Drake hunter boots', 'drake hunter boots'
}
dreadhoodboots = {
    'Dread Hood Boots', 'Dread hood boots', 'dread hood boots'
}
drickenarmoredboots = {
    'Dricken Armored Boots', 'Dricken armored boots', 'dricken armored boots'
}
drickenleatherfeet = {
    'Dricken Leather Feet', 'Dricken leather feet', 'dricken leather feet'
}
dwarvenforemanboots = {
    'Dwarven Foreman Boots', 'Dwarven foreman boots', 'dwarven foreman boots'
}
dwarvenminerboots = {
    'Dwarven Miner Boots', 'Dwarven miner boots', 'dwarven miner boots'
}
ebontalongreaves = {
    'Ebon Talon Greaves', 'Ebon talon greaves', 'ebon talon greaves'
}
elitedragonchampiongreaves = {
    'Elite Dragon Champion Greaves', 'Elite dragon champion greaves', 'elite dragon champion greaves'
}
elvenguardboots = {
    'Elvenguard Boots', 'Elvenguard boots', 'elvenguard boots'
}
eternalchronomancerboots = {
    'Eternal Chronomancer Boots', 'Eternal chronomancer boots', 'eternal chronomancer boots'
}
firemageboots = {
    'Fire Mage Boots', 'Fire mage boots', 'fire mage boots'
}
firerogueboots = {
    'Fire Rogue Boots', 'Fire rogue boots', 'fire rogue boots'
}
frostdefenderboots = {
    'Frost Defender Boots', 'Frost defender boots', 'frost defender boots'
}
frostlornmageboots = {
    'Frostlorn Mage Boots', 'Frostlorn mage boots', 'frostlorn mage boots'
}
frostlornrogueboots = {
    'Frostlorn Rogue Boots', 'Frostlorn rogue boots', 'frostlorn rogue boots'
}
frostlornwarriorboots = {
    'Frostlorn Warrior Boots', 'Frostlorn warrior boots', 'frostlorn warrior boots'
}
frostvalelfboots = {
    'Frostval Elf Boots', 'Frostval elf boots', 'frostval elf boots'
}
furnaceknightboots = {
    'Furnace Knight Boots', 'Furnace knight boots', 'furnace knight boots'
}
goldenboots = {
    'Golden Boots', 'Golden boots', 'golden boots'
}
grampysleatherboots = {
    'Grampy\'s Leather Boots', 'Grampy\'s leather boots', 'grampy\'s leather boots'
}
guardianboots = {
    'Guardian Boots', 'Guardian boots', 'guardian boots'
}
guardiandragonboots = {
    'Guardian Dragon Boots', 'Guardian dragon boots', 'guardian dragon boots'
}
holeywitchshoes = {
    'Holey Witch Shoes', 'Holey witch shoes', 'holey witch shoes'
}
invisibleboots = {
    'Invisible Boots', 'Invisible boots', 'invisible boots'
}
ironberserkerboots = {
    'Iron Berserker Boots', 'Iron berserker boots', 'iron berserker boots'
}
keenalphapirateboots = {
    'Keen Alpha Pirate Boots', 'Keen alpha pirate boots', 'keen alpha pirate boots'
}
kickstarterguardianboots = {
    'KickStarter Guardian Boots', 'Kickstarter guardian boots', 'kickstarter guardian boots'
}
leatherboots = {
    'Leather Boots', 'Leather boots', 'leather boots'
}
leatherpirateboots = {
    'Leather Pirate Boots', 'Leather pirate boots', 'leather pirate boots'
}
legiongruntboots = {
    'Legion Grunt Boots', 'Legion grunt boots', 'legion grunt boots'
}
legionzealotboots = {
    'Legion Zealot Boots', 'Legion zealot boots', 'legion zealot boots'
}
mageshoes = {
    'Mage Shoes', 'Mage shoes', 'mage shoes'
}
magmarranboots = {
    'Magmarran Boots', 'Magmarran boots', 'magmarran boots'
}
navalcommanderboots = {
    'Naval Commander Boots', 'Naval commander boots', 'naval commander boots'
}
nightguardboots = {
    'Night Guard Boots', 'Night guard boots', 'night guard boots'
}
noblesboots = {
    'Noble\'s Boots', 'Noble\'s boots', 'noble\'s boots'
}
orokuboots = {
    'Oroku Boots', 'Oroku boots', 'oroku boots'
}
pebblarshellboots = {
    'Pebblar Shell Boots', 'Pebblar shell boots', 'pebblar shell boots'
}
phoenixknightboots = {
    'Phoenix Knight Boots', 'Phoenix knight boots', 'phoenix knight boots'
}
plutocratboots = {
    'Plutocrat Boots', 'Plutocrat boots', 'plutocrat boots'
}
pumpkinlordboots = {
    'Pumpkin Lord Boots', 'Pumpkin lord boots', 'pumpkin lord boots'
}
pumpkinmancerboots = {
    'Pumpkinmancer Boots', 'Pumpkinmancer boots', 'pumpkinmancer boots'
}
redelfboots = {
    'Red Elf Boots', 'Red elf boots', 'red elf boots'
}
redeyeboots = {
    'Red-Eye Boots', 'Red-eye boots', 'red-eye boots'
}
runedelvenguardboots = {
    'Runed Elvenguard Boots', 'Runed elvenguard boots', 'runed elvenguard boots'
}
santaboots = {
    'Santa Boots', 'Santa boots', 'santa boots'
}
scaleslayergreaves = {
    'Scale Slayer Greaves', 'Scale slayer greaves', 'scale slayer greaves'
}
scoundrelboots = {
    'Scoundrel Boots', 'Scoundrel boots', 'scoundrel boots'
}
serpentfighterboots = {
    'Serpent Fighter Boots', 'Serpent fighter boots', 'serpent fighter boots'
}
shadowleatherboots = {
    'Shadow Leather Boots', 'Shadow leather boots', 'shadow leather boots'
}
shadowedbloodboots = {
    'Shadowed Blood Boots', 'Shadowed blood boots', 'shadowed blood boots'
}
shadowedboots = {
    'Shadowed Boots', 'Shadowed boots', 'shadowed boots'
}
shadowedplateboots = {
    'Shadowed Plate Boots', 'Shadowed plate boots', 'shadowed plate boots'
}
shadowslayeresboots = {
    'ShadowSlayer E\'s Boots', 'Shadowslayer E\'s boots', 'shadowslayer E\'s boots'
}
shadowslayerrsboots = {
    'ShadowSlayer R\'s Boots', 'Shadowslayer R\'s boots', 'shadowslayer R\'s boots'
}
shradesboots = {
    'Shrade\'s Boots', 'Shrade\'s boots', 'shrade\'s boots'
}
soothsayerboots = {
    'SoothSayer Boots', 'Soothsayer boots', 'soothsayer boots'
}
spiritualwarriorboots = {
    'Spiritual Warrior Boots', 'Spiritual warrior boots', 'spiritual warrior boots'
}
spookywitchshoes = {
    'Spooky Witch Boots', 'Spooky witch boots', 'spooky witch boots'
}
sturdyleatherboots = {
    'Sturdy Leather Boots', 'Sturdy leather boots', 'sturdy leather boots'
}
talynsboots = {
    'Talyn\'s Boots', 'Talyn\'s boots', 'talyn\'s boots'
}
trolluksteinboots = {
    'Trollukstein Boots', 'Trollukstein boots', 'trollukstein boots'
}
twilightwolfboots = {
    'Twilight Wolf Boots', 'Twilight wolf boots', 'twilight wolf boots'
}
unboundboots = {
    'Unbound Boots', 'Unbound boots', 'unbound boots'
}
unboundvampboots = {
    'Unbound Vamp Boots', 'Unbound vamp boots', 'unbound vamp boots'
}
undeadvindicatorboots = {
    'Undead Vindicator Boots', 'Undead vindicator boots', 'undead vindicator boots'
}
undeadwarriorboots = {
    'Undead Warrior Boots', 'Undead warrior boots', 'undead warrior boots'
}
underguardianboots = {
    'Under Guardian Boots', 'Under guardian boots', 'under guardian boots'
}
vostsboots = {
    'Vost\'s Boots', 'Vost\'s boots', 'vost\'s boots'
}
warriorboots = {
    'Warrior Boots', 'Warrior boots', 'warrior boots'
}
witchshoes = {
    'Witch Shoes', 'Witch shoes', 'witch shoes'
}
wolfskinboots = {
    'Wolfskin Boots', 'Wolfskin boots', 'wolfskin boots'
}
zardscaleboots = {
    'Zardscale Boots', 'Zardscale boots', 'zardscale boots'
}

letter_a_boots = ["Alpha Knight Boots", "Alpha Pirate Boots", "Ancient Evil Boots", "Ashbrand Boots", "Ashen Plate Boots"]
letter_b_boots = ["Battleon Militia Boots", "Beta Berserker Boots", "Blood Knight Boots"]
letter_c_boots = ["Campy Boots", "Chewed Zardscale Boots", "Chiropteran Boots", "Chronomancer Boots", "Crimson Battle Mage Boots"]
letter_d_boots = ["Dark Defender Boots", "Dark Leather Boots", "Defender Knight Boots", "Defender Mage Boots", "Defender Rogue Boots", "Dragon Berserker Boots"]
letter_d2_boots = ["Dragon Champion Greaves", "Dragon Stalker Boots", "DragonSlayer Boots", "Drake Hunter Boots", "Dread Hood Boots", "Dricken Armored Boots", "Dricken Leather Feet"]
letter_d3_boots = ["Dwarven Foreman Boots", "Dwarven Miner Boots"]
letter_e_boots = ["Ebon Talon Greaves", "Elite Dragon Champion Greaves", "Elvenguard Boots", "Eternal Chronomancer Boots"]
letter_f_boots = ["Fire Mage Boots", "Fire Rogue Boots", "Frost Defender Boots", "Frostlorn Mage Boots"]
letter_f2_boots = ["Frostlorn Rogue Boots", "Frostlorn Warrior Boots", "Frostval Elf Boots", "Furnace Knight Boots"]
letter_g_boots = ["Golden Boots", "Grampy\'s Leather Boots", "Guardian Boots", "Guardian Dragon Boots"]
letter_h_boots = ["Holey Witch Shoes"]
letter_i_boots = ["Invisible Boots","Iron Berserker Boots"]
letter_k_boots = ["Keen Alpha Pirate Boots", "Kickstarter Guardian Boots"]
letter_l_boots = ["Leather Boots", "Leather Pirate Boots", "Legion Grunt Boots", "Legion Zealot Boots"]
letter_m_boots = ["Mage Shoes", "Magmarran Boots"]
letter_n_boots = ["Naval Commander Boots", "Night Guard Boots", "Noble\'s Boots"]
letter_o_boots = ["Oroku Boots"]
letter_p_boots = ["Pebblar Shell Boots", "Phoenix Knight Boots", "Plutocrat Boots", "Pumpkin Lord Boots", "Pumpkinmancer Boots"]
letter_r_boots = ["Red Elf Boots", "Red Eye Boots", "Runed Elvenguard Boots"]
letter_s_boots = ["Santa Boots", "Scale Slayer Greaves", "Scoundrel Boots", "Serpent Fighter Boots", "Shadow Leather Boots", "Shadowed Blood Boots"]
letter_s2_boots = ["Shadowed Boots", "Shadowed Plate Boots", "Shadowslayer E\'s Boots", "Shadowslayer R\'s Boots", "Shrade\'s Boots"]
letter_s3_boots = ["Soothsayer Boots", "Spiritual Warrior Boots", "Spooky Witch Shoes", "Sturdy Leather Boots"]
letter_t_boots = ["Talyn\'s Boots", "Trollukstein Boots", "Twilight Wolf Boots"]
letter_u_boots = ["Unbound Boots", "Unbound Vamp Boots", "Undead Vindicator Boots", "Undead Warrior Boots", "Undead Guardian Boots"]
letter_v_boots = ["Vost\'s Boots"]
letter_w_boots = ["Warrior Boots", "Witch Shoes", "Wolf Skin Boots"]
letter_z_boots = ["Zardscale Boots"]
@bot.command()
async def boots():
    embed = discord.Embed(title="Boots", description="Current Boots listed in the wiki bot.", color=0x00a0ea)
    embed.set_thumbnail(url="https://thumb.ibb.co/jnBPB7/descarga.png")
    embed.add_field(name="Letter A", value=letter_a_boots)
    embed.add_field(name="Letter B", value=letter_b_boots)
    embed.add_field(name="Letter C", value=letter_c_boots)           
    embed.add_field(name="Letter D", value=letter_d_boots)
    embed.add_field(name="Letter D", value=letter_d2_boots)
    embed.add_field(name="Letter D", value=letter_d3_boots)
    embed.add_field(name="Letter E", value=letter_e_boots)
    embed.add_field(name="Letter F", value=letter_f_boots)
    embed.add_field(name="Letter F", value=letter_f2_boots)
    embed.add_field(name="Letter G", value=letter_g_boots)
    embed.add_field(name="Letter H", value=letter_h_boots)
    embed.add_field(name="Letter I", value=letter_i_boots)
    embed.add_field(name="Letter K", value=letter_k_boots)           
    embed.add_field(name="Letter L", value=letter_l_boots)
    embed.add_field(name="Letter M", value=letter_m_boots)
    embed.add_field(name="Letter N", value=letter_n_boots)
    embed.add_field(name="Letter O", value=letter_o_boots)
    embed.add_field(name="Letter P", value=letter_p_boots)
    embed.add_field(name="Letter R", value=letter_r_boots)
    embed.add_field(name="Letter S", value=letter_s_boots)
    embed.add_field(name="Letter S", value=letter_s2_boots)
    embed.add_field(name="Letter S", value=letter_s3_boots)
    embed.add_field(name="Letter T", value=letter_t_boots)
    embed.add_field(name="Letter U", value=letter_u_boots)
    embed.add_field(name="Letter V", value=letter_v_boots)
    embed.add_field(name="Letter W", value=letter_w_boots)
    embed.add_field(name="Letter Z", value=letter_z_boots)
    await bot.say(embed=embed)
    
letter_a_monsters = ["Abyss Warfiend", "Abyss Warsworn", "Acevorah", "Agressive Skeleton", "Agitated Pebblar", "Air Elemental", "Akriloth"]
letter_a2_mosnters = ["Akriloth Exposed", "Alpha Maroon Frogzard", "Alpha Twilight Hound", "Ancient Evil", "Angered Acevorah", "Angered Controlled Villager", "Angered Frogvorah"]
letter_a3_monsters = ["Angered Mature Braintick"]
abysswarfiend = {
    'Abyss Warfiend', 'Abyss warfiend', 'abyss warfiend'
}

@bot.command()
async def monsters(*, monsters: str):
    await bot.say("Beta")
    
@bot.command()
async def char(*, char):
    string = char
    new_string = string.replace(" ", "%20")
    url = "https://game.aq3d.com/account/Character?id=" + new_string

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            if 'placeholder="Character Name"' in html:
                return await bot.say(":x: That character could not be found.")

            soup = BeautifulSoup(html, "html.parser")

            main = soup.find("div", attrs={"class":["text-center", "nopadding"]})
            char = main.find("h1").text
            level = main.find("p").text.split()[1]
            class_img_attr = [img for img in soup.find_all("img", attrs={
                "class": ["img-responsive", "center-block"]
            }) if "/char" in img["src"]][0]
            class_name = class_img_attr["alt"]

            badges = soup.find_all("h3", attrs={"class": "h4"})
     
                #await bot.say(f"{username} : {level} : {class_name} : {badges[0].text}")
            embed = discord.Embed(title=f"{char}" + " character's profile.", color=0x463dfc)
            embed.set_thumbnail(url="https://thumb.ibb.co/mTpYvo/helix.png")
            embed.set_image(url=f"https://game.aq3d.com{class_img_attr['src']}")
            embed.add_field(name="Level", value=f"{level}")
            embed.add_field(name="Class", value=f"{class_name}")
            formatted_badges = "\n".join([b.text for b in badges])
            if len(formatted_badges) > 700:  
               embed.add_field(name="Badges", value = "\n".join([b.text for b in badges[:35]]))
               num_of_parts = math.ceil(len([b.text for b in badges]) / 35)
               for i in range(1, num_of_parts):
                   embed.add_field(name='\u200b', value="\n".join([b.text for b in badges[35*i:35*(i+1)]]))
            else:
                embed.add_field(name="Badges", value=formatted_badges if len(badges) > 0 else "--No badges--")
                embed.set_footer(text="Melodia Bot ~ AdventureQuest 3D Community © ")
            await bot.say(embed=embed)
@bot.command()
async def badges(pass_context=True):
    embed = discord.Embed(title="Badges List", description="Here you will find all the badges from AQ3D (Still in development)", color=0x00a0ea)
    embed.set_thumbnail(url = "https://thumb.ibb.co/euN8un/AQ3_D_Logo_T_shirt.png")
    embed.add_field(name="Badges (Loyalty)".format("null"), value="Alpha Knight ~ Closed Beta ~ Guardian ~ Dragon Guardian ~ Pre Beta ~ Backer ~ Founder ~ Epic Founder ~ Legendary Founder ~ Determined ~")
    embed.add_field(name="Badges (Special)".format("null"), value="Undersworn T-shirt ~ Dage Collection 2018 ~ Zorbak Blue Moglin Plush Hat ~ 2018 Calendar ~ Eternal Chronomancer ~ Frostval Collector 2017 ~ Contest Swimsuit Edition 2016 ~ April Fools Day ~ Legion Pledge Scroll ~ AE 2017 Calendar ~ AQ3D Logo T-shirt ~")
    embed.add_field(name="Badges (Lore)".format("null"), value="Little Dread Bested ~ Firezilla Challenge ~ Burning Man Challenge ~ River Stone ~")
    embed.add_field(name="Important!".format("null"), value="Type wiki.badge \"badgename\" for more details. Example: wiki.badge alpha knight")  
    await bot.say(embed=embed)    
alphaknight = {
    'Alpha Knight', 'Alpha knight', 'alpha knight'
}
closedbeta = {
    'Closed Beta', 'Closed beta', 'closed beta'
}
guardian = {
    'Guardian', 'guardian'
}
dragonguardian = {
    'Dragon Guardian', 'Dragon guardian', 'dragon guardian'
}
prebeta = {
    'Pre Beta', 'Pre beta', 'pre beta'
}
backer = {
    'Backer', 'backer'
}
undersworn = {
    'Undersworn', 'undersworn'
}
dagecollector = {
    'Dage Collector', 'dage collector'
}
calendar2018 = {
    'Eternal Chronomancer', 'eternal chronomancer', 'Calendar 2018', 'calendar 2018'
}
    
@bot.command()
async def badge(*, badge: str):
    if badge in alpha_knight_armor:
        embed = discord.Embed(title="AQ3D Alpha Knight", description="Participated in the Alpha Test. A knight from the days of old... before AdventureQuest 3D was even a game..", color=0x00ff00)
        embed.set_thumbnail(url = "https://thumb.ibb.co/bSkVPn/Alpha_Knight.png")
        await bot.say(embed=embed)
    elif badge in closedbeta:
        embed = discord.Embed(title="AQ3D Closed Beta", description="Awarded to all players who took part in the closed beta of AdventureQuest 3D.", color=0x00ff00)
        embed.set_thumbnail(url = "https://thumb.ibb.co/mvzX4n/Closed_Beta.png")
        await bot.say(embed=embed)
    elif badge in guardian:
        embed = discord.Embed(title="AQ3D Guardian", description="Guardian of AdventureQuest 3D! Will include Guardian Class, access to the Guardian tower and special guardian quests & perks.", color=0x00ff00)
        embed.set_thumbnail(url = "https://thumb.ibb.co/dYeoc7/Guardian.png")
        await bot.say(embed=embed)
    elif badge in dragonguardian:
        embed = discord.Embed(title="AQ3D Dragon Guardian", description="You have answered the call of the Dragon Guardian! Your passion and might are unmatched!", color=0x00ff00)
        embed.set_thumbnail(url = "https://thumb.ibb.co/dofBx7/Dragon_Guardian.png")
        await bot.say(embed=embed) 
    elif badge in prebeta:
        embed = discord.Embed(title="AQ3D Pre Beta", description="Awarded to every hero who had a character during AQ3D's Pre-Beta testing phase!", color=0x00ff00)
        embed.set_thumbnail(url = "https://thumb.ibb.co/facrx7/Pre_Beta.png")
        await bot.say(embed=embed)
    elif badge in backer:
        embed = discord.Embed(title="AQ3D Backer", description="\"I've got your back!\" Backed the AdventureQuest 3D project on Kickstarter.",color=0x00ff00)
        embed.set_thumbnail(url = "https://thumb.ibb.co/naDQPn/backer.png")
        await bot.say(embed=embed)
    elif badge in undersworn:
        embed = discord.Embed(title="Undersworn T-Shirt", description="You have spoken the oath in Undertongue. You are of the Undead Legion now and forever.",color=0x00ff00)
        embed.set_thumbnail(url = "https://thumb.ibb.co/bMbtun/Undersworn.png")
        await bot.say(embed=embed)
    elif badge in dagecollector:
        embed = discord.Embed(title="Dage's Collector 2018", description="You have purchased Dage's entire 2018 Dage Collection! Visit Melodia to access your undead items at any time! For the Legion!",color=0x00ff00)
        embed.set_thumbnail(url = "https://image.ibb.co/dQLmEn/Dage_Collection1.jpg")
        await bot.say(embed=embed)
    elif badge in calendar2018:
        embed = discord.Embed(title="2018 Calendar - Eternal Chronomancer", description="Shop unlocked with the purchase of the AE 2018 Calendar. ",color=0x00ff00)
        embed.set_thumbnail(url = "https://image.ibb.co/n0xcLS/Eternal_Chronomancer.jpg")
        await bot.say(embed=embed)
    else:
        await bot.say("Fatal error! :anger: Please check your grammar or try again! If problem persists contact bot owner.")

letter_a_gloves = ["Alpha Knight Gloves", "Alpha Pirate Gloves", "Ancient Evil Gloves", "Ashbrand Gloves"]

letter_a2_gloves = ["Ashen Armplates", "Ashen Wristguards"]

letter_b_gloves = ["Battleon Militia Gloves", "Beta Berserker Gauntlets", "Bloodknight Vambraces", "Bloodknight Wristplates", "Box-ing Gloves"]

letter_c_gloves = ["Campy Gloves", "Cardboard Gloves", "Chiropteran Gloves"]

letter_c2_gloves = ["Chronomancer Gloves", "Clawed Rogue Gloves", "Crimson Battle Mage Gloves"]

letter_d_gloves = ["Dark Defender Gloves", "Defender Knight Gloves", "Defender Mage Gloves", "Defender Rogue Gloves", "Dragon Berserker Gloves"]

letter_d2_gloves = ["Dragon Champion Gauntlets", "Dragonslayer Gloves", "Drake Hunter Gloves", "Dread Hood Gloves", "Dream Warden\'s Gloves"]

letter_d3_gloves = ["Dwarven Foreman Gloves", "Dwarven Miner Gloves"]

letter_e_gloves = ["Ebon Talon Gloves", "Elite Dragon Champion Gloves", "Elvenguard Gloves", "Eternal Chronomancer Gloves"]

letter_f_gloves = ["Feathered Gauntlets", "Fire Mage Gloves", "Fire Rogue Gloves", "Force Master Gloves", "Frost Defender Gloves"]

letter_f2_gloves = ["Frostlorn Mage Gloves", "Frostlorn Rouge Gloves", "Frostlorn Warrior gloves(DC)", "Frostlorn Warrior Gloves (non-DC)", "Frostval Elf Gloves (2016)"]

letter_f3_gloves = ["Frostval Elf Gloves(2017)", "Furnace Knight Gloves"]

letter_g_gloves = ["Gauntlets of the Night Guard", "Golden Vambraces", "Golden Wristplates", "Guardian Dragon Gloves", "Guardian Gloves"]

letter_h_gloves = ["Hardened Shackles", "Heavy Gloves"]

letter_i_gloves = ["Invisible Gloves", "Iron Berserker Gloves"]

letter_j_gloves = ["Jagulope Gloves"]

letter_k_gloves = ["Kickstarter Guardian Gloves", "Kylord Gloves"]

letter_l_gloves = ["Lava Fits", "Leather Pirate Gloves(DC)", "Leather Pirate Gloves(non-DC)", "Legion Grunt Gloves", "Legion Zealot Gloves(DC)"]

letter_m_gloves = ["Mac\'gyver\'d Gloves", "Mage Casting Gloves", "Magmarran Gloves"]

letter_n_gloves = ["Naval Commander Gloves(DC)", "Naval Commander Gloves(non-DC)", "Noble\'s Gloves"]

letter_o_gloves = ["Oroku Gloves"]

letter_p_gloves = ["Peblar Shell Gloves", "Phoenix Knight Gloves", "Plutocrat Gloves", "Pumpkin Lord Gloves", "Pumpkinmancer Gloves"]

letter_r_gloves = ["Red Elf Gloves(2016)", "Red Elf Gloves(2017)", "Rounge Gloves", "Runed Elvenguard Gloves"]

letter_s_gloves = ["Santa Gloves", "Scale Slayer Gauntlets", "Serpent Fighter Grips", "Shadowed Blood loves", "Shadowed Gloves"]

letter_s2_gloves = ["Shadowed Plate Gloves", "ShadowSlayer E\'s Gloves", "ShadowSlayer R\'s Gloves", "Shard Encrusted Fists", "Shrade\'s Chains"]

letter_s3_gloves = ["Slimy Gloves", "SoothSayer Gloves", "Spiritual Warrior Gloves", "Stone Gauntlets"]

letter_t_gloves = ["Talyn\'s Gloves", "Thin Paper Gloves", "Torn Witch Gloves", "Trollukstein Gloves(DC)", "Trollukstein Gloves(non-DC)"]

letter_u_gloves = ["Unbound Gloves", "Unbound Vamp Gloves", "Undead Vindicator Gloves", "Undead Warrior Gloves", "Under Guardian Gloves"]

letter_v_gloves = ["Vost's Gloves"]

letter_w_gloves = ["Warrior Gauntlets", "Witch Gloves", "Wolf Handler\'s Gloves", "Wristplates"]

letter_z_gloves = ["Zardscale Gloves"] 
@bot.command()
async def gloves():
    embed = discord.Embed(title="Gloves", description="Current Gloves listed in the wiki bot.", color=0x00a0ea)
    embed.set_thumbnail(url="https://thumb.ibb.co/jnBPB7/descarga.png")
    embed.add_field(name="Letter A", value=letter_a_gloves)
    embed.add_field(name="Letter B", value=letter_a2_gloves)
    embed.add_field(name="Letter B", value=letter_b_gloves)           
    embed.add_field(name="Letter C", value=letter_c_gloves)
    embed.add_field(name="Letter C", value=letter_c2_gloves)
    embed.add_field(name="Letter D", value=letter_d_gloves)
    embed.add_field(name="Letter D", value=letter_d2_gloves)
    embed.add_field(name="Letter D", value=letter_d3_gloves)
    embed.add_field(name="Letter E", value=letter_e_gloves)
    embed.add_field(name="Letter F", value=letter_f_gloves)
    embed.add_field(name="Letter F", value=letter_f2_gloves)
    embed.add_field(name="Letter F", value=letter_f3_gloves)
    embed.add_field(name="Letter G", value=letter_g_gloves)           
    embed.add_field(name="Letter H", value=letter_h_gloves)
    embed.add_field(name="Letter I", value=letter_i_gloves)
    embed.add_field(name="Letter J", value=letter_j_gloves)
    embed.add_field(name="Letter K", value=letter_k_gloves)
    embed.add_field(name="Letter L", value=letter_l_gloves)
    embed.add_field(name="Letter M", value=letter_m_gloves)
    embed.add_field(name="Letter N", value=letter_n_gloves)
    embed.add_field(name="Letter O", value=letter_o_gloves)
    embed.add_field(name="Letter P", value=letter_p_gloves)
    embed.add_field(name="Letter R", value=letter_r_gloves)
    embed.add_field(name="Letter S", value=letter_s_gloves)
    embed.add_field(name="Letter S", value=letter_s2_gloves)
    embed.add_field(name="Letter S", value=letter_s3_gloves)
    embed.add_field(name="Letter T", value=letter_t_gloves)
    embed.add_field(name="Letter U", value=letter_u_gloves)
    embed.add_field(name="Letter V", value=letter_v_gloves)
    embed.add_field(name="Letter W", value=letter_w_gloves)
    embed.add_field(name="Letter Z", value=letter_z_gloves)
    await bot.say(embed=embed)
'''                
letter_a_monsters = ["Abyss Warfiend", "Abyss Warsworn", "Acevorah(Monster)", "Aggressive Skeleton", "Agitated Pebblar"]
letter_a2_monsters = ["Air Elemental", "Akriloth", "Akriloth Exposed", "Alpha Maroon Frogzard", "Alpha Twilight Hound"]
letter_a3_monsters = ["Ancient Evil(1)", "Ancient Evil(2)", "Angered Acevorah", "Angered Controlled Villager", "Angered Frogvorah"]
letter_a4_monsters = ["Angered Ghost", "Angered Mature Braintick", "Angry Snowman", "Apocalypse Slime", "Apocalypse Zard"]
letter_a5_monsters = ["Aquazard", "Armored Black Dragonling", "Attacker Eye"]
letter_b_monsters = ["Bank Robber", "Bat Swarm", "Big Bones", "Big Bones General", "Bite Coin"]
letter_b2_monsters = ["Blight Hound", "Blightcrystal Bandit", "BloodKnight", "Bludroot", "Blue Berry"]
letter_b3_monsters = ["Blue Cheese", "Blue Flying Eye", "Blue Ogre", "Blue Velvet", "Blue Whale"]
letter_b4_monsters = ["Bog Sneevil", "Bone Guardian", "Bone Spider", "Boogerling", "Bothvar Yettisson"]
letter_b5_monsters = ["Bridge Skeleton", "Brutalcorn", "Burning Warsworn"]
letter_c_monsters = ["Cadaverous Frogzard", "Carnivorous Clawg", "Cave Frogzard", "Cave Ghoul", "Cave Skeleton"]
letter_c2_monsters = ["Cave Sneevil", "Cave Spider", "Cavern Crawler", "Cavern Spider", "Cavezard"]
letter_c3_monsters = ["Charred Undead", "Chorty", "Clawg Minion", "Coggweller", "Commander Ironclaw"]
letter_c4_monsters = ["Commander Ironfang", "Common Doomwood Chest", "Common Greenguard Chest", "Common Tower Chest", "Controlled Villager"]
letter_c5_monsters = ["Crawler", "Creaky Spider", "Crimson Circle Mage", "Crimson Conjuror", "Crimson Hellhound"]
letter_c6_monsters = ["Crispy Undead", "Crystal Queen Spider", "Crystalized Clawg", "Crystalized Spider", "Cursed Island Pirate"]
letter_d_monsters = ["Damp Zombie", "Dark Harvester", "Dark Legion Arachnid", "Dark Legion Behemoth", "Dark Legion Dragon"]
letter_d2_monsters = ["Dark Legion Horde", "Dark Legion Renegade", "Dark Memory", "Dark Necrohencer", "Dark Slime Lord"]
letter_d3_monsters = ["Dark Warfiend", "David", "Deadtooth", "Deadwood", "Death Knight"]
letter_d4_monsters = ["Deogarth", "Destroyer Dragon", "Direwolf", "Dirty Pirate", "Disloyal Sneevil"]
letter_d5_monsters = ["Disturbed Drakimp", "Doomed Shrade", "Doomguard Garr", "DoomSeer Prime", "Doomwraith Dorn"]
letter_d6_monsters = ["Dragon Whelp", "Dragonling", "Drakimp", "Drakimp Scout", "Drak-imperor"]
letter_d7_monsters = ["Dravir", "Dravir Commander", "Dravir Guard", "Dravir Scout", "Dravir Soldier"]
letter_d8_monsters = ["Dravir Usurper", "Dread Gazer", "Dread Spider", "Dreadwood", "Dricken"]
letter_d9_monsters = ["DrickenBones", "Drooster", "Dusk Wolf", "Dusk Wolf Brute", "Dust Golem"]
letter_e_monsters = ["Earth Elemental", "East Warsworn", "East Wing Warlock", "Eight Legged Terror", "Elite Skeletal Invader"]
letter_e2_monsters = ["Elite Vault Security", "Emberzard", "Enchanted Hellhound", "End of Days Warfiend", "Enraged Clawg"]
letter_e3_monsters = ["Enraged Valek", "Enraged Wolf Spirit", "Enraged Wrythion", "Epic Angry Snowman", "Epic Frostsaber Wolf"]
letter_e4_monsters = ["Epic Gourd\'thulu", "Epic Ice Revenant", "Epic Mini Snowman", "Epic Yettun", "Epic Yettun\'s Eye"]
letter_e5_monsters = ["Escaped Voidling", "Extra Roasted Dricken", "Eye of Darkness"]
letter_f_monsters = ["Faustbite", "Feral Frogzard", "Fiery Dravir", "Fire Elemental", "Fire Phan"]
letter_f2_monsters = ["Firespine", "Firezard", "Firezard Swarm", "Firezilla", "Flying Skull"]
letter_f3_monsters = ["Fool\'s Gold", "Forest Wolf", "Fresh Undead", "Frogvorah", "Frogzard"]
letter_f4_monsters = ["Frost Dravir", "Frost Hound", "Frostsaber Wolf", "Frostsaber Wolf Keeper", "Frozen Warrior"]
letter_f5_monsters = ["Furious Frogzard"]
letter_g_monsters = ["Galanoth(Monster)", "Game Ogre", "Gargoyle", "Gargoyle Guardian", "GateWraith"]
letter_g2_monsters = ["General Evenmor", "General Gathmor", "General Hakesh", "General Hoth", "General Skellak"]
letter_g3_monsters = ["General Wrythion", "General Zelleth", "General Zulkus", "Ghastly Ghost", "Ghastly Gourdite"]
letter_g4_monsters = ["Ghastly Harvester", "Ghastly Lil\' Spider", "Ghastly Skeleton", "Ghastly Spider", "Ghastly Tricksters"]
letter_g5_monsters = ["Ghost Dog", "Ghostly Guardian", "Ghostly Guardians", "Ghostly Spellsword", "Ghostly Warrior"]
letter_g6_monsters = ["Ghostly Warrior", "Ghoul Minion", "Giant Crispy Undead", "Giant Spider", "Golden Eye"]
letter_g7_monsters = ["Golden Retriever", "Gold Rush", "Gorthor The Warfiend", "Gourdite", "Gourd\'thulu"]
letter_g8_monsters = ["Granite Gollum", "Grave Skeleton", "Great Lava Worm", "Greenguard Ent", "Grim Ghost"]
letter_g9_monsters = ["Grove Stalker", "Grumpy Snowman", "Guard Wolf", "Guardian HighLord", "Guardian Opponent"]
letter_g10_monsters = ["Guarding Arachnid"]
letter_h_monsters = ["Haunted Skeleton", "Healer Eye", "Heavy Vault Security", "Hollow Ixtis", "Honey Moglin"]
letter_h2_monsters = ["Hostile Green Frogzard", "Huge Lava Worm", "Hulking Spider"]
letter_i_monsters = ["Ice Revenant", "Ice Revenant Keeper", "Incendium", "Infected Burden", "Infected Pebblar"]
letter_i2_monsters = ["Infected Pebblar Beast", "Infected Zombie", "Infernal", "Infernal Sentry", "Infernal Watcher"]
letter_i3_monsters = ["Ingot the 14K9", "Insectoid", "Intro Skeleton", "Invading Dragon", "Invading Drake"]
letter_i4_monsters = ["Invading Drakimp", "Invading Dravir", "Invading Firezard", "Invading Hellhound", "Invading Infernal"]
letter_i5_monsters = ["Invading Observer", "Invading Phan", "Invading Towering Dravir", "Island Clawgling", "Ixtis Harvester"]
letter_j_monsters = ["Jacked Skellington", "Jackpot"]
letter_k_monsters = ["King Sneed", "Krusty Klawg"]
letter_l_monsters = ["Lair Dravir", "Lair Dravir Commander", "Lava Globs", "Lava Hydra", "Lava Hydra Heart"]
letter_l2_monsters = ["Laval Lord Gorm", "Lava Rocky", "Lava Tunnel Globs", "Legion Arachnid", "Legion Arachnus"]
letter_l3_monsters = ["Legion Behemoth", "Legion Corpus", "Legion Dragon", "Legion Drakaus", "Legion Grunt"]
letter_l4_monsters = ["Legion Horde", "Legion Hound", "Legion Minion", "Legion Ossa Magnus", "Legion Quaesitor"]
letter_l5_monsters = ["Legion Renegade", "Legion Revenant", "Legion Warfiend", "Lieutenant Dan", "Lieutenant Stan"]
letter_l6_monsters = ["Little Dread(Monster)", "Little Ogre Blue", "Living Root", "Lootable Vault Chest", "Lord Anemis"]
letter_l7_monsters = ["Loyal Firezard", "Loyal Phan", "Lurking Behemoth", "Lycan Guard", "Lycan Prowler"]
letter_l8_monsters = ["Lychimera"]
letter_m_monsters = ["Mad Air Spirit", "Mad Earth Spirit", "Mad Fire Spirit", "Mad Water Spirit", "Major FrostBiter"]
letter_m2_monsters = ["Malthamas", "Mammazard", "Maroon Frogzard", "Mature Braintick", "Megazard"]
letter_m3_monsters = ["Megazard(PTR)", "Mine Sentinel", "Mini Snowman", "Mini Spider", "Mini-Sneevil"]
letter_m4_monsters = ["Mitch", "Molten Undead", "Monsterous Bat", "Mother Hen", "Mud Lord"]
letter_m5_monsters = ["Mystic Bones"]
letter_n_monsters = ["Necrochibi", "Necroknight", "Nightlocke Scytheblade(Monster)", "Nightlocke War Axe(Monster)", "Nightlocke War Staff(Monster)"]
letter_n2_monsters = ["Nightmare Axaz", "Nightmare Pahua", "Nightmare Snek", "Nightmare Zolin", "North Warsworn"]
letter_n3_monsters = ["Nugget"]
letter_o_monsters = ["Ogreman", "Ogreman the GameOgre", "Oops Dog", "Oops Infernal", "Oops Seer"]
letter_o2_monsters = ["Oops Spellsword", "Oops Spider", "Outcast Alpha Wolf", "Outcast Frogzard", "Outcast Hand"]
letter_p_monsters = ["Pack Leader Antonia", "Pack Leader Cassius", "Pahua(Monster)", "Past Self", "Pebblar"]
letter_p2_monsters = ["Pebblar Broodmother", "Phrozen", "Pirate Mate", "Pirate Wench", "Pit Shrade"]
letter_p3_monsters = ["Poisonous Gas", "Proto Lava Worm", "Pumken", "Pumpkin Lord"]
letter_r_monsters = ["Rabid Wolf", "Raging Ironclaw", "Raging Ironfang", "Raging Trolluk", "Raid Warfiend"]
letter_r2_monsters = ["Rare Doomwood Chest", "Rare Greenguard Chest", "Rare Tower Chest", "Rashhek", "Red Dragonling"]
letter_r3_monsters = ["Red Flying Eye", "Red Frogzard", "Red Winged Eye", "Reinforcement Soldier", ""Retired" Counselor"]
letter_r4_monsters = ["Roaming Rocky", "Roasted Dricken", "Rocky", "Rushing Wave"]
letter_s_monsters = ["Salty Swab", "Sand Pebblar", "Scary Lil\' Spider", "Scary Spider", "Scrappy"]
letter_s2_monsters = ["Sergeant Iceheart", "Shadow Crawler", "Shadow Seer", "Shadow Tricksters", "Shadow Wolf"]
letter_s3_monsters = ["Shadow Wolf Alpha", "Shadowzard", "Shard Pebblar", "Shiny Fool\'s Gold", "Shiny Golden Retriever"]
letter_s4_monsters = ["Shiny Nugget", "Shrade", "Shrade Minion", "Sister of Yore", "Skeletal Crawler"]
letter_s5_monsters = ["Skeletal Invader", "Skeletal Mage", "Skeletal Minion", "Skeleton", "Sleet"]
letter_s6_monsters = ["Slime Lord", "Smash Mash the Trolluk", "Sneevil", "Sneevil Guard", "Snow Goon"]
letter_s7_monsters = ["Snow Monster", "Snowcrasher", "Snowman Keeper", "Southwarsworn", "SpiDricken"]
letter_s8_monsters = ["Spoopy Spider", "Stalking Dravir", "Steelfang", "Stoic Gargoyle", "Subterrachne"]
letter_s9_monsters = ["Summoned Flying Skull", "Summoned Tower Skeleton", "Summoned Towering Bones", "Summoned Warsword", "Sunken Shrade"]
letter_s10_monsters = ["Sword in the Stone"]
letter_t_monsters = ["Talyn", "Terrortoma", "The Burning Man", "Top Vault Guard", "Totem"]
letter_t2_monsters = ["Tovus the Bladedog", "Tower Skeleton", "Towering Bones", "Towering Huge Bones", "Towering Infernal Invader"]
letter_t3_monsters = ["TowerWraith", "Town Tricksters", "Trained Frogzard", "Training Frogzard", "Transformed Ghoul"]
letter_t4_monsters = ["Tree Frogzard", "Tree Sneevil", "Treevenge", "Trollenstein\'s Monster", "Trolluk"]
letter_t5_monsters = ["Trolluk", "Troma Terrortoma", "Tunnel Dravir", "Tunnel Dravir Commander", "Twilight Hound"]
letter_t6_monsters = ["Tyrion the Tyrant"]
letter_u_monsters = ["Umbral Wolf", "Unbound Vamp", "Uncommon Doomwood Chest", "Uncommon Greenguard Chest", "Uncommon Tower Chest"]
letter_u2_monsters = ["Undead Dragon", "Undead Terror", "Undead Warrior Armor(Monster)", "Unstable Outcast Hand"]
letter_v_monsters = ["Valek", "Vamir the Chronomancer", "Vampire Guard", "Vampire Knight", "Vampire Sentry"]
letter_v2_monsters = ["Vault Guard", "Viassayth", "Void Knightmare(Monster)", "Voidling", "Voidling Patroller"]
letter_v3_monsters = ["Volcanic Black Dragonling", "Volcanic Firezard", "Volcanic Green Dragonling", "Volcanic Hellhound", "Volcanic Infernal"]
letter_v4_monsters = ["Volcaning Infernal - Weak", "Volcanic Minion", "Volcanic Red Dragon", "Volcanic Red Dragonling", "Volcanic Tunnel Infernal"]
letter_v5_monsters = ["Volcanic Wasworn", "Vulgren", "VurrMan", "Vurrmenator"]
letter_w_monsters = ["Wall of Pain", "Wall Spider", "Warwolf", "Warwolf Chieftain", "Water Elemental"]
letter_w2_monsters = ["Weakend Crawler", "Weakend Skeleton", "Werewolf", "West Wing Witch", "Wild Drakimp"]
letter_w3_monsters = ["Wild Wolf", "Wolf", "Wraith of Destruction"]
letter_y_monsters = ["Yettun", "Yettun\'s Eye", "Yettun\'s Eye Keeper", "Young Lava Worm"]
letter_z_monsters = ["Zolin(Monster)", "Zombie"]
@bot.command()
async def monsters():
    embed = discord.Embed(title="Monsters", description="Current Monsters listed in the wiki bot.", color=0x00a0ea)
    embed.set_thumbnail(url="https://thumb.ibb.co/jnBPB7/descarga.png")
    embed.add_field(name="Letter A", value=letter_a_gloves)
    embed.add_field(name="Letter B", value=letter_a2_gloves)
    embed.add_field(name="Letter B", value=letter_b_gloves)           
    embed.add_field(name="Letter C", value=letter_c_gloves)
    embed.add_field(name="Letter C", value=letter_c2_gloves)
    embed.add_field(name="Letter D", value=letter_d_gloves)
    embed.add_field(name="Letter D", value=letter_d2_gloves)
    embed.add_field(name="Letter D", value=letter_d3_gloves)
    embed.add_field(name="Letter E", value=letter_e_gloves)
    embed.add_field(name="Letter F", value=letter_f_gloves)
    embed.add_field(name="Letter F", value=letter_f2_gloves)
    embed.add_field(name="Letter F", value=letter_f3_gloves)
    embed.add_field(name="Letter G", value=letter_g_gloves)           
    embed.add_field(name="Letter H", value=letter_h_gloves)
    embed.add_field(name="Letter I", value=letter_i_gloves)
    embed.add_field(name="Letter J", value=letter_j_gloves)
    embed.add_field(name="Letter K", value=letter_k_gloves)
    embed.add_field(name="Letter L", value=letter_l_gloves)
    embed.add_field(name="Letter M", value=letter_m_gloves)
    embed.add_field(name="Letter N", value=letter_n_gloves)
    embed.add_field(name="Letter O", value=letter_o_gloves)
    embed.add_field(name="Letter P", value=letter_p_gloves)
    embed.add_field(name="Letter R", value=letter_r_gloves)
    embed.add_field(name="Letter S", value=letter_s_gloves)
    embed.add_field(name="Letter S", value=letter_s2_gloves)
    embed.add_field(name="Letter S", value=letter_s3_gloves)
    embed.add_field(name="Letter T", value=letter_t_gloves)
    embed.add_field(name="Letter U", value=letter_u_gloves)
    embed.add_field(name="Letter V", value=letter_v_gloves)
    embed.add_field(name="Letter W", value=letter_w_gloves)
    embed.add_field(name="Letter Z", value=letter_z_gloves)
    await bot.say(embed=embed)
'''

conn = sqlite3.connect("user_data.db")
cursor = conn.cursor()
 
timed_users = {}
 
@bot.command(pass_context=True)
async def daily(ctx):
    reward = random.randint(10, 16)
    if ctx.message.author.id not in timed_users:
        timed_users[ctx.message.author.id] = math.floor(time.time())
    else:
        current_time = math.floor(time.time())
        elapsed_time = current_time - timed_users[ctx.message.author.id]
        remaining_time = 43200 - elapsed_time
 
        if elapsed_time < 43200:
            formatted_time = str(datetime.timedelta(seconds=remaining_time)).split(":")
            return await bot.say(f"You can use your next daily in **{formatted_time[0]} hours\
{formatted_time[1]} minutes {formatted_time[2]} seconds**")
 
    cursor.execute("INSERT OR IGNORE INTO userdata (ID, username, cash) VALUES(?, ?, ?)",\
     (ctx.message.author.id, str(ctx.message.author), 0))
    cursor.execute("UPDATE userdata SET cash=cash + ?, inventory='[]' WHERE ID=?", (reward, ctx.message.author.id))
    conn.commit()
    timed_users[ctx.message.author.id] = math.floor(time.time())
    return await bot.say(f"You received **{reward}** cash!")
 
@bot.command(pass_context=True)
async def shop(ctx):
    shop_items = cursor.execute("SELECT * FROM shop")
    embed = discord.Embed(title="Items", description="Current items listed in the wiki bot.", color=0x00a0ea)
    embed.set_thumbnail(url="https://thumb.ibb.co/jnBPB7/descarga.png")
    embed.add_field(name="Alpha Knight Armor", value='100$')
    embed.add_field(name="Alpha Knight Boots", value="75$")
    embed.add_field(name="Alpha Knight Gloves", value="50$")
    embed.add_field(name="Alpha Knight Helm", value="75$")
    return await bot.say(embed=embed)
@bot.command(pass_context=True)
async def buy(ctx, *, item_name):
    cursor.execute("SELECT * FROM shop WHERE item_name=? COLLATE NOCASE", (item_name,))
    item = cursor.fetchone()
 
    if not item:
        return await bot.say("Sorry, that item is not in the shop.")
 
    price = item[1]
    cursor.execute("SELECT * FROM userdata WHERE ID=?", (ctx.message.author.id,))
    user_data = cursor.fetchone()
 
    if not user_data: return await bot.say(":x: You do not have enough cash to buy this item")
    if user_data[2] < price: return await bot.say(":x: You do not have enough cash to buy this item")
 
    inventory = json.loads(user_data[3])
    if item[0] in inventory:
        return await bot.say("You already have that item")
    inventory.append(item[0])
 
    remaining_cash = user_data[2] - price
    cursor.execute("UPDATE userdata SET username=?, cash=?, inventory=? WHERE ID=?",
    (str(ctx.message.author), remaining_cash, json.dumps(inventory), ctx.message.author.id))
 
    conn.commit()
    embed = discord.Embed(description=f"You have successfully bought {item[0]} for **{item[1]}** cash!", color=discord.Color.green())
    return await bot.say(embed=embed)
 
@bot.command(pass_context=True)
async def cash(ctx):
    if ctx.message.author.id == 337343219128074240:
        sembed = discord.Embed(description="400000000000000000000", title="Cash", color=0xFFFF)
        return await bot.say(sembed=sembed)
    cursor.execute("SELECT * FROM userdata WHERE ID=?", (ctx.message.author.id,))
    user = cursor.fetchone()
    if not user:
        embed = discord.Embed(description="0", title="Cash", color=0xFFFF)
        return await bot.say(embed=embed)
    embed=discord.Embed(description=str(user[2]), title="Cash", color=0xFFFF)
    return await bot.say(embed=embed)
 
@bot.command(pass_context=True)
async def inventory(ctx):
    cursor.execute("SELECT * FROM userdata WHERE ID=?", (ctx.message.author.id,))
    user = cursor.fetchone()
    if not user:
        embed = discord.Embed(description="--Empty--", title="Cash", color=0xFFFF)
        return await bot.say(embed=embed)

    inv = "\n".join(json.loads(user[3]))
    embed = discord.Embed(description=inv, title="Inventory", color=0xFFFF)
    return await bot.say(embed=embed)

      
        
quests = ['Kill frogzard for 2xp.', 'Search for Mega Scroll for 5xp', 'Open portal for 10xp']
randomquest = random.choice(quests)
@bot.command()
async def quests():
    embed = discord.Embed(description="Quest", title=randomquest, color=0xFFFF)
    await bot.say(embed=embed)
        
        
        
        
        
greetings = ["Hello", "hello","Hi", "hi", "Hey", "hey!", "Hi there!", "hey"]
@bot.command()
async def chat(*, chat: str):
    if chat in greetings:
        await bot.say(random.choice(greetings))
token = os.environ.get("sira")
bot.run(f'{token}')

