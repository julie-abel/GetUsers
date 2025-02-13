#Бот, который должен быть запущен во время получения данных из групп
import asyncio
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantsSearch

# Укажите свои учетные данные Telegram API
api_id = 23928587  # Ваш API ID +79537600412
api_hash = '7294ef219af1271bc71d968bdb342e06'  # Ваш API Hash
bot_token = '8036769492:AAGcB5XzmHHW3SNWybVhz1yHRTrxMTH6JZE'    # Токен вашего бота

# Инициализация клиента Telethon
client = TelegramClient('bot_session', api_id, api_hash)


# Функция для получения списка участников чата
async def get_members(chat_id):
    members = []  # Список для хранения пользователей

    # Получаем всех участников чата
    async for participant in client.iter_participants(chat_id, filter=ChannelParticipantsSearch('')):
        user_name = participant.first_name or ''
        if participant.last_name:
            user_name += f" {participant.last_name}"
        if participant.username:
            user_name += f" (@{participant.username})"

        members.append(f" {participant.id}: '', #{user_name}")

        # Добавляем небольшую задержку между запросами, чтобы избежать лимитов Telegram API
        await asyncio.sleep(0.5)

    return members


# Обработчик команды /get_members <chat_id>
@client.on(events.NewMessage(pattern=r'/get_members (\-?\d+)'))
async def handler(event):
    sender_id = event.sender_id  # ID отправителя команды
    match = event.pattern_match  # Извлекаем chat_id из команды

    try:
        # Получаем chat_id из команды
        chat_id = int(match.group(1))
        await event.reply(f"Получаю список участников для чата с ID {chat_id}...")

        # Получаем список участников чата
        members = await get_members(chat_id)

        if members:
            result = '\n'.join(members)
            MAX_MESSAGE_LENGTH = 4096

            # Отправляем результат в ответ на команду, разбивая на части
            for i in range(0, len(result), MAX_MESSAGE_LENGTH):
                await client.send_message(sender_id, result[i:i + MAX_MESSAGE_LENGTH])
        else:
            await event.reply("Не удалось получить список участников.")
    except Exception as e:
        await event.reply(f"Произошла ошибка: {e}")


# Запуск клиента
async def main():
    await client.start(bot_token=bot_token)
    print("Бот запущен...")
    await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
