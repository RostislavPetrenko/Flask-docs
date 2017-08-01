from flask import Flask

from config import Configuration #Импортируем наш конфигурационный файл

app = Flask(__name__)
app.config.from_object(Configuration) # Используем значения из нашего конфиг файла