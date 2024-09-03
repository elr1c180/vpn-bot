from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from kb import start

router = Router() 

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"<b>Здравствуйте, {message.from_user.first_name}!</b>\nДля доступа к VPN перейдите в WebApp",
        parse_mode='html',
        reply_markup=start.comm.as_markup()
    )

@router.callback_query(F.data == 'start')
async def cmd_start(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        f"<b>Здравствуйте, {callback.from_user.first_name}!</b>\nДля доступа к VPN перейдите в WebApp",
        parse_mode='html',
        reply_markup=start.comm.as_markup()
    )
