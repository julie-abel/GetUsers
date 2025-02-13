#этап 1. получение списка участников и вывод их идов в консоль,
# для последующего использования для создания групп
# Бот getmyusers должен быть в этой группе


from telethon import TelegramClient
from telethon.tl.functions.channels import CreateChannelRequest, InviteToChannelRequest
from telethon.tl.types import ChannelParticipantsAdmins
import asyncio

#from create_group_with_bot import curator

# Укажите свои учетные данные Telegram API
api_id = 23928587  # Ваш API ID +79537600412
api_hash = '7294ef219af1271bc71d968bdb342e06'  # Ваш API Hash
bot_token = '8036769492:AAGcB5XzmHHW3SNWybVhz1yHRTrxMTH6JZE'  # Токен бота @Getusersfrombot

#supergroup_id = -1002257830039  # группа Светы
# supergroup_id = -1002436322933 #Айсылу
supergroup_id = -1002313576803  #  Анна Павлова
#supergroup_id = -1002435650518  #  Ильвира
#supergroup_id = -1002278434123  # Группа Юлии
#supergroup_id = -1002499830579 # Олеся
#supergroup_id = -1002268599692 #> Юля Мартьянова
#supergroup_id = -1002389759298  # Группа Илоны
#supergroup_id = -1002450685211  # Группа Ирины
#supergroup_id = -1002265418288  # Группа Юлии Розвезевой
#supergroup_id = -1002467087860 # чат тайного клуба
#supergroup_id = -1002154690459 # тайный клуб
#curator = [7576222106] # я
curator = [269415093] # Анна Павлова
#curator = [6432080123] # Илона
#curator = [5057620285] # Ирина Каева
#curator = [1829841346] # Айсылу
#curator = [5173292505] # Юлия Розвезева

async def main():
    # Инициализация клиента с использованием токена бота
    client = TelegramClient('bot_session1', api_id, api_hash)

    # Авторизация бота
    await client.start(bot_token=bot_token)

    try:
        print("Получение списка администраторов супергруппы...")
        # Получаем список администраторов группы
        admins = await client.get_participants(supergroup_id, filter=ChannelParticipantsAdmins())
        admin_ids = [admin.id for admin in admins]

        entity = await client.get_input_entity(supergroup_id)
        print(f"Информация о чате: {entity}")

    except Exception as e:
        print(f"Не удалось получить информацию о чате: {type(e).__name__}: {e}")

    print("Получение списка участников супергруппы...")
    try:
        # Используем метод iter_participants для работы с супергруппами
        async for member in client.iter_participants(supergroup_id):
            if not member.bot and not member.id in admin_ids :
                user_id = member.id
                user_name = member.first_name or "Нет имени"
                first_name = member.first_name or " "
                last_name = member.last_name or " "
                #print(f"({user_id}, \"/status {user_id}, '{user_name} {first_name} {last_name}'),")
                #print(f" {user_id},")
                print(f"insert into chats values({user_id},-100,'{user_name} {first_name} {last_name}', {curator[0]});")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(main())

