from vk_api.longpoll import VkLongPoll, VkEventType
from threading import Thread
import vk_api, random, time, os, re

#mytokenvk = os.environ.get('BOT_TOKEN_VK')
vk_session = vk_api.VkApi(token='0c0151147883a61fcc4cf73fd9255c0d53045071fb0697f8995c14294abfb1add34f73f7dd754112452bd')
longpull = VkLongPoll(vk_session)
vk = vk_session.get_api()


def answer():
    while True:
        for event in longpull.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    q = event.text
                    print(q)
                    if 'нажмите' in q:
                        textlookfor=r"\w\w\w\w\w\s\d\d\d\d"
                        mask2= re.findall(textlookfor, q)
                        print(mask2)
                        #mask= mask2[-1]
                        vk.messages.send(
                            # chat_id= event.chat_id,
                            chat_id=48,
                            message=mask2,
                            random_id=random.randint(0, 10000000000000000)
                        )
                    if 'поиграйте' in q:
                        vk.messages.send(
                            # chat_id= event.chat_id,
                            chat_id=48,
                            message='питомец поиграть',
                            random_id=random.randint(0, 10000000000000000)
                        )
                        vk.masseges.send(
                            chat_id=48,
                            message='питомец поход',
                            random_id=random.randint(0, 10000000000000000)
                        )

                    if 'покормите' in q:
                        vk.messages.send(
                            # chat_id= event.chat_id,
                            chat_id=48,
                            message='питомец покормить',
                            random_id=random.randint(0, 10000000000000000)
                        )
                        vk.masseges.send(
                            chat_id=48,
                            message='питомец поход',
                            random_id=random.randint(0, 10000000000000000)
                        )
                    else:
                        pass
            else:
                pass


def gorilla_kopat():
    while True:
        for _ in range(5):
            time.sleep(10)
            vk.messages.send(
                # chat_id= event.chat_id,
                chat_id=48,
                message='копать алмазы',
                random_id=random.randint(0, 10000000000000000)
            )
        time.sleep(1500)


def gorilla_pitomec():
    while True:
        vk.messages.send(
            chat_id=48,
            message="питомец поход",
            random_id=random.randint(0, 10000000000000000)
        )
        time.sleep(3710)

def main():
    answervar = Thread(target=answer)
    kopat = Thread(target=gorilla_kopat)
    pitomec = Thread(target=gorilla_pitomec)
    answervar.start()
    kopat.start()
    pitomec.start()

'''
def main1():
   threading.Thread(target=answer).start()
   threading.Thread(target=gorilla_pitomec).start()
   threading.Thread(target=gorilla_kopat).start()
'''
try:   
	if __name__ == '__main__':
	    main()
except:
	raise Exception('test err')
