import random
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    image = random.choice(images)
    with open(f'images/{image}', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f"\\U0001f642")

rady = ['Oszczędzaj wodę poprzez naprawę przecieków i używanie pryszniców z niskim zużyciem wody.',
'Recyklinguj wszystkie możliwe materiały, takie jak papier, szkło i plastik.',
'Korzystaj z reusable worków zakupowych zamiast jednorazowych plastikowych.',
'Unikaj plastikowych słomek i używaj słomek ze stali nierdzewnej lub szkła.',
'Wybieraj produkty organiczne i lokalne, aby zmniejszyć emisję gazów cieplarnianych z transportu.',
'Korzystaj z publicznego transportu, roweru lub chodzenia pieszo, zamiast korzystać z samochodu.',
'Ogranicz zużycie energii poprzez wyłączanie świateł i urządzeń elektrycznych, gdy nie są potrzebne.',
'Sadź więcej roślin, aby zwiększyć ilość tlenu w powietrzu i zatrzymać erozję gleby.',
'Unikaj jedzenia mięsa w co najmniej jeden dzień w tygodniu, aby zmniejszyć emisję gazów cieplarnianych.',
'Upowszechniaj świadomość ekologiczną poprzez edukację innych i zachęcanie do podejmowania proekologicznych działań.',
'Naprawiaj i ponownie wykorzystuj przedmioty, zanim zdecydujesz się na zakup nowych.',
'Ogranicz zużycie jednorazowych plastikowych butelek, wybierając butelki wielokrotnego użytku.',
'Wybieraj produkty o minimalnym opakowaniu, aby zmniejszyć ilość odpadów.',
'Używaj energooszczędnych urządzeń, aby zmniejszyć zużycie energii elektrycznej.',
'Zbieraj i segreguj odpady organiczne do kompostowania.',
'Wspieraj lokalne inicjatywy ekologiczne i organizacje pozarządowe.',
'Utrzymuj opony pojazdów odpowiednio napompowane, aby zmniejszyć zużycie paliwa.',
'Unikaj używania chemikaliów i pestycydów w ogrodach, aby chronić środowisko naturalne.',
'Popieraj zakładanie parków miejskich i terenów zielonych w swojej okolicy.',
'Bądź eko-świadomy przy zakupie elektroniki, wybierając produkty o niższym zużyciu energii i dłuższym czasie użytkowania.']

@bot.command()
async def ecorada(ctx):
    await ctx.send(random.choice(rady))
    
@bot.command()
async def ecomem(ctx):
    ecoimages = os.listdir('ecoimages')
    ecoimage = random.choice(ecoimages)
    with open(f'ecoimages/{ecoimage}', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
    
bot.run("MTE5OTQwMDAzMjU1NDcxNzI0NA.GTjNGk.cVmoUd-XU0NWe0PDSn2FnD_k8v9K6pXMyk-_Ik")