from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder
import json

def generate_menu(level:str):
    
    with open(r'C:\Users\egor2\Desktop\bot_pre\core\buttom.json', encoding='utf-8') as f:
        menu_json = json.load(f)
        
    builder = InlineKeyboardBuilder()
    for i in range(len(menu_json[level]['callback_data'])):
        builder.button(
            text=menu_json[level]['text'][i], 
            callback_data=menu_json[level]['callback_data'][i])
    builder.adjust(1)
    return builder

def home_menu():
    return  [
        [InlineKeyboardButton(text="Как это работает для вас", callback_data="how_work_for_your")],
        [InlineKeyboardButton(text="Как работает интерфейс клиента", callback_data="how_work_for_client")],
        [InlineKeyboardButton(text="Заказать", callback_data="buy")]
    ]

menu_int_client = [
    [InlineKeyboardButton(text="Расскажи", callback_data="tell_me")],
    [InlineKeyboardButton(text="Покажи", callback_data="show_me")],
    [InlineKeyboardButton(text="Назад", callback_data="menu")]
]
menu = InlineKeyboardMarkup(inline_keyboard=home_menu())
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])