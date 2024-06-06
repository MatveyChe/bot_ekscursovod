from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove


def build_enter_markup():
    builder = ReplyKeyboardBuilder()

    builder.button(text='Войти')

    builder.adjust(1)

    return builder.as_markup(resize=True)


def build_first_markup():
    builder = ReplyKeyboardBuilder()

    builder.button(text='Второй зал')
    builder.button(text='Выйти')

    builder.adjust(1, 1)

    return builder.as_markup(resize=True)


def build_second_markup():
    builder = ReplyKeyboardBuilder()

    builder.button(text='Третий зал')

    builder.adjust(1)

    return builder.as_markup(resize=True)


def build_third_markup():
    builder = ReplyKeyboardBuilder()

    builder.button(text='Четвёртый зал')
    builder.button(text='Первый зал')

    builder.adjust(1, 1)

    return builder.as_markup(resize=True)


def build_fourth_markup():
    builder = ReplyKeyboardBuilder()

    builder.button(text='Первый зал')

    builder.adjust(1)

    return builder.as_markup(resize=True)


rmk = ReplyKeyboardRemove()