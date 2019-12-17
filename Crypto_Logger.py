#Basic project to monitor crypto currency prices
#07/12/2019

#To use: add a call to the coin you want
#number is which part of json it uses: 0 is btc
#TODO: may add feature to disable the print out, html logs, other notifications

try:
    import requests, sys, json, time
    from datetime import datetime
except ImportError as e:
    print(e)

print("Crypto currency price logger")
print("github.com/nullsc/Bitcoin_Monitor/ \n")

apiUrl = 'https://api.coinmarketcap.com/v1/ticker/'
btcalertPRICE = float('7569.1')
TIME = 30 #time in minutes to poll
logFile = "log.txt"


class checker(object):
    def __init__(self, name, alertPrice = 0):
        self.name = name #instance
        self.coin = "null" #none
        self.sym = "null"
        self.price = 0
        self.alertPrice = alertPrice #0 by default, zero will also deactivate it

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
        self.price = float(cryptoData[cIndex]['price_usd'])
        self.sym = cryptoData[cIndex]['symbol']
        print(self.coin)
        print(self.price)
        if(self.alertPrice > 0): #start logging
            if(self.price < self.alertPrice):
                print("[ALERT]Price has dipped below {}".format(str(self.alertPrice)))
                self.log("[ALERT]Price has dipped below {}".format(str(self.alertPrice))) #append the msg
            else:
                self.log()
        else:
            self.log()

 
btc = checker("btc", btcalertPRICE) #first arg is a name which may be used later, second argument is the alert price
eth = checker("eth", 200)

while (1):
    btc.scrape(0)
    eth.scrape(1)
    time.sleep(TIME * 60)



