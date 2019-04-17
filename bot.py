import discord
import asyncio
import time
import re
import sys
TOKEN = 'put your token in token.txt'
HELP = """
!timer {time in minutes}  ex: `!timer 30`
!timer {time in mminutes} {message}  ex: `!timer 30 @x1mk`

Make our bot better at `https://github.com/BrainsPlace/8rain-BOT`
        """
async def say_after(message, delay, what):
        await asyncio.sleep(int(delay)*60)
        await message.channel.send(what)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


    async def on_message(self, message):
        if message.author == self.user:
            return

        print('Message from {0.author}: {0.content}'.format(message))

        if(message.content.startswith('!help')):
            await message.channel.send(HELP)
        
        elif(message.content.startswith('!timer')):
            input = message.content.split()
            
            #basic timer
            if(len(input) == 2):
                print(input[1])
                await say_after(message, input[1], 'times up!')
                
            #timer tied to a user
            elif(len(input) == 3):
                await say_after(message, input[1], 'time is up! - ' + input[2])

        search = re.search('([0-9]+)\s(min|hour)', message.content)
        if search:
            print('regex found: ' + search.group())

            if 'min' in search.group(2):
                await say_after(message, search.group(1), 'time is up! -' + str(message.author.mention))

            elif 'hour' in search.group(2):
                await say_after(message, int(search.group(1))*60, 'time is up! -' + str(message.author.mention))


with open(sys.path[0] + '\\token.txt', 'r') as file:
    TOKEN = file.read().replace('\n','')

client = MyClient()
client.run(TOKEN)