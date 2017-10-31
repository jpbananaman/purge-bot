import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import discord.utils

Client = Bot("!") #this defines the prefix of the command, i.e. "!clean 3"

def is_owner_check(message):
    return message.author.id == '##UserID Goes Here##'

def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))
	
@Client.command(pass_context = True)
async def clean(ctx, num):
	number = int(num) #Converting the amount of messages to delete to an integer
	counter = 0
	msg = ctx.message
	if is_owner_check(msg):
		async for x in Client.logs_from(ctx.message.channel, limit = number+1):
			await Client.delete_message(x)
			await Client.change_presence(game=discord.Game(name='Purged '+str(counter)+' of '+str(number))) #sets the bot's current game to the progress of the purge
			counter += 1
			await asyncio.sleep(0.5) #0.5 second timer so the deleting process can be even
		done_msg = await Client.send_message(ctx.message.channel,"Done purging.")
		done_msg
		await Client.change_presence(game=None)
		await asyncio.sleep(3.0)
		await Client.delete_message(done_msg)
	else: #if the user is not the owner, the bot deletes the invoking command and returns an error
		await Client.delete_message(msg)
		err_msg = await Client.send_message(ctx.message.channel,"You don't have the permissions to use that command.")
		err_msg
		await Client.change_presence(game=None)
		await asyncio.sleep(3.0)
		await Client.delete_message(err_msg)
	
	
		
	
			
Client.run("##enter your bot's user token##")
