from aiogram import types, F, Router, flags, Dispatcher
from aiogram.types import Message
from aiogram.types.inline_query import InlineQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from aiogram.types import (
    CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message,
)
from aiogram.exceptions import TelegramBadRequest
import kb
import text
 
router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.first.format(name=msg.from_user.full_name), reply_markup=kb.generate_menu(level='0').as_markup())
    await msg.delete()
    
@router.callback_query(lambda callback: callback.data == "how_work_for_your")
async def your_handler(callback: CallbackQuery):
    await callback.message.answer(text.how_work_for_your_text, reply_markup=kb.generate_menu(level='1.1').as_markup())
    await callback.message.delete()
    
@router.callback_query(lambda callback: callback.data == "how_work_for_client")
async def your_handler(callback: CallbackQuery):
    await callback.message.answer('Как работает интерфейс', reply_markup=kb.generate_menu(level='1.2').as_markup())
    await callback.message.delete()
    
@router.callback_query(lambda callback: callback.data == "buy")
async def buy_handler(callback: CallbackQuery):
    await callback.message.answer('Выбери один тариф', reply_markup=kb.generate_menu(level='2.2').as_markup())
    await callback.message.delete()
    
@router.callback_query(lambda callback: callback.data == "tell_me")
async def show_me_handler(callback: CallbackQuery):
    await callback.message.answer(text.how_work_for_client_text, reply_markup=kb.generate_menu(level='2.1').as_markup())
    await callback.message.delete()
    
@router.callback_query(lambda callback: callback.data == "show_me")
async def show_me_handler(callback: CallbackQuery):
    await callback.message.answer('Показываю', reply_markup=kb.generate_menu(level='3.1').as_markup())
    await callback.message.delete()
    
@router.callback_query(lambda callback: callback.data == "tarif_1")
@router.callback_query(lambda callback: callback.data == "tarif_2")
@router.callback_query(lambda callback: callback.data == "tarif_3")
async def show_me_handler(callback: CallbackQuery):
    await callback.message.answer('Оферта', reply_markup=kb.generate_menu(level='3.2').as_markup())
    await callback.message.delete()
    
@router.callback_query(lambda callback: callback.data == "next_1")
async def show_me_handler(callback: CallbackQuery):
    await callback.message.answer('Вы точно осознаете, что мы возьмем ваши деньги и ничего не дадим в замен?', reply_markup=kb.generate_menu(level='4').as_markup())
    await callback.message.delete()
    
@router.callback_query(lambda callback: callback.data == "next_2")
async def show_me_handler(callback: CallbackQuery):
    await callback.message.answer('Модуль оплаты', reply_markup=kb.generate_menu(level='5').as_markup())
    await callback.message.delete()
    
@router.callback_query(lambda callback: callback.data == "menu")
async def menu(callback: CallbackQuery):
    await callback.message.answer(text.first, reply_markup=kb.menu)
    await callback.message.delete()
