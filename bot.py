import os
from dotenv import load_dotenv

load_dotenv()


import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

karty = {
    "Brązowe": [f"Brązowa karta {i+1}" for i in range(68)],
    "Srebrne": [f"Srebrna karta {i+1}" for i in range(116)],
    "Złote": [f"Złota karta {i+1}" for i in range(84)],
    "Mityczne": [f"Mityczna karta {i+1}" for i in range(31)],
    "Bohaterskie": [f"Bohaterska karta {i+1}" for i in range(11)],
}

tryby_gry = {
    "n": {
        "Brązowe": 48,
        "Srebrne": 30,
        "Złote": 13,
        "Mityczne": 4,
        "Bohaterskie": 1,
    },
    "%+": {
        "Brązowe": 28,
        "Srebrne": 21,
        "Złote": 24,
        "Mityczne": 15,
        "Bohaterskie": 9,
    }
}

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name}')

@bot.command()
async def losuj(ctx, liczba_kart: int = 5, tryb: str = "n"):
    tryb = tryb.lower()
    if tryb not in tryby_gry:
        await ctx.send("❌ Nieprawidłowy tryb. Wybierz `normalny` lub `alternatywny`.")
        return

    szanse = tryby_gry[tryb]
    typy = list(szanse.keys())
    wagi = list(szanse.values())

    wyniki = []
    for _ in range(liczba_kart):
        typ_karty = random.choices(typy, weights=wagi, k=1)[0]
        karta = random.choice(karty[typ_karty])
        wyniki.append(f"{typ_karty}: {karta}")

    await ctx.send("🎴 Wylosowane karty:\n" + "\n".join(wyniki))

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    print("❌ Nie znaleziono tokena!")
else:
    bot.run(TOKEN)

import os

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    print("❌ Nie znaleziono tokena!")
else:
    print("✅ Token znaleziony, uruchamiam bota...")
    bot.run(TOKEN)
