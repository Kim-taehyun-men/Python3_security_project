import dns.resolver

hosts=["www.naver.com","www.daum.net", "www.google.com"]

for host in hosts:
    print(host)
    dns_ip = dns.resolver.resolve(host,"A")
    for ip in dns_ip:
        print(ip)
