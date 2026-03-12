from aiogram import Bot, Dispatcher, types
import asyncio

TOKEN = "ВАШ8692892233:AAFQ0tuhuj01WJ1ub6_sabpBaU5QyROh-do_НОВЫЙ_ТОКЕН_ОТ_BOTFATHER"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer("Привет! Бот работает.")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
