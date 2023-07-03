import discord
from discord.ext import commands
#import random


bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} запущен и готов к работе!')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    print(f'Получено сообщение! Text: {message.content}, Server: {message.guild}, Person: {message.author}')

@bot.slash_command(name='help', description='Выводит все команды и их краткое описание.')
async def helper(ctx):
    await ctx.delete()
    await ctx.send('[1]Выводит ')

@bot.slash_command(name='test', description='Выводит сообщение')
async def test(ctx):
    await ctx.delete()
    await ctx.send('Проверка пройдена')


token = 'MTEyNDg0MTMxMzQ5NDM2ODM4Ng.GzneNu.z-UBV2Zx7IuOAd3w9p_ZpysGs1SsdA3jWYtc6s'
bot.run(token)