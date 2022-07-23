import optparse

#처음 안내해주는 도움말, usage명령어로 불러옴
parser = optparse.OptionParser('Port Scan '+ '-H <Host> -P <Port>')
# -H옵션 입력을 하면 host에다가 받는다.
parser.add_option('-H', dest='host', type='string', help='specify host')
parser.add_option('-P', dest='port', type='string', help='specify port')

#옵션에 입력한 값을 넣어준
(options, args) = parser.parse_args()

host = options.host
port = options.port

#입력 받은 값들이 없으면 pasrser.usage값을 출력
if(host == None) | (port == None):
    print(parser.usage)

else:
    print(host)
    print(port)
