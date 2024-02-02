import asyncio
import logging
import subprocess
from aiogram import Bot, Dispatcher, types
import SQL_ask
from config_reader import config

bot = Bot(token=config.bot_token.get_secret_value())

logging.basicConfig(level=logging.INFO)
# Диспетчер
dp = Dispatcher()


async def start_monitoring():
    while True:
        if SQL_ask.check_for_new_record():
            # Обработайте новую запись
            await bot.send_message(385076489, f"{SQL_ask.send_for_new_date()}")

        # Пауза между проверками базы данных
        # await asyncio.sleep()


async def main():
    await start_monitoring()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
