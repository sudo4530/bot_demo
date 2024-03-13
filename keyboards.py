from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from connect_db import Database

menu_keyword = ReplyKeyboardMarkup([
    [KeyboardButton("Menyu"), KeyboardButton("Category")],
], resize_keyboard=True)


menu_detail = ReplyKeyboardMarkup(resize_keyboard=True)
query = "SELECT * FROM menu"
for i in Database.connect(query, "select"):
    menu_detail.add(KeyboardButton(i[1]))
menu_detail.add(KeyboardButton("Back"))

category_detail = ReplyKeyboardMarkup([
    [KeyboardButton("Category 1")],
    [KeyboardButton("Category 2")],
    [KeyboardButton("Category 3")],
    [KeyboardButton("Category 4")],
    [KeyboardButton("Back")],
], resize_keyboard=True)


menu_1 = ReplyKeyboardMarkup([
    [KeyboardButton("1")],
    [KeyboardButton("2")],
    [KeyboardButton("Back")],
], resize_keyboard=True
)
