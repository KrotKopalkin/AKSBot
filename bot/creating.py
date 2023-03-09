import json
from aiogram import Bot, Dispatcher, types, executor
import logging



# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5847893374:AAE6__0Eja6PHQk5gzFdj_k7bMSPL5fYPFE")  # тестовый
#bot = Bot(token="6063059678:AAEc8PcY1dswjmv-CuRbCKA9JdfvZQ3BEhQ") # рабочий
# Диспетчер
dp = Dispatcher(bot)