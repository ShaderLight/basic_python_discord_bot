# flop discord bot  ![GitHub](https://img.shields.io/github/license/shaderlight/flop_discord_bot) ![GitHub last commit](https://img.shields.io/github/last-commit/shaderlight/flop_discord_bot)


Basic bot using discord.py library

Has a few integrations, e.g. with Urban Dictionary or worldometers.info

## Requirements:
- aiofiles
- aiohttp
- discord.py
- shinden
- UrbanDictionary
- SQLAlchemy

## Usage:

- Run bot.py
- The program will generate settings.json and close itself
- Fill in settings.json with your discord api token, preffered language (currently only EN or PL) and prefix
- Run bot.py again
- Done (assuming you already added your app associated with the token to your guild)

For available commands, type *!help* in a text channel with the bot
