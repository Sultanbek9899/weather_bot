import requests
import json
token = "2096976934:AAHt0W7a_t1OI6-ewdDZtl6856zGqPwG5uE"
url=f"https://api.telegram.org/bot{token}/getUpdates"

r=requests.get(url)
# print(r.content)

update = json.loads(r.content.decode('utf-8'))
message = update['result'][0]
chat_id = message['message']['chat']['id']
url=f"https://api.telegram.org/bot{token}/sendMessage"
response = requests.post(url, {"chat_id":chat_id, "text":"написан на python"})
# print(r.content)