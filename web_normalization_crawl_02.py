import requests
import re

url = 'https://sports.news.naver.com/news?oid=139&aid=0002168397' 
headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
        }
response = requests.get(url,headers=headers)
results = re.findall(r'[\w\.-]+@[\w\.-]+', response.text) 
results = list(set(results))
print(results)

#보안 - 고객서비스 대상으로 중요한 이메일, 아이디, 주석처리 내...-> 슬랙을 이용한 통보, 이메일을 통해서 통보..
