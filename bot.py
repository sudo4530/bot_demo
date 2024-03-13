import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from connect_db import Database
from keyboards import menu_keyword, menu_detail, category_detail, menu_1

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    chat_id = str(message.chat.id)

    check_query = f"""SELECT * FROM users WHERE chat_id = '{chat_id}'"""
    if len(Database.connect(check_query, "select")) >= 1:
        print(f"{username}")

        await message.answer(f"Hello @{username}", reply_markup=menu_keyword)

    else:
        print(f"{first_name} start bot")
        query = f"""INSERT INTO users(first_name, last_name, username, chat_id) VALUES('{first_name}', '{last_name}', '{username}', '{chat_id}')"""
        print(f"{username} {Database.connect(query, "insert")} database")
        print(f"{username}")
        await message.answer(f"Hello @{username}", reply_markup=menu_keyword)


@dp.message_handler(commands=['data'])
async def select(message: types.Message):
    chat_id = message.chat.id
    query_select = f"SELECT * FROM users WHERE chat_id = '{chat_id}'"
    data = Database.connect(query_select, "select")
    print(data)
    await message.reply(f"""
        Salom @{data[0][3]}
        
        First Name: {data[0][1]}
        Last Name: {data[0][2]}""")

@dp.message_handler(lambda message: message.text == "Menyu")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Menyulardan birini tanglang:", reply_markup=menu_detail)

@dp.message_handler(lambda message: message.text == "Category")
async def show_category(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Bo'limlardan birini tanglang:", reply_markup=category_detail)

@dp.message_handler(lambda message: message.text == "Back")
async def back(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Menyu yoki Categoryni tanglang:", reply_markup=menu_keyword)

@dp.message_handler(lambda message: message.text == "Menu 1")
async def menu_01(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Menu 1", reply_markup=menu_1)


@dp.message_handler(lambda message: message.text not in ["Courses", "Modules", "Python"])
async def menu_01(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Bunday bo'lim mazjud emas", reply_markup=menu_detail)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
