from bot.creating import *
from bot.bot_commands import *


# Запуск процесса поллинга новых апдейтов
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

