import os
import asyncio
from aiogram import Bot, Dispatcher

# Включаем отладку
TOKEN = os.getenv("BOT_TOKEN")

print(f"DEBUG: Значение TOKEN равно: {TOKEN}") # Это выведет значение в логи

if TOKEN is None:
    print("ОШИБКА: Переменная BOT_TOKEN не найдена в окружении!")
    exit(1) # Завершаем работу, если токена нет

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    print("Бот успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
