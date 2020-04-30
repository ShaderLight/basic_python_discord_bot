import discord
from discord.ext import commands
import urbandictionary as ud
import shinden as sh

import json
import logging
import sys
from datetime import datetime, timedelta

import timer
import covid19
import languages

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S', level=logging.INFO)

cv = covid19.Covid_data()
t = timer.Timer()


# On the first execution, there will be no settings.json, so we will create one
try:
    with open('settings.json', 'r') as f:
        content = json.load(f)

    api_key = content['api']
    prefix = content['prefix']
    starting_language = content['language']
except:
    logging.warning("Proper settings.json file wasn't found, creating a default one")
    default_settings = {'api': 'your_api_token', 'prefix': '!', 'language':'EN'}
    
    with open('settings.json', 'w') as f:
        json.dump(default_settings, f, indent=4)

    # After creating the settings file, code execution will stop, so the user can enter discord api token and run the code again
    logging.debug('Program will now shutdown, please apply settings in settings.json')
    sys.exit()



# Applying prefix
bot = commands.Bot(command_prefix=prefix, help_command=None)

# Applying language
lg = languages.Language(starting_language)

logging.debug('Bot ready to connect with prefix {} and language {}'.format(prefix, starting_language))

# Excuted when bot is connected and ready
@bot.event
async def on_ready():
    logging.info('We have logged in as {0.user}'.format(bot)) # Logging the bot's nickname

    for guild in bot.guilds:
        logging.debug('Logged in ' + str(guild.name) +  ' (id: '+ str(guild.id) +')') # Printing out server name, which the bot is connected to

    members = ' - '.join([member.name for member in guild.members])
    logging.debug(f'Guild Members:\n - {members}') # Logging a list of server members

    # Setting bot status to streaming (Never gonna give you up)
    stream = discord.Streaming(name=prefix + 'helperino', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    await bot.change_presence(activity=stream) 

    logging.info("------ | Ready | ------")


# Help command
@bot.command(name='help', aliases=['helperino'], help='Lists available commands')
async def help(ctx):
    color = discord.Colour(16777215)
    response = discord.Embed(title='***Flop***', type='rich', description=lg.help[1].format(prefix), colour = color.dark_magenta(), url = 'https://github.com/ShaderLight/flop_discord_bot')
    response.add_field(name=lg.help[2].format(prefix), value=lg.help[3], inline=False)
    response.add_field(name=lg.help[4].format(prefix), value=lg.help[5], inline=False)
    response.add_field(name=lg.help[6].format(prefix), value=lg.help[7], inline=False)
    response.add_field(name=lg.help[8].format(prefix), value=lg.help[9], inline=False)
    response.add_field(name=lg.help[10].format(prefix), value=lg.help[11], inline = False)
    response.add_field(name=lg.help[12].format(prefix), value=lg.help[13], inline = False)
    response.add_field(name=lg.help[14].format(prefix), value=lg.help[15], inline = False)
    response.add_field(name=lg.help[16].format(prefix), value=lg.help[17], inline=False)
    response.add_field(name=lg.help[18].format(prefix), value=lg.help[19], inline=False)
    response.add_field(name=lg.help[20].format(prefix), value=lg.help[21], inline=False)
    response.add_field(name=lg.help[22].format(prefix), value=lg.help[23], inline=False)
    response.add_field(name=lg.help[24].format(prefix), value=lg.help[25], inline=False)


    await ctx.send(embed=response)


# Language command
@bot.command(name='language', aliases=['lang'])
async def language(ctx, *args):
    logging.debug('Executing command {}language'.format(prefix))

    if len(args) != 1:
<<<<<<< Updated upstream
        help_string = ('**Command:** language\n'
            '**Description:** Changes language\n'
            '**Aliases:** `lang`\n'
            '**Usage:** `{}language (desired_language)`\n'
            '**Parameters:** \n'
            '\t*desired_language* (str, currently only EN or PL)\n'.format(prefix))
=======
        help_string = (lg.language[0].format(prefix))
>>>>>>> Stashed changes
        return await ctx.send(help_string)

    desired_language = ''.join(args)
    desired_language = desired_language.upper()

    if desired_language == lg.lang_set:
<<<<<<< Updated upstream
        return await ctx.send('***Desired language has already been set***')
=======
        return await ctx.send(lg.language[2])
>>>>>>> Stashed changes
    
    try:
        lg.update(desired_language)
    except languages.LanguageNotSupportedError:
<<<<<<< Updated upstream
        return await ctx.send('***Wrong or not supported language***')

    await ctx.send('***Language changed to*** `{}`'.format(lg.lang_set))
=======
        return await ctx.send(lg.language[1])

    await ctx.send(lg.language[3].format(lg.lang_set))
>>>>>>> Stashed changes


 
# Urban Dictionary related commands



@bot.command(name='urban', aliases=['u','ud'], help='Responds with urban dictionary definition')
async def urban(ctx, *args):
    logging.debug('Executing command {}urban'.format(prefix))

    if args == (): # If no arguments were passed, then respond with help message
        help_string = (lg.urban[0].format(prefix))
        return await ctx.send(help_string)

    if len(args) >= 2:
        args_list = list(args)
        which_result = 1
        possible_int = args_list.pop()

        try:
            which_result = int(possible_int)
        
        except:
            args_list.append(possible_int)
        
        words = ' '.join(args_list)
        
        defs = ud.define(words) # Using UrbanDictionary library to search for Urban Dictionary definitions
        try:
            definition = defs[which_result-1] # Selecting one result, based on which_result parameter (first result by default)
        except IndexError:
<<<<<<< Updated upstream
            await ctx.send("***No result***") # If index is out of range, then prints out that there was no result found
=======
            await ctx.send(lg.urban[1]) # If index is out of range, then prints out that there was no result found
>>>>>>> Stashed changes
    
        response = lg.urban[2].format(definition) # Reponse with some discord formatting for a nicer look
        await ctx.send(response)

    else:
        words = ' '.join(args)

        defs = ud.define(words) # Using UrbanDictionary library to search for Urban Dictionary definitions
        try:
            definition = defs[0]
        except IndexError:
<<<<<<< Updated upstream
            await ctx.send("***No result***") # If index is out of range, then prints out that there was no result found
=======
            await ctx.send(lg.urban[1]) # If index is out of range, then prints out that there was no result found
>>>>>>> Stashed changes
    
        response = lg.urban[2].format(definition) # Reponse with some discord formatting for a nicer look
        await ctx.send(response)



@bot.command(name='urbanlist', aliases=['ul','udlist','udl', 'ulist'], help='Responds with urban dictionary definition list')
async def urbanlist(ctx, *args): # This function responds with every definition found on UD (maximum result count is 10 and maximum word count for every definition is 75, urban command does not have that restriction)
    logging.debug('Executing command {}urbanlist'.format(prefix))
    
    if args == ():
<<<<<<< Updated upstream
        help_string = ('**Command:** urbanlist\n'
            '**Description:** Responds with urban dictionary definition list.\n'
            '**Aliases:** `ul, udlist, udl, ulist`\n'
            '**Usage:** `{}urbanlist (word)`\n'
            '**Parameters:** \n'
            '\t*word* (str)'.format(prefix))
=======
        help_string = (lg.urbanlist[0].format(prefix))
>>>>>>> Stashed changes

        return await ctx.send(help_string)
    
    try:
        t.start()
    except timer.TimerAlreadyRunning:
        t.stop()
        t.start()

    words = ' '.join(args)

    defs = ud.define(words)
    response = discord.Embed(title=words, type='rich', description='Results for maximum 10 first results from Urban Dictionary' )
    try:
        check = 0 # This variable checks if there was at least one successful iteration
        for i in range(10):
            result = defs[i]
            check = 1 
            text = (result.definition[:75] + '...') if len(result.definition) > 75 else result.definition # This line checks if the word count of the definition is over 75, if true, then cuts it and adds '...'
            response.add_field(name=result.word, value=text, inline=False)
    except IndexError:
        if check == 0: # If there wasnt any correct iteration, then bot responds with No result message
            t.stop()
<<<<<<< Updated upstream
            return await ctx.send("***No results***")
=======
            return await ctx.send(lg.urbanlist[0])
>>>>>>> Stashed changes
    
    execution_time = str(t.stop())
    response.set_footer(text=lg.urbanlist[1].format(execution_time[:5]))

    await ctx.send(embed=response)



@bot.command(name='urbanrandom', aliases=['ur', 'udrandom', 'udr', 'urandom'], help='Returns random Urban Dictionary definition')
async def urbanrandom(ctx):
    logging.debug('Executing command {}urbanrandom'.format(prefix))

    definition = ud.random()[0]  # selecting first definition from the list of random definitions
    response = '***{0.word}***\n\n`{0.definition}\n\n{0.example}`'.format(definition)

    await ctx.send(response)



# Shinden related commands



@bot.command(name='shindenanime', aliases=['sa', 'shindena', 'sha', 'sanime', 'shanime'], help='Returns an anime from shinden.pl')
async def shindenanime(ctx, *args):
    logging.debug('Executing command {}shindenanime'.format(prefix))

    if args == ():
        help_string = (lg.s_anime[0].format(prefix))
        return await ctx.send(help_string)
    
    try:
        t.start()
    except timer.TimerAlreadyRunning:
        t.stop()
        t.start()

    if len(args) >= 2:
        args_list = list(args)
        which_result = 1
        possible_int = args_list.pop()

        try:
            which_result = int(possible_int)
        except:
            args_list.append(possible_int)
        
        title = ' '.join(args_list)

        anime_list = sh.search_titles(title)

        try:
            anime = anime_list[which_result-1] # Selecting one anime result from the list of all found results
        except TypeError:
            t.stop()
<<<<<<< Updated upstream
            return await ctx.send('***No results***')
        except IndexError:
            await ctx.send('**which_result param was too big, showing last result**')
=======
            return await ctx.send(lg.s_anime[1])
        except IndexError:
            await ctx.send(lg.s_anime[2])
>>>>>>> Stashed changes
            anime = anime_list[-1]

        color = discord.Colour(16777215)

        # Creating a discord embed message object and adding fields with information
        response = discord.Embed(title='***{0.title}***'.format(anime), type='rich', description=lg.s_anime[3] + str(anime.tags), colour=color.teal(), url=anime.url) 
        response.add_field(name=lg.s_anime[4], value=anime.top_score)
        response.add_field(name=lg.s_anime[5], value=anime.episodes)
        response.add_field(name=lg.s_anime[6], value=anime.status)

        execution_time = round(t.stop(), 3)
        response.set_footer(text=lg.s_anime[7].format(execution_time))

        await ctx.send(embed=response)

    else:
        title = ' '.join(args)
        anime_list = sh.search_titles(title)

        try:
            anime = anime_list[0] # Selecting one anime result from the list of all found results
        except TypeError:
            t.stop()
<<<<<<< Updated upstream
            return await ctx.send('***No results***')
=======
            return await ctx.send(lg.s_anime[1])
>>>>>>> Stashed changes

        color = discord.Colour(16777215)

        # Creating a discord embed message object and adding fields with information
        response = discord.Embed(title='***{0.title}***'.format(anime), type='rich', description=lg.s_anime[3] + str(anime.tags), colour=color.teal(), url=anime.url) 
        response.add_field(name=lg.s_anime[4], value=anime.top_score)
        response.add_field(name=lg.s_anime[5], value=anime.episodes)
        response.add_field(name=lg.s_anime[6], value=anime.status)

        execution_time = round(t.stop(), 3)
        response.set_footer(text=lg.s_anime[7].format(execution_time))

        await ctx.send(embed=response)



@bot.command(name='shindenmanga', aliases=['sm', 'shindenm', 'shm','smanga', 'shmanga'], help='Returns a manga from shinden.pl')
async def shindenmanga(ctx, *args):
    logging.debug('Executing command {}shindenmanga'.format(prefix))

    if args == ():
        help_string = (lg.s_manga[0].format(prefix))
        return await ctx.send(help_string)

    try:
        t.start()
    except timer.TimerAlreadyRunning:
        t.stop()
        t.start()

    if len(args) >= 2:
        args_list = list(args)
        which_result = 1
        possible_int = args_list.pop()

        try:
            which_result = int(possible_int)
        except:
            args_list.append(possible_int)

        title = ' '.join(args_list)

        manga_list = sh.search_titles(title, anime_or_manga='manga')

        try:
            manga = manga_list[which_result-1]
        except TypeError:
            t.stop()
<<<<<<< Updated upstream
            return await ctx.send('***No results***')
        except IndexError:
            await ctx.send('*which_result param was too big, showing last result*')
=======
            return await ctx.send(lg.s_manga[1])
        except IndexError:
            await ctx.send(lg.s_manga[2])
>>>>>>> Stashed changes
            manga = manga_list[-1]

        color = discord.Colour(16777215)

        response = discord.Embed(title='***{0.title}***'.format(manga), type='rich', description=lg.s_manga[3] + str(manga.tags), colour=color.teal(), url=manga.url)
        response.add_field(name=lg.s_manga[4], value=manga.top_score)
        response.add_field(name=lg.s_manga[5], value=manga.episodes)
        response.add_field(name=lg.s_manga[6], value=manga.status)

        execution_time = round(t.stop(), 3)
        response.set_footer(text=lg.s_manga[7].format(execution_time))

        
        await ctx.send(embed=response)

    else:

        title = ' '.join(args)

        manga_list = sh.search_titles(title, anime_or_manga='manga')

        try:
            manga = manga_list[0]
        except TypeError:
            t.stop()
<<<<<<< Updated upstream
            return await ctx.send('***No results***')
=======
            return await ctx.send(lg.s_manga[1])
        except IndexError:
            await ctx.send(lg.s_manga[2])
            manga = manga_list[-1]

>>>>>>> Stashed changes

        color = discord.Colour(16777215)

        response = discord.Embed(title='***{0.title}***'.format(manga), type='rich', description=lg.s_manga[3] + manga.tags, colour=color.teal(), url=manga.url)
        response.add_field(name=lg.s_manga[4], value=manga.top_score)
        response.add_field(name = lg.s_manga[5], value=manga.episodes)
        response.add_field(name=lg.s_manga[6], value=manga.status)
        
        execution_time = round(t.stop(), 3)
        response.set_footer(text=lg.s_manga[7].format(execution_time))

        
        await ctx.send(embed=response)



@bot.command(name='shindenanimelist', aliases=['sal', 'shindenal', 'shal', 'sanimelist', 'shanimelist'], help='Returns a list of anime from shinden.pl')
async def shindenanimelist(ctx, *args):
    logging.debug('Executing command {}shindenanimelist'.format(prefix))

    if args == ():
        help_string = (lg.s_animelist[0].format(prefix))
        return await ctx.send(help_string)

    try:
        t.start()
    except timer.TimerAlreadyRunning:
        t.stop()
        t.start()

    title = ' '.join(args)

    anime_list = sh.search_titles(title)
    if anime_list == None:
        t.stop()
<<<<<<< Updated upstream
        return await ctx.send('***No results***')
=======
        return await ctx.send(lg.s_animelist[1])
>>>>>>> Stashed changes

    color = discord.Colour(16777215)

    response = discord.Embed(title=lg.s_animelist[2], type='rich', description=lg.s_animelist[3].format(title), colour=color.teal())
    
    counter = 1
    for anime in anime_list:
        value_text = '[{0.title}]({0.url})'.format(anime)
        response.add_field(name=str(counter) + '.', value=value_text) # Counter variable helps with returning many anime titles in a row (1. 2. 3. etc)
        counter = counter + 1

    execution_time = round(t.stop(), 3)
    response.set_footer(text=lg.s_animelist[4].format(execution_time))


    await ctx.send(embed=response)



@bot.command(name='shindenmangalist', aliases=['sml', 'shindenml', 'shml', 'smangalist', 'shmangalist'], help='Returns a list of manga results')
async def shindenmangalist(ctx, *args):
    logging.debug('Executing command {}shindenmangalist'.format(prefix))

    try:
        t.start()
    except timer.TimerAlreadyRunning:
        t.stop()
        t.start()

    if args == ():
        help_string = (lg.s_mangalist[0].format(prefix))

        return await ctx.send(help_string)

    title = ' '.join(args)

    manga_list = sh.search_titles(title, anime_or_manga='manga')
    if manga_list == None:
        t.stop()
<<<<<<< Updated upstream
        return await ctx.send('***No results***')
=======
        return await ctx.send(lg.s_mangalist[1])
>>>>>>> Stashed changes
    color = discord.Colour(16777215)

    response = discord.Embed(title=lg.s_mangalist[2], type='rich', description=lg.s_mangalist[3].format(title), colour=color.teal())
    
    counter = 1
    for manga in manga_list:
        value_text = '[{0.title}]({0.url})'.format(manga)
        response.add_field(name=str(counter) + '.', value=value_text)
        counter = counter + 1

    execution_time = round(t.stop(), 3)
    response.set_footer(text=lg.s_mangalist[4].format(execution_time))


    await ctx.send(embed=response)



@bot.command(name='shindencharacter', aliases=['sc', 'shindenc', 'shc', 'scharacter', 'shcharacter', 'sch', 'shindench', 'shch'], help='Returns a character result from shinden.pl')
async def shindencharacter(ctx, *args):
    logging.debug('Executing command {}shindencharacter'.format(prefix))

    if args == ():
        help_string = (lg.s_character[0].format(prefix))

        return await ctx.send(help_string)

    try:
        t.start()
    except timer.TimerAlreadyRunning:
        t.stop()
        t.start()

    if len(args) >= 2:
        args_list = list(args)
        which_result = 1
        possible_int = args_list.pop()

        try:
            which_result = int(possible_int)
        except:
            args_list.append(possible_int)

        name = ' '.join(args_list)

        character_list = sh.search_characters(name)
        try:
            character = character_list[which_result-1]
        except TypeError:
            t.stop()
<<<<<<< Updated upstream
            return await ctx.send('***No results***')
        except IndexError:
            await ctx.send('*which_result param was too big, showing last result*')
=======
            return await ctx.send(lg.s_character[1])
        except IndexError:
            await ctx.send(lg.s_character[2])
>>>>>>> Stashed changes
            character = character_list[-1]

        color = discord.Colour(16777215)
        
        if len(character.description) > 2000: # Description of discord embed must be under 2048 characters
            desc = character.description[:2000] + '...'
        else:
            desc = character.description

        response = discord.Embed(title='***{0.name}***'.format(character), type='rich', description='`' + desc + '`', colour=color.dark_gold(), url=character.url)

        response.add_field(name=lg.s_character[3], value=character.gender)
        response.add_field(name=lg.s_character[4], value=character.is_historical)
        response.add_field(name=lg.s_character[5], value=(', '.join(character.appearance_list)), inline=False)

        execution_time = round(t.stop(), 3)
        response.set_footer(text=lg.s_character[6].format(execution_time))

        
        await ctx.send(embed=response)

    else:
        name = ' '.join(args)

        character_list = sh.search_characters(name)
        try:
            character = character_list[0]
        except TypeError:
            t.stop()
<<<<<<< Updated upstream
            return await ctx.send('***No result***')
=======
            return await ctx.send(lg.s_character[1])
        except IndexError:
            await ctx.send(lg.s_character[2])
            character = character_list[-1]
>>>>>>> Stashed changes
        
        color = discord.Colour(16777215)

        response = discord.Embed(title='***{0.name}***'.format(character), type='rich', description='`{0.description}`'.format(character), colour=color.dark_gold(), url=character.url)

        response.add_field(name=lg.s_character[3], value=character.gender)
        response.add_field(name=lg.s_character[4], value=character.is_historical)
        response.add_field(name=lg.s_character[5], value=(', '.join(character.appearance_list)), inline=False)

        execution_time = round(t.stop(), 3)
        response.set_footer(text=lg.s_character[6].format(execution_time))

        
        await ctx.send(embed=response)



@bot.command(name='shindencharacterlist', aliases=['scl', 'shindencl', 'shcl', 'scharacterlist', 'shcharacterlist', 'schl', 'shindenchl', 'shchl'], help='Responds with a list of character results')
async def shindencharacterlist(ctx, *args):
    logging.debug('Executing command {}shindencharacterlist'.format(prefix))

    if args == ():
        help_string = (lg.s_characterlist[0].format(prefix))
        return await ctx.send(help_string)

    try:
        t.start()
    except timer.TimerAlreadyRunning:
        t.stop()
        t.start()

    name = ' '.join(args)

    character_list = sh.search_characters(name, get_description=False)
    if character_list == None:
        t.stop()
<<<<<<< Updated upstream
        return await ctx.send('***No results***')

    color = discord.Colour(16777215)
    response = discord.Embed(title='***Shinden character list***', type='rich', description='Search results for: **{}**'.format(name), colour=color.green())
=======
        return await ctx.send(lg.s_characterlist[1])

    color = discord.Colour(16777215)
    response = discord.Embed(title=lg.s_characterlist[2], type='rich', description=lg.s_characterlist[3].format(name), colour=color.green())
>>>>>>> Stashed changes

    counter = 1
    for character in character_list:
        
        info = lg.s_characterlist[4].format(character)
        for appear in character.appearance_list:
            info = info + str(appear) + ', '
        
        response.add_field(name='`{0}. {1.name}`'.format(counter, character), value=info[:-2], inline=False)
        counter = counter + 1
    
    execution_time = round(t.stop(), 3)
    response.set_footer(text=lg.s_characterlist[5].format(execution_time))


    await ctx.send(embed=response)



@bot.command(name='shindenuser', aliases=['su', 'shindenu', 'shu', 'suser', 'shuser'], help='Searches for a shinden user')
async def shindenuser(ctx, *args):
    logging.debug('Executing command {}shindenuser'.format(prefix))

    if args == ():
        help_string = (lg.s_user[0].format(prefix))

        return await ctx.send(help_string)

    try:
        t.start()
    except timer.TimerAlreadyRunning:
        t.stop()
        t.start()

    if len(args) >= 2:
        args_list = list(args)
        which_result = 1
        possible_int = args_list.pop()

        try:
            which_result = int(possible_int)
        except:
            args_list.append(possible_int)

        nickname = ' '.join(args_list)

        user_list = sh.search_users(nickname)
        try:
            user = user_list[which_result-1]
        except IndexError:
<<<<<<< Updated upstream
            await ctx.send('*which_result param too big, showing last result*')
            user = user_list[-1]
        except TypeError:
            t.stop()
            return await ctx.send('***No results***')
=======
            await ctx.send(lg.s_user[1])
            user = user_list[-1]
        except TypeError:
            t.stop()
            return await ctx.send(lg.s_user[2])
>>>>>>> Stashed changes

        color = discord.Colour(16777215)
        response = discord.Embed(title='**{0.nickname}**'.format(user), type='rich', colour=color.red(), url=user.url)
        
        response.add_field(name=lg.s_user[3], value='`{0.anime_titles_watched}`'.format(user))

        hours_watched = int(user.anime_minutes_watched/60)
        response.add_field(name=lg.s_user[4], value='`{}`'.format(hours_watched))

        response.add_field(name=lg.s_user[5], value='`{0.anime_episodes_watched}`'.format(user))
        response.add_field(name=lg.s_user[6], value='`{0.average_anime_ratings}`'.format(user))
        response.add_field(name=lg.s_user[7], value='`{0.achievement_count}`'.format(user))
        response.add_field(name=lg.s_user[8], value='`{0.points}`'.format(user))

        formatted_last_seen = user.last_seen.strftime('%H:%M %d.%m.%Y')
        response.add_field(name=lg.s_user[9], value='`{}`'.format(formatted_last_seen))
        
        execution_time = round(t.stop(), 3)
        response.set_footer(text=lg.s_user[10].format(execution_time))


        await ctx.send(embed=response)
    
    else:
        nickname = ' '.join(args)

        user_list = sh.search_users(nickname)
        try:
            user = user_list[0]
        except TypeError:
            t.stop()
<<<<<<< Updated upstream
            return await ctx.send('***No results***')
=======
            return await ctx.send(lg.s_user[1])
        except TypeError:
            t.stop()
            return await ctx.send(lg.s_user[2])
>>>>>>> Stashed changes

        color = discord.Colour(16777215)
        response = discord.Embed(title='**{0.nickname}**'.format(user), type='rich', colour=color.red(), url=user.url)
        
        response.add_field(name=lg.s_user[3], value='`{0.anime_titles_watched}`'.format(user))

        hours_watched = int(user.anime_minutes_watched/60)
        response.add_field(name=lg.s_user[4], value='`{}`'.format(hours_watched))

        response.add_field(name=lg.s_user[5], value='`{0.anime_episodes_watched}`'.format(user))
        response.add_field(name=lg.s_user[6], value='`{0.average_anime_ratings}`'.format(user))
        response.add_field(name=lg.s_user[7], value='`{0.achievement_count}`'.format(user))
        response.add_field(name=lg.s_user[8], value='`{0.points}`'.format(user))

        formatted_last_seen = user.last_seen.strftime('%H:%M %d.%m.%Y')
        response.add_field(name=lg.s_user[9], value='`{}`'.format(formatted_last_seen))
        
        execution_time = round(t.stop(), 3)
        response.set_footer(text=lg.s_user[10].format(execution_time))


        await ctx.send(embed=response)



@bot.command(name='shindenuserlist', aliases=['sul', 'shindenul', 'shul', 'suserlist', 'shuserlist'], help='Lists shinden users found')
async def shindenuserlist(ctx, *args):
    logging.debug('Executing command {}shindenuserlist'.format(prefix))

    if args == ():
        help_string = (lg.s_userlist[0].format(prefix))
        return await ctx.send(help_string)

    try:
        t.start()
    except timer.TimerAlreadyRunning:
        t.stop()
        t.start()

    nickname = ' '.join(args)

    user_list = sh.search_users(nickname, detailed_info=True)
    if user_list == None:
        t.stop()
<<<<<<< Updated upstream
        return await ctx.send('***No results***')
=======
        return await ctx.send(lg.s_userlist[1])
>>>>>>> Stashed changes

    color = discord.Colour(16777215)
    response = discord.Embed(title=lg.s_userlist[2] , type='rich', description=lg.s_userlist[3].format(nickname), colour=color.purple()) 
    
    counter = 1
    for user in user_list: # Formatting the data using datatime's strftime method
        profile_hyperlink = lg.s_userlist[4].format(user)
        formatted_last_seen = user.last_seen.strftime('%H:%M %d.%m.%Y')
        hours_watched = int(user.anime_minutes_watched/60)

        info = lg.s_userlist[5].format(formatted_last_seen, hours_watched, profile_hyperlink)

        response.add_field(name='`{0}. {1.nickname}`'.format(counter, user), value=info, inline=False)
        counter = counter + 1
    
    execution_time = str(t.stop())
    response.set_footer(text=lg.s_userlist[6].format(execution_time[:5]))


    await ctx.send(embed=response)



# Other commands



@bot.command(name='covid', aliases=['ncov', 'covid19', 'coronavirus'])
async def covid(ctx):
    logging.debug('Executing command {}covid'.format(prefix))

    if cv.when_last_update() == 'never':
        cv.update()
    elif (datetime.now() - cv.when_last_update()) > timedelta(hours=12): # if covid data hasnt been updated in 12 hours, then update (in order to minimalise requests sent)
        cv.update()
    
    data = cv.read_data()

    # Creating two separate embeds for world and poland respectively
    color = discord.Colour(16777215)
    world_embed = discord.Embed(title=lg.covid[0], type='rich', colour=color.red(), url='https://worldometers.info/coronavirus/')
    
    world_embed.add_field(name=lg.covid[2], value=data['world'].cases)
    world_embed.add_field(name=lg.covid[3], value=data['world'].deaths)
    world_embed.add_field(name=lg.covid[4], value=data['world'].recovered)

    poland_embed = discord.Embed(title=lg.covid[1], type='rich', colour=color.red(), url='https://worldometers.info/coronavirus/country/poland')
    
    poland_embed.add_field(name=lg.covid[2], value=data['poland'].cases)
    poland_embed.add_field(name=lg.covid[3], value=data['poland'].deaths)
    poland_embed.add_field(name=lg.covid[4], value=data['poland'].recovered)
    
    world_embed.set_footer(text=lg.covid[5])
    poland_embed.set_footer(text=lg.covid[5])

    await ctx.send(embed=world_embed)
    await ctx.send(embed=poland_embed)



@bot.command(name='truth', help='This basically responds with dino earth image and nothing else')
async def truth(ctx):
    logging.debug('Executing command {}truth'.format(prefix))

    response = discord.Embed(title='The truth')
    response.set_image(url='https://pbs.twimg.com/profile_images/1116994465464508418/E9UB9VPx.png')

    await ctx.send(embed=response)



# Finally running the bot with our api key from settings.json
bot.run(api_key)