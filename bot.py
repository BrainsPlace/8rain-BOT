import discord
import asyncio
import time
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

with open('token.txt', 'r') as file:
    TOKEN = file.read()

client = MyClient()
client.run(TOKEN)