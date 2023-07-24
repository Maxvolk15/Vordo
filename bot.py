import discord
from discord import Option
from discord.ext import commands
import asyncio
#import random


bot = commands.Bot(command_prefix='>', intents=discord.Intents.all()) #Хз что даёт(права бота), убирает ошибку

@bot.event
async def on_ready():
    print(f'{bot.user.name} запущен и готов к работе!')

@bot.event #Создаёт событие бота(действие)
async def on_message(message):
    if message.author.bot:
        return
    print(f'Получено сообщение! Text: {message.content}, Server: {message.guild}, Person: {message.author}')

@bot.slash_command(name='help', description='Выводит все команды и их краткое описание.') #Комнады на /
async def helper(ctx): #Сама команда
    await ctx.delete()
    await ctx.send('[/]...') #Отправляет в канал сообщение

#Дальше идут тесты----------------------------------------------------------------------------|
@bot.slash_command(name='test', description='Выводит сообщение')
async def test(ctx):
    await ctx.defer() #Позволяет ждать ответа от бота, не выдавая ошибку
    await asyncio.sleep(3) #Время сна (сек)
    await ctx.delete() #Удаляет сообщение(команду)
    await ctx.send('Проверка пройдена!')
    await ctx.respond('Да') #Отвечает на сообщение


#required - обязательно указывать или нет
#default - стандартное значение аргумента, если он не был указан
@bot.slash_command(name='test2')
async def test2(
    ctx,
    number: Option(int, description='Кол-во чемпов от 1 до 10', required=True, min_value=1, max_value=10)
    #member:  Option(discord.Member,  description='Любой участник сервера',       required=True),
    #choice:  Option(str,             description='Выберите пункт из списка',     required=True,  choices=['Банан', 'Яблоко', 'Апельсин']),
    #text:    Option(str,             description='Текст из нескольких слов',     required=False, default=''),
    #boolean: Option(bool,            description='True или False',               required=False, default=False)
    ):
    await ctx.delete()

class CustomBoolArgType(commands.Converter):
    choices = ('Да', 'Нет')
    async def convert(cls, ctx, arg): #cls — объект этого класса\ctx — контекст выполнения команды\arg — значение аргумента
        return arg == 'Да'
@bot.slash_command(name='test3')
async def test3(ctx, arg: Option(CustomBoolArgType, choices=CustomBoolArgType.choices)):
    await ctx.respond(f'{arg}, {type(arg).__name__}')

'''
class IntFromStrArgType(commands.Converter):
    values = ('Два', 'Один', 'Три')

    async def convert(cls, ctx, arg):
        try:
            return cls.values.index(arg) + 1
        except ValueError:
            return -1

@bot.slash_command()
async def test4(ctx, arg: Option(IntFromStrArgType)):
    await ctx.respond(f'{arg}, {type(arg).__name__}')
'''

#Тесты закончены------------------------------------------------------------------------------|

token = 'MTEyNDg0MTMxMzQ5NDM2ODM4Ng.GRBY2a.5hzPKBC43huTEqIVK-m6GgfXcwsEdZKYZDfzmY'
bot.run(token) #Запускает бота с настройками, ВСЕГДА В КОНЦЕ КОДА