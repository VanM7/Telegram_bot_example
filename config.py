from dotenv import load_dotenv
import os

# Загрузить переменные из .env
load_dotenv()

# Получить значение токена
token = os.getenv('TOKEN')