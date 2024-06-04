import requests
import pandas
from config.global_config import engine, base, weather_list
from cities_for_weather import Cities
from sqlalchemy.orm import Mapped,  mapped_column, Session
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()



class WeatherCity:
    def get_param(self):
        for city in Cities.str_cities():
            r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={os.getenv('API_ID')}")
            temp = r.json()['main']['temp']
            wind = r.json()['wind']['speed']
            gorod = r.json()['name']
            weather_list.append([datetime.now(), gorod, temp, wind])
        return weather_list

    def weather_list_csv(self):
        date = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        with open(fr"C:/programms/weather_project/weather_files/{date}.csv", 'w') as f:
            pandas.DataFrame(self.get_param()).to_csv(f, index=False)

a = WeatherCity()
a.weather_list_csv()

class Weather_In_City(base):
    __tablename__ = 'weather_in_city'
    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    date: Mapped[datetime]
    city: Mapped[str]
    temperature: Mapped[float]
    wind_speed: Mapped[float]

with Session(bind=engine) as session:
    with session.begin():
        base.metadata.create_all(bind=engine)
        for i in range(1, len(weather_list)):
                weather_str = Weather_In_City(date=weather_list[i][0], city=weather_list[i][1], temperature=weather_list[i][2], wind_speed=weather_list[i][3])
                session.add(weather_str)

