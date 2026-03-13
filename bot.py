import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command

# Токен (не забудьте обновить в BotFather, если GitHub его заблокировал!)
TOKEN = "8692892233:AAGQLwqxMI0Y1U_uxOAxEZaFYWHU8EqtLWY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- ФУНКЦИИ ДЛЯ РАБОТЫ С БАЗОЙ ---
def add_user(user_id):
    users = get_users()
    if str(user_id) not in users:
        with open("users.txt", "a") as f:
            f.write(f"{user_id}\n")

def get_users():
    try:
        with open("users.txt", "r") as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        return set()

# --- ОБРАБОТЧИКИ ---

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    add_user(message.from_user.id) # Теперь пользователь реально сохраняется
    await message.answer("✅ Вы подписаны на рассылку!")

@dp.message(Command("send"))
async def send_broadcast(message: types.Message):
    # Узнайте свой ID в боте @userinfobot и вставьте вместо 0
    ADMIN_ID = 728473364
    
    if ADMIN_ID != 0 and message.from_user.id != ADMIN_ID:
        return

    users = get_users()
    count = 0
    for user_id in users:
        try:
            await bot.send_message(user_id, "📢 Сообщение рассылки!")
            count += 1
            await asyncio.sleep(0.05)
        except Exception:
            continue
    
    await message.answer(f"✅ Рассылка завершена! Получили: {count} чел.")

# --- ЗАПУСК ---
async def main():
    print("Бот запущен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
