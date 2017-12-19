import requests

url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_stat' \
      'ion=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' %('2018-01-17','SHH','XAY')

response = requests.get(url)
response = response.json()
result = response['data']['result']
tickets = []
for i in result:
    a = i.split('|')
    if a[0] == '':
        tickets.append(a)
        pass

print(tickets)
