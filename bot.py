import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

# ВСТАВЬТЕ НОВЫЙ ТОКЕН ИЗ BOTFATHER
TOKEN = "8692892233:AAGYUkHBvlLCVJHPTnDcrEMc7ufqmwlmPCk"
ADMIN_ID = 728473364 

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Состояния для диалога рассылки
class Broadcast(StatesGroup):
    waiting_for_message = State()

def add_user(user_id):
    users = get_users()
    if str(user_id) not in users:
        with open("users.txt", "a") as f:
            f.write(f"{user_id}\n")

def get_users():
    try:
        with open("users.txt", "r") as f:
            return set(line.strip() for line in f)
    except FileNotFoundError: return set()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    add_user(message.from_user.id)
    await message.answer("✅ Вы подписаны на рассылку! Теперь админ может присылать вам новости.")

# 1. Начинаем рассылку
@dp.message(Command("send"), F.from_user.id == ADMIN_ID)
async def start_broadcast(message: types.Message, state: FSMContext):
    await message.answer("Введите текст или пришлите фото для рассылки (или /cancel):")
    await state.set_state(Broadcast.waiting_for_message)

# 2. Отменяем, если передумали
@dp.message(Command("cancel"), Broadcast.waiting_for_message)
async def cancel_broadcast(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Рассылка отменена.")

# 3. Сама рассылка
@dp.message(Broadcast.waiting_for_message)
async def do_broadcast(message: types.Message, state: FSMContext):
    users = get_users()
    count = 0
    await message.answer(f"Начинаю рассылку по {len(users)} пользователям...")
    
    for user_id in users:
        try:
            # Копируем любое сообщение (текст, фото, видео)
            await message.copy_to(chat_id=user_id)
            count += 1
            await asyncio.sleep(0.05)
        except Exception: continue
    
    await state.clear()
    await message.answer(f"✅ Готово! Получили: {count} чел.")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
