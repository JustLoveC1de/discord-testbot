import jsmanager
import logging
import commands
import handler
from os.path import exists
from discord import *
# значения
prefix: str | None = None

# Базовая строка (Создание объекта с правами бота)
intents: Intents = Intents.default()
# Базовая строка №2 (Обеспечение права на написание и отправку сообщений)
intents.message_content = True
# Базовая строка №3 (Создание объекта самого бота)
bot: Client = Client(intents=intents)
# Инициализация команд

# Логика бота
@bot.event
async def on_ready():
    print(f'> Бот запущен! ({bot.user})')
@bot.event
async def on_message(message: Message):
    if bot.user == message.author:
        return
    print(f"> Ввод пользователя: {message.content}")
    if not message.content.startswith(prefix):
        return
    await commands.commandHandler(message.content.removeprefix(prefix), message)

def main() -> None:
    if not exists(jsmanager.FILE_PATH):
        print("> Создаём файл с настройками...")
        jsmanager.file_create()
    botinfo: dict[str] = jsmanager.file_read()
    if not jsmanager.check_keys(botinfo):
        handler.handle_critical('> В файле не указаны некоторые значения!')
    global prefix
    prefix = botinfo["prefix"]
    commands.init()
    try:
        bot.run(botinfo["token"])
    except LoginFailure:
        handler.handle_critical("> В файле указан некорректный токен!")
if __name__ == '__main__':
    main()