import discord
from discord import app_commands
import discord.ext
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import json
import os
from subprocess import call
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, bot):
        self.bot = bot

    def on_modified(self, event):
        if not event.is_directory:
            command = self.bot.get_command("updated")
            if command is not None:
                callback = command.callback
                self.bot.loop.create_task(callback(command))

TOKEN = ''

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot Ready")
    try:
        await bot.tree.sync()
        print("Commands Synced!")
    except:
        print(Exception)

# Slash Command
@bot.tree.command(name="uwu", description="Do the uwu thing")
async def uwu(interaction: discord.Interaction):
    await interaction.response.send_message(f'UwU')

""" @bot.tree.command(name="thor", description="Shows what Thor is doing!")
async def thor(interaction: discord.Interaction):
    call(["python3", "thor.py"])
    file=discord.File('./thor/Thor.png')
    await interaction.response.send_message(file) """

# Server Commands
@bot.command()
async def server(ctx):
    os.system('ifconfig > ip.txt')
    file = open("ip.txt", "r")
    embed = discord.Embed(title="Server Communication Info", description=file.read(), colour=discord.Colour.random())
    file.close()
    os.system('rm ip.txt')
    await ctx.send(embed=embed)

@bot.command()
async def cpu(ctx):
    os.system('cpu > cpu.txt')
    file = open("cpu.txt", "r")
    embed = discord.Embed(title="Server CPU Usage", description=file.read(), colour=discord.Colour.random())
    file.close()
    os.system('rm cpu.txt')
    await ctx.send(embed=embed)

@bot.command()
@cooldown(1, 5, BucketType.user)
async def updated(ctx):
    channel = bot.get_channel(730260467733233777)  
    with open('db_copy.json', 'r') as db_data:
        contact_data = json.load(db_data)
    fname = contact_data["firstName"]
    lname = contact_data["lastName"]
    email = contact_data["email"]
    subject = contact_data["subject"]
    embed = discord.Embed(title="Database", colour=discord.Colour.random())
    embed.add_field(name="Name", value=fname, inline=False)
    embed.add_field(name="Last Name", value=lname, inline=False)
    embed.add_field(name="Email", value=email, inline=False)
    embed.add_field(name="Subject", value=subject, inline=False)
    await channel.send(embed=embed)



@bot.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    print(f'{username}: {user_message} ({channel})')

    if message.author == bot.user: 
        return

    if user_message == "hello":
        await message.channel.send(f'Hello {username}!! ')
        return
    elif user_message == 'bye':
        await message.channel.send(f'Goodbye {username}!!')
        return
    await bot.process_commands(message)





if __name__ == "__main__":
    event_handler = FileChangeHandler(bot)
    observer = Observer()
    observer.schedule(event_handler, path="./db_copy.json", recursive=True)
    observer.start()
    bot.run(TOKEN)

    """ try:
        bot.run(TOKEN)
    finally:
        observer.stop()
        observer.join() """
