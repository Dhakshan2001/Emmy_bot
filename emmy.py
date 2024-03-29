import discord
import logging
from discord.ext import commands
import requests
import wikipedia
import math
import cmath
import random
from bs4 import BeautifulSoup
from discord.utils import get
import asyncio
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import codecs
import aiohttp


TOKEN='Not mentioned here for privary reasons'
bot = commands.Bot(command_prefix=(['oi ','Oi ','oI', 'OI']),help_command=None)
client = discord.Client() 

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot.load_extension('jishaku')

#pre-definitions

constants = {"G":('6.67259 ⨯ 10⁻¹¹','Nm²kg⁻²'),"c":('2.99792458 ⨯ 10⁸','ms⁻¹'),"Na":('6.0221367⨯ 10²³', 'mol⁻¹'),
"R":(8.314510,"JK⁻¹mol⁻¹"),"k":('1.380658 ⨯ 10⁻²³',"JK⁻¹"),"sb":('5.67051 ⨯ 10⁻⁸',"Wm⁻²K⁻⁴"),
"b":('2.897756 ⨯ 10⁻³','mK'),"e":('1.60217733 ⨯ 10⁻¹⁹',"C"),"me":('9.1093897 ⨯ 10⁻³¹',"kg"),
"mp":('1.6726231 ⨯ 10⁻²⁷','kg'),"mn":('1.6749286 ⨯ 10⁻²⁷','kg'),"mu0":('1.2566370614359173 ⨯ 10⁻⁰⁶',"NA⁻²"),
"E0":('8.854187817 ⨯ 10⁻¹²',"C²N⁻¹m⁻²"),"F":(96485.3029,'Cmol⁻¹'),"h":('6.6260755 ⨯ 10⁻³⁴',"Js"),
"Ry":('1.0973731534⨯ 10⁷','m⁻¹'),"h0":(13.605698,"eV"),"a0":('5.29177249 ⨯ 10⁻¹¹',"m")}


#For errors

k = discord.Embed(title = "❌ Exception", description = "MissingRequiredArgument: A required argument is missing.",colour = 0xff0000)
r = discord.Embed(title = "❌ Exception", description = "MissingAnyRole: You are missing at least one of the required roles to use this command",colour = 0xff0000)
b1 = discord.Embed(title = "❌ Exception", description = "BadArgument: You need to mention an user to send them this message",colour = 0xff0000)
b2 = discord.Embed(title = "❌ Exception", description = "BadArgument: Cannot find that user",colour = 0xff0000)
#Usuals

@bot.event
async def on_ready():
    game = discord.Game("oi help")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower().startswith("oi?"):
        await message.channel.send("Yes, boss. I'm right here")
    elif message.content.lower().startswith("gg"):
        await message.add_reaction("👌")
    elif message.content.lower().startswith("gm") or message.content.lower().startswith("good morning"):
        await message.channel.send("Good morning cutie. Hope you slept well")
    await bot.process_commands(message)

@bot.command()
async def help(ctx):
    h = discord.Embed(title = "Emmy's command list",description="**General:**\nhelp: Shows this message. My prefix is `oi`\nping: The bot's latency\ndm: The bot will message on your behalf. Usage: `oi dm <user_name/id_here> <your_message_here>`\nremind: a simple reminder command. Usage: `oi <amount> <unit> <reminder message>`\nforward: use this command in the bot's dm and it will forward it to the channel assigned. Usage: `oi forward <your message>` \n\ncol: Gives a link to the Google colour picker\nemoji:Gives a link to the list of all emojis\ncovid19: Gives the current info about covid cases all over the world\nwiki: Search a topic in wikipedia\nav: Wanna see your or your friend's dp?\nurban:Look up a word in the urban dictionary\nselfmute: mute yourself for a certain amount of time. Usage `oi selfmute <time> <unit>`\nstudy: no distractions. usage `<oi study add>`. when you are done `<oi study remove>`\n\n**Fun**\noink: I am a pig now\ndie: Faking my death\nkill: Mention someone to fake *their* death\n\n**Maths**\npower: Raises the first number to the power of second\nfact: Gives the factorial of the given number\nc: For two numbers n,r gives nCr. Use as `oi combi n r`\np: For two numbers n,r gives nPr. Use as `oi permu n r`\nquad: Given the coefficients a,b,c of a quadratic equation, gives the two roots of the equation. Even if they are complex roots\nadd: Adds all the given numbers\nmulti: Gives the product of all the given numbers\n\n**Physics:**\nfitsread: reads a fits file and outputs an image\nconst: Gives the value of the physical constant you ask. Use their symbols to get their values\nconstlist: Gives you the list of all the physical constants to choose from\n\n**Admin**:\nclear: clears the denoted number of messages\nmute:mutes the specified member\nunmute:unmutes the specified member\n\n**Note**: Logout command and commands using jsk are owner only. Don't try them and expect any results",colour=0x1ab1db)
    await ctx.send(embed=h)


@bot.command()
@commands.is_owner()
async def logout(ctx):
    await ctx.send("Logging out...")
    await bot.logout()

@bot.event
async def on_command_error(ctx, error):
    h = discord.Embed(title="❌ Exception",description = 'That command is not in my directory.To know about things I do, use `oi help`. If you want to add a command, ask `Tesla#1045`',colour = 0xff0000)
    o = discord.Embed(title = "❌ Exception", description = "NotOwner: You do not own this bot.",colour = 0xf8fc03)
    if isinstance(error, commands.CommandNotFound): 
        await ctx.send(embed=h)  
    elif isinstance(error,commands.NotOwner):
        await ctx.send(embed=o)
    else:
        raise error

#General

@bot.command()
async def ping(ctx):
    await ctx.send('GODSPEED {0} '.format(round(bot.latency, 5)*1000) + " ms")

@bot.command()
async def dm(ctx, member: discord.Member,*, message: str):
    try:
        await member.send(message)
        await ctx.send(f"Successfully sent message to {member}")
    except discord.Forbidden:
        await ctx.send(f"Failed to send message to {member}.")
@dm.error
async def on_member_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = k)
    elif isinstance(error,commands.BadArgument):
        await ctx.send(embed=b1)
    else:
        pass

@bot.command(aliases=["av"])
async def avatar(ctx, *, member: discord.Member):    
    await ctx.send(member.avatar_url)
@avatar.error
async def on_memb_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(ctx.author.avatar_url)
    if isinstance(error, commands.BadArgument):
        await ctx.send(embed=b2)


@bot.command()
async def selfmute(ctx, duration = 0,*, unit = None):
    member = ctx.author
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(f"{member},you have been muted for {duration}{unit}")
    if unit == "s" or unit == "sec":
        wait = 1 * duration
        await asyncio.sleep(wait)
    elif unit == "m" or unit == "min" or unit == "mins":
        wait = 60 * duration
        await asyncio.sleep(wait)
    elif unit== "hr" or unit=="hrs":
        wait = 3600 * duration
        await asyncio.sleep(wait)
    elif unit== "day" or unit=="d" or unit== "days":
        wait = 86400 * duration
        await asyncio.sleep(wait)
    await member.remove_roles(role)
    await ctx.send(f" {member}, you are unmuted")  

@bot.command()
async def study(ctx, text:str):
    member = ctx.author
    s = discord.utils.get(ctx.guild.roles, name="I'm Studying RN 📖")
    r = discord.utils.get(ctx.guild.roles, name="Yippy")
    if text=="add":
        await member.add_roles(s)
        await member.remove_roles(r)
        await ctx.send(f" {member}, go study now")
    elif text=="remove":
        await member.add_roles(r)
        await member.remove_roles(s)
        await ctx.send(f" {member}, have fun")
    else:
        pass
@study.error
async def on_mb_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = k)
    
@bot.command()
async def remind(ctx,duration = 0, unit = None,*, text : str):
    member = ctx.author
    await ctx.send(f"I'll remind you in {duration}{unit}")
    if unit == "s" or unit == "sec":
        wait = 1 * duration
        await asyncio.sleep(wait)
    elif unit == "m" or unit == "min" or unit == "mins":
        wait = 60 * duration
        await asyncio.sleep(wait)
    elif unit== "hr" or unit=="hrs":
        wait = 3600 * duration
        await asyncio.sleep(wait)
    elif unit== "day" or unit=="d" or unit== "days":
        wait = 86400 * duration
        await asyncio.sleep(wait)
    await member.send(str(text)) 
@remind.error
async def on_argument_error(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        r = discord.Embed(title = "❌ Exception", description = "Tell me what to remind you",colour = 0xff0000)
        await ctx.send(embed=r)

@bot.command()
async def urban(ctx,word:str):
    r = requests.get("http://www.urbandictionary.com/define.php?term={}".format(word))
    soup = BeautifulSoup(r.content,features="lxml")
    m = discord.Embed(title=word,description=(soup.find("div",attrs={"class":"meaning"}).text),colour = 0x1ab1db)
    await ctx.send(embed=m)
@urban.error
async def on_word_error(ctx,error):
    if isinstance(error,commands.CommandInvokeError):
        e = discord.Embed(title = "❌ Exception", description = "This word is not in the dictionary itself",colour = 0xff0000)
        await ctx.send(embed=e)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=k)
    else:
        pass 

@bot.command(aliases=["wiki"])
async def wikiquestions(ctx,*, topic:str):
	try:
		await ctx.send(wikipedia.summary(topic)[:1000])
	except discord.ext.commands.errors.CommandInvokeError:
		await ctx.send("Something went wrong")
@wikiquestions.error
async def on_topic_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = k)

@bot.command()
async def invite(ctx):
    link = discord.Embed(title="You can invite me to your server via this",description='https://discord.com/api/oauth2/authorize?client_id=742781198325121187&permissions=0&scope=bot',colour = 0x1ab1db)
    await ctx.send(embed=link)

@bot.command()
async def emoji(ctx):
    await ctx.send("<https://www.prosettings.com/emoji-list/>")
    
@bot.command(aliases=['color','colour'])
async def col(ctx):
    await ctx.send('https://www.google.com/search?q=color+picker')

#Fun

@bot.command(aliases = ["I love you"])
async def ily(ctx, member: discord.Member):
    await ctx.send(f"I love you too {member.Mention}")

@bot.command()
async def oink(channel):
    with open('pigfarm.wav', 'rb') as fp:
        await channel.send(file=discord.File(fp, 'oink oink.wav'))


@bot.command()
@commands.is_owner()
async def alarm(ctx,member: discord.Member, n:int):
    mes = member.mention + "wake up"
    for i in range(n+1):
        await ctx.send(mes)

#Maths

@bot.command()
async def power(ctx, message1: float,message2: float):
    n = message1**message2
    m = str(n)
    if len(m) >= 2000:
        await ctx.send("**WHY WOULD YOU NEED SUCH A BIG NUMBER? I CANNOT HANDLE IT**")
    else:
        await ctx.send(n)
@power.error
async def on_overflow_error(ctx,error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Sorry. That is beyond my calculation abilities")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=k)
    else:
        pass

@bot.command(aliases=["!"])
async def fact(ctx, message: int):
    if message >= 808:
        await ctx.send("**WHY WOULD YOU NEED SUCH A BIG NUMBER? I CANNOT HANDLE IT**")
    else:
        n = math.factorial(message)
        await ctx.send(n)

@bot.command(aliases=["c"])
async def C(ctx, n:int,r:int):
    if n<r:
        await ctx.send("Learn MATHS before using this command")
    elif n > 2100000000 or r > 2100000000:
        await ctx.send("WHAT ARE YOU THINKING? AM I A **SUPERCOMPUTER** OR SOMETHING? I AM NOT GOING TO DO THAT. I SIMPLY **CANNOT**")
    elif n==r:
        await ctx.send("`1.0` *(Are you kidding me?)*")
    elif n-r==1:
        await ctx.send(f"`{n}` *(You got to be kidding me)*")
    else:
        P = math.factorial(n)/(math.factorial(n-r)*math.factorial(r)) 
        m = str(P)
        if len(m) >= 2000:
            await ctx.send("**WHY WOULD YOU NEED SUCH A BIG NUMBER? I CANNOT HANDLE IT**")
        else:
            await ctx.send(P)

@bot.command(aliases=["P"])
async def p(ctx, n:int,r:int):
    if n<r:
        await ctx.send("Learn MATHS before using this command")
    elif n==r==1:
        await ctx.send("I don't answer dumb people")
    elif n==r==2:
        await ctx.send("`2.0` But that is too dumb. Learn to use this thing you have called brain")
    elif n > 2100000000 or r > 2100000000:
        await ctx.send("WHAT ARE YOU THINKING? AM I A **SUPERCOMPUTER** OR SOMETHING? I AM NOT GOING TO DO THAT. I SIMPLY **CANNOT**")
    else:
        C = math.factorial(n)/math.factorial(n-r)
        m = str(C)
        if len(m) >= 2000:
            await ctx.send("**WHY WOULD YOU NEED SUCH A BIG NUMBER? I CANNOT HANDLE IT**")
        else:
            await ctx.send(C)

@bot.command()
async def quad(ctx,a: float,b: float,c: float):
    x1 = ((-b)+cmath.sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = ((-b)-cmath.sqrt((b**2)-(4*a*c)))/(2*a)
    await ctx.send(f"\n*The roots of this equation are* `x = {x1},{x2}`*. If you see a* `0j`*, it means you have real roots. Otherwise, your equation has complex roots*")
@quad.error
async def on_zero_error(ctx,error):
    if isinstance(error,commands.CommandInvokeError):
        await ctx.send("*Are you sure you aren't drunk or something?*")

@bot.command(aliases=["sum"])
async def add(ctx, *args):
    l = []
    for a in args:
        l.append(float(a))
    await ctx.send(sum(l))

@bot.command(aliases = ["prod","product"])
async def multi(ctx,*args):
    l = []
    for a in args:
        l.append(float(a))
    await ctx.send(math.prod(l))

@bot.command(aliases = ["eigenvalues","eigenvectors", "eigen"])
async def eig(ctx, m:int):
    l = []
    p = str(m)
    for i in p:
        l.append(float(i)) 
    o = np.asarray(l)
    o = o.reshape(3,3) 
    e,g = np.linalg.eig(o)
    await ctx.send(f"The eigenvalues of the given matrix are \n {e} \n\n The eigenvectors of the give matrix are \n {g}")


#Physics

@bot.command()
async def const(ctx,message:str):
    await ctx.send(constants[message])
@const.error
async def on_key_error(ctx,error):
    if isinstance(error,commands.CommandInvokeError):
        await ctx.send("Sorry. That is not in my directory. You can check the list of constants with the `oi constlist` command or if you are sure the constant you specified exists, you can inform my owner `Tesla#1045`")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = k)
    else:
        pass

def checkint(m):
    return m.content.isdigit()    
@bot.command()
async def constlist(ctx):
    embed = discord.Embed(title="Index of the shortforms of the constants",description="`1.`  G-Gravitational constant\n`2.`  c-speed of light in vacuum\n`3.`  Na-Avogadro constant\n`4.`  R-Gas constant\n`5.`  k-Boltzmann constant\n`6.`  sb-Stefan Boltzmann constant\n`7.`  b-Wien's displacement law constant\n`8.`  e-charge of electron/proton\n`9.`  me-mass of electron\n`10.`mp-mass of proton\n`11.`mn-mass of neutron\n`12.`mu0-Permeability of free space\n`13.`e0-Permittivity of vacuum\n`14.`F-Faraday constant\n`15.`h-Plank's constant\n`16.`Ry-Rydberg constant\n`17.`h0-Ground state of hygrogen atom\n`18.`a0-Bohr radius\nChoose a number to get its value",colour=0xff2052)
    masg = await ctx.send(embed=embed) 
    msg = await bot.wait_for('message', check=checkint)
    value = list(constants)[int(msg.content)-1] + " : " + str(list(list(constants.values())[int(msg.content)-1])[0]) + " " + str(list(list(constants.values())[int(msg.content)-1])[1])   
    await masg.delete()
    await ctx.send(value)

@bot.command()
async def fitsread(ctx):
    attachment = ctx.message.attachments[0]
    await attachment.save("FITS.fits")
    hdulist=fits.open("E:/Py-General/Discord_Bot/fits/FITS.fits")
    data=hdulist[0].data
    plt.imshow(data,cmap= plt.cm.viridis)
    plt.xlabel("x-pixels (RA)")
    plt.ylabel("y-pixels (Dec)")
    plt.colorbar()
    plt.savefig("E:/Py-General/Discord_Bot/fits/FITS.png")
    with open('E:/Py-General/Discord_Bot/fits/FITS.png', 'rb') as fp:
        await ctx.send(file=discord.File(fp, 'fits.png'))    


#moderation

@bot.command(aliases=['clr','purge'])
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit = amount + 1)
@clear.error
async def on_perm_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You are not permitted to do that action")



@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    guild = ctx.guild
    if role not in guild.roles:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Muted", permissions=perms)
        await member.add_roles(role)
        await ctx.send(f"🔨{member} was muted.")
    else:
        await member.add_roles(role) 
        await ctx.send(f"🔨{member} was muted.")     
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(embed=r) 
    elif isinstance(error, commands.BadArgument):
        await ctx.send("That is not a valid member")
    else:
        pass

@bot.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    await ctx.send(f"{member} has been unmuted")
@unmute.error
async def on_arg_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = k)


bot.run(TOKEN)

#Not in use
 
# @bot.command()
#async def forward(ctx,*, message: str):
#    channel = bot.get_channel(745664856845451295)
#    await channel.send(message)
#    await ctx.send(f"Succesfully sent the message")
#@forward.error
#async def on_mb_error(ctx,error):
#    if isinstance(error, commands.MissingRequiredArgument):
#        await ctx.send(embed = k)
#    elif isinstance(error,commands.BadArgument):
#        await ctx.send(embed=b1)
#    else:
#        pass
