import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Сейчас мы используем токен из кода для проверки
TOKEN = "8692892233:AAGQLwqxMI0Y1U_uxOAxEZaFYwHU8EqtLWY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("✅ Бот успешно запущен и работает на Railway!")

async def main():
    print("Бот успешно запущен!")
    # Очистка очереди сообщений
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
