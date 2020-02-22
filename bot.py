import discord
from discord.ext import commands
import urbandictionary as ud
import shinden as sh

import json


with open('settings.json') as f:
    content = json.load(f)

api_key = content["api"]
prefix = content['prefix']

# Applying settings
bot = commands.Bot(command_prefix = prefix, help_command = None)

# Excuted when bot is connected and ready

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot)) # printing out the bot's nickname

    for guild in bot.guilds:
        print('Logged in ' + str(guild.name) +  ' (id: '+ str(guild.id) +')') # printing out server name, which bot is connected to

    members = ' - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}') # printing out a list of server members

    # Setting bot status to streaming (it's rickroll)
    stream = discord.Streaming(name = 'Online', url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    await bot.change_presence(activity=stream) 

    print("Ready")

# Urban Dictionary related commands

@bot.command(name = 'urban', help='Responds with urban dictionary definition', category = 'Urban Dictionary')
async def urban(ctx, word, which_result=1):
    word = str(word) # Checking if word is a string
    defs = ud.define(word) # Using UrbanDictionary library to search for Urban Dictionary definitions
    try:
        definition = defs[which_result-1] # Selecting one result, based on which_result parameter (first result by default)
    except IndexError:
        await ctx.send("**No result**") # If index is out of range, then prints out that there was no result found
    
    response = '***' + definition.word + '***' + '\n\n`' + definition.definition + '\n\n' + definition.example + '`' # Reponse with some discord formatting for a nicer look
    await ctx.send(response)


@bot.command(name = 'urbanlist', help='Responds with urban dictionary definition list')
async def urbanlist(ctx, word): # This function responds with every definition found on UD (maximum result count is 10 and maximum word count for every definition is 75, urban command does not have that restriction)
    word = str(word)
    defs = ud.define(word)
    response = discord.Embed(title = word, type = 'rich', description = 'Results for maximum 10 first results from Urban Dictionary' )
    try:
        check = 0 # This variable checks if there was at least one successful iteration
        for i in range(10):
            result = defs[i]
            check = 1 
            text = (result.definition[:75] + '...') if len(result.definition) > 75 else result.definition # This line checks if the word count of the definition is over 75, if true, then cuts it and adds '...'
            response.add_field(name = result.word, value = text, inline = False)
    except IndexError:
        if check == 0: # If there wasnt any correct iteration, then bot responds with No result message
            await ctx.send("No results")
    await ctx.send(embed = response)


@bot.command(name = 'urbanrandom', help = 'Returns random Urban Dictionary definition')
async def urbanrandom(ctx):
    definition = ud.random()[0] # selecting first definition from the list of random definitions
    response = '***' + definition.word + '***' + '\n\n`' + definition.definition + '\n\n' + definition.example + '`'

    await ctx.send(response)

# Shinden related commands

@bot.command(name='shindenanime', help = 'Returns an anime from shinden.pl')
async def shindenanime(ctx, title, which_result = 1):
    try: # Checking the correctness of parameters
        title = str(title)
        which_result = int(which_result)
    except:
        return await ctx.send("**wrong parameters**")

    anime_list = sh.search_titles(title)

    anime = anime_list[which_result-1] # Selecting one anime result from the list of all found results
    color = discord.Colour(16777215)

    # Creating a discord embed message object and adding fields with information
    response = discord.Embed(title = '***' + anime.title + '***', type = 'rich', description = 'Tags: ' + str(anime.tags), colour = color.teal(), url = anime.url) 
    response.add_field(name = 'Score', value = anime.top_score)
    response.add_field(name = 'Episodes', value = anime.episodes)
    response.add_field(name = "Status", value = anime.status)

    await ctx.send(embed = response)


@bot.command(name='shindenmanga', help = 'Returns an anime or manga from shinden.pl')
async def shindenmanga(ctx, title, which_result = 1):
    try:
        title = str(title)
        which_result = int(which_result)
    except:
        return await ctx.send('**Wrong parameters**')

    manga_list = sh.search_titles(title, anime_or_manga = 'manga')
    manga = manga_list[which_result-1]
    color = discord.Colour(16777215)

    response = discord.Embed(title = '***' + manga.title + '***', type = 'rich', description = 'Tags: ' + str(manga.tags), colour = color.teal(), url = manga.url)
    response.add_field(name = 'Score', value = manga.top_score)
    response.add_field(name = 'Chapters', value = manga.episodes)
    response.add_field(name = 'Status', value = manga.status)

    await ctx.send(embed = response)


@bot.command(name='shindenanimelist', help = 'Returns a list of anime from shinden.pl')
async def shindenanimelist(ctx, title):
    title = str(title)

    anime_list = sh.search_titles(title)
    color = discord.Colour(16777215)

    response = discord.Embed(title= 'Shinden', type = 'rich', description = '***Search results for: ' + title + '***', colour = color.teal())
    
    counter = 1
    for anime in anime_list:
        response.add_field(name = str(counter) + '.', value = anime.title) # Counter variable helps with returning many anime titles in a row (1. 2. 3. etc)
        counter = counter + 1

    await ctx.send(embed = response)


@bot.command(name='shindenmangalist', help = 'Returns a list of manga results')
async def shindenmangalist(ctx, title):
    title = str(title)

    manga_list = sh.search_titles(title, anime_or_manga = 'manga')
    color = discord.Colour(16777215)

    response = discord.Embed(title= 'Shinden', type = 'rich', description = '***Search results for: ' + title + '***', colour = color.teal())
    
    counter = 1
    for anime in manga_list:
        response.add_field(name = str(counter) + '.', value = anime.title)
        counter = counter + 1
        
    await ctx.send(embed = response)


@bot.command(name = 'shindencharacter')
async def shindencharacter(ctx, keyword, which_result = 1):
    try:
        keyword = str(keyword)
        which_result = int(which_result)
    except:
        await ctx.send("**Wrong parameters**")
    
    character_list = sh.search_characters(keyword)
    character = character_list[which_result-1]
    color = discord.Colour(16777215)

    response = discord.Embed(title = '***' + character.name + '***', type = 'rich', description = '`' + character.description + '`', colour = color.dark_gold(), url = character.url)

    response.add_field(name = 'Gender', value = character.gender)
    response.add_field(name = 'Is historical', value = character.is_historical)
    response.add_field(name = 'Appearance list', value = (', '.join(character.appearance_list)), inline = False) 

    await ctx.send(embed = response)


@bot.command(name = 'shindencharacterlist')
async def shindencharacterlist(ctx, keyword):
    keyword = str(keyword)

    character_list = sh.search_characters(keyword)
    color = discord.Colour(16777215)

    response = discord.Embed(title = '***Shinden characters***', type = 'rich', description = 'Search results for: ***' + keyword + '***', colour = color.green())

    counter = 1
    for ch in character_list:
        
        info = '**Appears in:** '
        for appear in ch.appearance_list:
            info = info + str(appear) + ', '
        
        response.add_field(name = '`' + str(counter) + '. ' + ch.name + '`', value = info[:-2], inline = False)
        counter = counter + 1
    await ctx.send(embed = response)


@bot.command(name = 'shindenuserlist')
async def shindenuserlist(ctx, keyword, search_type = 'contains'):
    keyword = str(keyword)
    user_list = sh.search_users(keyword, search_type)
    color = discord.Colour(16777215)
    response = discord.Embed(title = '***Shinden users***', type = 'rich', description = 'Search results for: ***' + keyword + '***', colour = color.purple()) 
    
    counter = 1
    for user in user_list: # Formatting the data using datatime's strftime method
        info = '**Last seen:** ' + user.last_seen.strftime('%H:%M %d.%m.%Y') + '\n' + '**Hours watched: **' + str(int(user.anime_minutes_watched/60))

        response.add_field(name = '`' + str(counter) + '.' + user.nickname + '`', value = info, inline = False)
        counter = counter + 1
    
    await ctx.send(embed = response)

# Other commands

@bot.command(name = 'truth') # This basically responds with dino earth image and nothing else
async def truth(ctx):
    response = discord.Embed(title = 'The truth')
    response.set_image(url = 'https://pbs.twimg.com/profile_images/1116994465464508418/E9UB9VPx.png')

    await ctx.send(embed = response)


# Finally running the bot with our api key from settings.json
bot.run(api_key)