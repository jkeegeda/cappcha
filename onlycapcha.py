from vk_api.longpoll import VkLongPoll, VkEventType

import vk_api, random, time, os, re

mytokenvk = os.environ.get('BOT_TOKEN_VK')
vk_session = vk_api.VkApi(token=mytokenvk)
longpull = VkLongPoll(vk_session)
vk = vk_session.get_api()

while True:
	for event in longpull.listen():
		if event.type == VkEventType.MESSAGE_NEW:
			if event.to_me:
				q=event.text
				print(q)
				if 'красную' in q:
					textlookfor = r'\w\w\w\w\w\s\d\d\d\d'
					mask =re.findall(textlookfor, q)
					
					vk.messages.send(
						chat_id=48,
						message =mask,
						random_id = random.randinj t(0,999999999999)
					)
				else:
					pass
			else:
				pass
		else:
			pass
