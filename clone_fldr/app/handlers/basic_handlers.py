from aiogram import types, Router, F
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Добро пожаловать TODO BOT!')

#TODO - написать обработчик /help - Отправляет два сообщения: 1. "Инструкция по использованию бота", 2. Инструкция