import requests
from bs4 import BeautifulSoup

url = "https://www.boannews.com/"
html = requests.get(url, verify=False).text
soup = BeautifulSoup(html, "html5lib")
for i in range(6):
    tags = soup.select("#headline0 > ul > li:nth-of-type("+str(i)+") > p")
    for tag in tags:
        print(tag.text)
