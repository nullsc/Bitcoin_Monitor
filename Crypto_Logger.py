#Basic project to monitor crypto currency prices
#07/12/2019

#To use: add a call to the coin you want
#number is which part of json it uses: 0 is btc

#TODO: may add feature to disable the print out(done), html logs, other notifications

#Issues: On the ticker directory I noticed that the coins are sorted by 'rank'. Although this is not an issue
#currently it could become an issue if you were using the tool long term and the ranks changed.
#A way to get around this is to use for example the /bitcoin folder and the index would be 0. although
#doing this you would have to a different url for each instance, you could use the first arg to do this

try:
    import requests, sys, json, time
    from datetime import datetime
except ImportError as e:
    print(e)

print("Crypto currency prices logger")

#apiUrl = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/' #https://api.coinmarketcap.com/v1/ticker dir
apiUrl = 'https://api.coinmarketcap.com/v1/ticker/'
btcalertPRICE = 7000.0
TIME = 30 #time in minutes to poll
logFile = "log.txt"
printPrices = True #Will print the prices each time


class checker(object):
    '''Class to check the crypto API'''
    def __init__(self, name, cIndex, logging = True, alertPrice = 0):
        self.name = name #instance
        self.cIndex = cIndex #coin index
        self.coin = "null"
        self.sym = "null" #coin symbol
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

    def scrape(self):
        priceRequest = requests.get(apiUrl)
        cryptoData = json.loads(priceRequest.text) #convert to dict

        self.coin = cryptoData[self.cIndex]['name']
        self.price = float(cryptoData[self.cIndex]['price_usd']) # 7569.17021495
        self.sym = cryptoData[self.cIndex]['symbol']
        if(printPrices):
            print(self.coin)
            print(self.price)

        if(self.alertPrice > 0): #start logging
            if(self.price < self.alertPrice):
                print("[ALERT] {} Price has dipped below {}".format(self.coin, str(self.alertPrice)))
                if(self.logging == True):
                    self.log("[ALERT] {} Price has dipped below {}".format(self.coin, str(self.alertPrice))) #append the msg
            else:
                if(self.logging == True):
                    self.log()
        else:
            if(self.logging == True):
                self.log()


btc = checker("btc", 0, True, btcalertPRICE) #note, coin index, logging?, price to alert at
eth = checker("eth", 1, True, 140)

while (1):
    btc.scrape()
    eth.scrape()
    time.sleep(TIME * 60)



