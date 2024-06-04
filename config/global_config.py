from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv
load_dotenv()

cities_list = ['Казань', 'Москва', 'Санкт-Петербург', 'Чебоксары', 'Сочи', 'Владивосток', 'Екатеринбург', 'Пекин']
weather_list = [['Дата', 'Город', 'Температура', 'Скорость ветра']]
engine = create_engine(f"postgresql://{os.getenv('USER_DB')}:{os.getenv('PASSWORD_USER')}@{os.getenv('API_DB')}/{os.getenv('NAME_DB')}", echo=True)
base = declarative_base()
