import vk_api,random,os
token = str(os.environ.get('token'))
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


vk_session = vk_api.VkApi(token=token)
vk=vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '199179454')
a=0
for event in longpoll.listen():
    if event.type == VkBotEventType.GROUP_JOIN:
        vk.messages.send(peer_id=463342021,random_id=0,message="Кто-то подписался на группу!")
    if event.type == VkBotEventType.GROUP_LEAVE:
        vk.messages.send(peer_id=463342021,random_id=0,message="Кто-то отписался от группы!")
    if event.type == VkBotEventType.WALL_POST_NEW:
        for i in vk.messages.getConversations(count=200,fields="id",filter="all",extended=1)["items"]:
            id=i['conversation']['peer']['id']
            if id==2000000001:
                pass
            else:
                try:
                    vk.messages.send(peer_id=id,message="В группе вышел новый пост!",random_id=0)
                except:
                    pass
    if event.type == VkBotEventType.MESSAGE_NEW:
        text=event.obj["message"]["text"].lower()
        pid=event.obj["message"]["peer_id"]
        uid=event.obj["message"]["from_id"]
#        if ".say" in text:
#            if uid==463342021 or uid==534212261:
#                text2=text.replace(".say ","").split(" ")
#                vk.messages.send(peer_id=pid,random_id=0,message=" ".join(text2))
        if text=="дс" or text=="дискорд" or text=="сервер":
            vk.messages.send(peer_id=pid,random_id=0,message="https://discord.gg/r3bPHX3 . Здесь мы играем в Among Us с подписчиками, заходи")
            a=1
        if text=="админ":
            vk.messages.send(peer_id=pid,random_id=0,message="https://vk.com/hokietm")
            a=1
        if text=="владелец" or text=="создатель":
            vk.messages.send(peer_id=pid,random_id=0,message="https://vk.com/glockinmylap . Все вопросы к нему!")
            a=1
        if "идея" in text:
            text2=text.replace("идея ","").split(" ")
            vk.messages.send(peer_id=534212261,random_id=0,message="Идея: "+" ".join(text2))
            vk.messages.send(peer_id=pid,random_id=0,message="Идея отправлена!")
            a=1
        if text=="бот":
            vk.messages.send(peer_id=pid,random_id=0,message="https://vk.com/vibed . Пиши если хочешь такого же бота)")
            a=1
        if text=="команды":
            a=1
            vk.messages.send(peer_id=pid,random_id=0,message='''
Вот команды:
1. Владелец/Создатель - даёт ссылку на владельца сообщества
2. "Админ" - даёт ссылку на админа
3. "Сервер" - даёт ссылку на сервер в дискорде
4. "Бот" - даёт ссылку на создателя бот
5. \"Идея\" {текст} - идея для поста''')
        else:
            if event.from_chat:
                pass
            else:
                if a == 0:
                    random2=["я не знаю такую команду! Напиши \"команды\"","Я хз че ты написал, по этому дам совет. Пиши \"команды\"","Напиши \"команды\""]
                    vk.messages.send(peer_id=pid,random_id=0,message=random.choice(random2))
        a=0
