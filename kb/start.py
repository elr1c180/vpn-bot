from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

comm = InlineKeyboardBuilder()
comm.add(
    types.InlineKeyboardButton(
        text="Сообщество",
        url="https://t.me/elr1cs_work"
    )
)
comm.add(
    types.InlineKeyboardButton(
        text="Инструкция по установке",
        url="https://teletype.in/@elr1cs_work/install-vpn"
    )
)
comm.add(
    types.InlineKeyboardButton(
        text="Поддержать",
        callback_data="support_project"
    )
)

comm.adjust(1)