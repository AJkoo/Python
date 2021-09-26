import requests

res = requests.get('http://google.com')
print(res.status_code)  # 200이면 정상

res.raise_for_status()

print(len(res.text))

with open('mygoogle.html', 'w', encoding='utf8') as f:
    f.write(res.text)






