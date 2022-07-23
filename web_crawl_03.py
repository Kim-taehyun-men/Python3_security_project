import requests
from bs4 import BeautifulSoup
import webbrowser

url = "https://www.malware-traffic-analysis.net/2022/index.html"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")

with open("a.html", "w", encoding="UTF-8") as f:
    f.write(soup.text)

webbrowser.open_new("a.html")
