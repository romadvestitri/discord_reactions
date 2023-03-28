import requests as r
import json
import random as rand
import config as con
# from pyuseragents import random as random_useragent


fp = open('http1.txt','r')
HEADERS = {"user-agent": "Opera/9.80 (X11; Linux x86_64; U; de) Presto/2.2.15 Version/10.00", "Conection": "close"}

proxies = fp.read().split("\n")


#Функция, обрабатывающая прокси из файла в нужный формат возвращает словарь для session.proxies
def get_proxy():
	proxy = rand.choice(proxies).split(":")
	str_proxy = f'http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}'
	return {"http":str_proxy,"https":str_proxy}

reaction = '💦'
reactions = ['🏛️','🍇','🙉','💥','💫','💦','💯','☢️','♊','🥑','🍈','🍉','🍊','💓','🏁','🚩','🎌','🏴','🏳️','🏴‍☠️','🇺🇸','🐖','🐷','🐪','🐭','🦫','🐼','🦨','🦕','🩸','❤️']

#ID чата на сервере(можно взять из URL)
chat_id = 1000054621844291636


def main():
	i = 1
	last_msg_id = ''
	s = r.Session()
	#основной цикл, ждущий появления сообщения
	while True:
		count = rand.randint(0, len(con.tokens)+1)
		if i == count+1:
			i = 1
		#авторизация пользователя по токену из config.py
		s.headers['authorization'] = con.tokens[i-1]
		print(f"{s.headers=}")
		# получение всех сообщений чата
		resp = s.get(f'https://discord.com/api/v9/channels/{chat_id}/messages').json()

		if resp[0]["id"] != last_msg_id:
			#цикл проставления реакций на последние пять сообщений, сделано для того, если сообщения будут быстро проходить и поставить реакции для максимально возможного количества сообщений
			for j in range(5):
				if j == 0:
					last_msg_id = resp[j]["id"]
				if ('reactions' not in resp[j].keys()) or ('reactions' in resp[j].keys() and not resp[j]['reactions'][0]['me']):
					reaction1 = rand.choice(reactions)
					# Цикл проставления реакций от рандомного количества юзеров
					for k in range(count+1):
						if i == count+1:
							i = 1
						# Проверка на сообщения от определенных юзеров. Необходимо изменить на айдишники ботов 
						if resp[j]['author']['id'] == '776368128144834561' or resp[j]['author']['id'] == '972525837222019122':
							# Подключаем прокси
							with r.Session() as session:
								session.proxies.update(get_proxy())
								session.headers.update(HEADERS)
								session.headers['authorization'] = con.tokens[i-1]
								print(f"{session.headers=}\n{session.proxies=}")
								try:
									
									
									resp1 = session.put(f'https://discord.com/api/v9/channels/{chat_id}/messages/{resp[j]["id"]}/reactions/{reaction1}/@me')
									
								except Exception as err:
									print('error', err, "\n\n\n\n\n\n")
							i += 1


if __name__ == '__main__':
	main()		