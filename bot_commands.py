from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
import builder


router = Router()


@router.message(Command('start'))
async def start(message: Message):
    await message.reply(f'Здравствуйте, не хотите посетить наши греческие залы?', reply_markup=builder.build_enter_markup())


@router.message(F.text == 'Войти')
async def first(message: Message):
    await message.reply(f'Добро пожаловать в первый зал - гардероб! Пожалуйста, сдайте верхнюю одежду', reply_markup=builder.build_first_markup())


@router.message(F.text == 'Выйти')
async def first(message: Message):
    await message.reply(f'Всего доброго, не забудьте забрать верхнюю одежду в гардеробе!', reply_markup=builder.rmk)


@router.message(F.text == 'Первый зал')
async def first(message: Message):
    await message.reply(f'Добро пожаловать в первый зал - гардероб!', reply_markup=builder.build_first_markup())


@router.message(F.text == 'Второй зал')
async def first(message: Message):
    await message.reply(f'В данном зале представлено..', reply_markup=builder.build_second_markup())


@router.message(F.text == 'Третий зал')
async def first(message: Message):
    await message.reply(f'В данном зале представлено..', reply_markup=builder.build_third_markup())


@router.message(F.text == 'Четвёртый зал')
async def first(message: Message):
    await message.reply(f'В данном зале представлено..', reply_markup=builder.build_fourth_markup())