from discord.ext import commands
import json
import urbandictionary as ud
from shinden import get_first_page_search
import discord

with open('settings.json') as f:
    content = json.load(f)

api_key = content["api"]
prefix = content['prefix']

bot = commands.Bot(command_prefix = prefix)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    for guild in bot.guilds:
        print('Logged in ' + str(guild.name) +  ' (id: '+ str(guild.id) +')')
    members = ' - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    stream = discord.Streaming(name = 'Online', url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    await bot.change_presence(activity=stream)
    print("Ready")

@bot.command(name = 'urban', help='Responds with urban dictionary definition')
async def urban(ctx, word, which_result=1):
    defs = ud.define(word)
    try:
        definition = defs[which_result-1]
    except IndexError:
        await ctx.send("No result")
    
    response = '***' + definition.word + '***' + '\n\n`' + definition.definition + '\n\n' + definition.example + '`'
    await ctx.send(response)

@bot.command(name = 'urbanlist', help='Responds with urban dictionary definition list')
async def urbanlist(ctx, word):
    defs = ud.define(word)
    response = discord.Embed(title = word, type = 'rich', description = 'Results for maximum 10 first results from Urban Dictionary' )
    try:
        check = 0
        for i in range(10):
            result = defs[i]
            check = 1
            text = (result.definition[:75] + '...') if len(result.definition) > 75 else result.definition
            response.add_field(name = result.word, value = text, inline = False)
    except IndexError:
        if check == 0:
            await ctx.send("No results")
    await ctx.send(embed = response)

@bot.command(name='shinden', help = 'Shinden search results')
async def shinden(ctx, title, which_result = 1,anime_or_manga = 'anime'):
    if anime_or_manga == 'manga':
        anime_list = get_first_page_search(title, 'manga')
    else:
        anime_list = get_first_page_search(title)

    anime = anime_list[which_result-1]
    color = discord.Colour(16777215)
    response = discord.Embed(title = '***' + anime.title + '***', type = 'rich', description = 'Tags: ' + str(anime.tags), colour = color.teal(), url = anime.url)
    response.add_field(name = 'Score', value = anime.top_score)
    response.add_field(name = 'Episodes', value = anime.episodes)
    response.add_field(name = "Status", value = anime.status)
    await ctx.send(embed = response)

@bot.command(name='shindenlist')
async def shindenlist(ctx, title, anime_or_manga = 'anime'):
    if anime_or_manga == 'manga':
        anime_list = get_first_page_search(title, 'manga')
    else:
        anime_list = get_first_page_search(title)
    color = discord.Colour(16777215)
    response = discord.Embed(title= 'Shinden', type = 'rich', description = '***Search results for: ' + title + '***',colour = color.teal())
    counter = 1
    for anime in anime_list:
        response.add_field(name = str(counter) + '.', value = anime.title)
        counter = counter + 1
    await ctx.send(embed = response)

@bot.command(name = 'truth')
async def truth(ctx):
    response = discord.Embed(title = 'The truth')
    response.set_image(url = 'https://pbs.twimg.com/profile_images/1116994465464508418/E9UB9VPx.png')
    await ctx.send(embed = response)


bot.run(api_key)
