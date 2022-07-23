import requests
import re
import socket

#outside IP
req = requests.get("http://ipconfig.kr/")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',req.text)
print(out_addr)

# inner IP
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print("Inner IP", in_addr.getsockname())
