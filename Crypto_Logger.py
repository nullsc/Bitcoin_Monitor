#Basic project to monitor crypto currency prices
#07/12/2019

#To use: add a call to the coin you want
#number is which part of json it uses: 0 is btc
#TODO: may add feature to disable the print out(done), html logs, other notifications

try:
    import requests, sys, json, time
    from datetime import datetime
except ImportError as e:
    print(e)

print("Crypto currency prices logger")

apiUrl = 'https://api.coinmarketcap.com/v1/ticker/'
btcalertPRICE = 7000.0
TIME = 15 #time in minutes to poll
logFile = "log.txt"


class checker(object):
    '''Class to check the crypto API'''
    def __init__(self, name, logging = True, alertPrice = 0):
        self.name = name #instance
        self.coin = "null"
        self.sym = "null"
        self.price = 0
        self.alertPrice = alertPrice #0 by default, zero will also deactivate it
        self.logging = logging #on by default

    def banner(self):
        print("checking for " + self.name)

    def log(self, msg=''):
        timeStamp = datetime.now().strftime('%d:%m:%Y %H:%M') #https://docs.python.org/3/library/time.html#time.strftime
        with open(logFile, 'a') as f:
            f.write("[" + self.sym + "]" + timeStamp + ": " + str(self.price) + " " + msg + "\n")
            f.close()

    def scrape(self, cIndex):
        priceRequest = requests.get(apiUrl)
        cryptoData = json.loads(priceRequest.text) #convert to dict

        self.coin = cryptoData[cIndex]['name']
        self.price = float(cryptoData[cIndex]['price_usd']) # 7569.17021495
        self.sym = cryptoData[cIndex]['symbol']
        print(self.coin)
        print(self.price)
        if(self.alertPrice > 0): #start logging
            if(self.price < self.alertPrice):
                print("[ALERT]Price has dipped below {}".format(str(self.alertPrice)))
                if(self.logging == True):
                    self.log("[ALERT]Price has dipped below {}".format(str(self.alertPrice))) #append the msg
            else:
                if(self.logging == True):
                    self.log()
        else:
            if(self.logging == True):
                self.log()

 

btc = checker("btc", True, btcalertPRICE)
eth = checker("eth", True, 140)
#btc.scrape(0) #number is which part of json it uses: 0 is btc


while (1):
    btc.scrape(0)
    eth.scrape(1)
    time.sleep(TIME * 60)


