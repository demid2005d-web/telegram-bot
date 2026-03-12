import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Railway сам подставит токен из вкладки Variables в эту переменную
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("✅ Бот успешно запущен и работает на Railway!")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
