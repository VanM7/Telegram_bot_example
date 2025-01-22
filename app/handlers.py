from aiogram import F, Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет!\n Твой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}',
                        reply_markup=await kb.inline_cars())

@router.message(Command('help')) 
async def get_help(message: Message):
    await message.answer('Это команда /help')

@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('OK!')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'10 фото: {message.photo[-1].file_id}')

@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMWZ5EdKhqlps6lDFlkOAY3qEV_6RoAAnfpMRs3BYlINAAB_ql0ZelpAQADAgADeQADNgQ',
                               caption ='Это BMW M4')
