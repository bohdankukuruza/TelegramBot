from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
 
import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет!\n Твой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}',
                        reply_markup=kb.main)

@router.message(Command('help'))
async def get_help(message: Message):
   await message.reply('это команда помощи /help', reply_markup=kb.settings)

@router.message(F.text == 'How are you?')
async def how_are_you(message: Message):
    await message.answer("I'm good, Thanks")
    