# Модуль для команд.
import discord
import random
from os.path import join
from filemanager import filelist
IMAGE_DIR: str = 'icons'


class TextCommand:
    description: str = ''
    name: str = ''
    flags: set = {}
    def run(self, message: discord.Message) -> dict:
        return {}
    def toString(self) -> str:
        return f'- «{self.name}» - {self.description}'

IMPLEMENTED_COMMANDS: list[TextCommand] = []

class HelpCommand(TextCommand):
    description: str = 'выводит информацию о всех текстовых командах.'
    name: str = 'помощь'
    def run(self, message: discord.Message) -> dict:
       return {"content":"\n".join(map(lambda c: c.toString(), IMPLEMENTED_COMMANDS))}

class TestImageCommand(TextCommand):
    description: str = 'отправляет в канал случайную картиночку'
    name: str = 'случКартиночка'
    def run(self, message: discord.Message) -> dict:
       return {"file": discord.File(join(IMAGE_DIR, random.choice(filelist(IMAGE_DIR))))}



def init() -> None:
    for commandClass in TextCommand.__subclasses__():
        IMPLEMENTED_COMMANDS.append(commandClass())

async def commandHandler(cmd: str, context: discord.Message) -> dict:
    for command in IMPLEMENTED_COMMANDS:
        if command.name == cmd:
            output: dict = command.run(context)
            await context.channel.send(**output)