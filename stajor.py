from telegram import InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardMarkup,MessageEntity
from telegram import Update,KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
import mysql.connector
from backend import analiz

data = analiz()

b1, b2, b3 = ("🇺🇿 Ўзбекча","🇷🇺 Руский","🇺🇿 O\'zbekcha")
def b_button():
    return ReplyKeyboardMarkup([[b1], [b2], [b3]], resize_keyboard=True, one_time_keyboard=True)

t1,t2 = ("📱 Raqam yuborish", "🇺🇿 Tilni o'zagrtirish 🇷🇺")
