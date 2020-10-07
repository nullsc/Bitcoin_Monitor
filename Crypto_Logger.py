#Basic project to monitor crypto currency prices
#07/12/2019
version = "v1.3"
#To use: add a call to the coin you want
#number is which part of json it uses: 0 is btc

#TODO: may add feature to disable the print out, html logs, other notifications, add try statement to check internet connection
# add main func

#Issues: On the ticker directory I noticed that the coins are sorted by 'rank'. Although this is not an issue
#currently it could become an issue if you were using the tool long term and the ranks changed.
#A way to get around this is to use for example the /bitcoin folder and the index would be 0. Although
#doing this you would have to a different url for each instance, you could use the first arg to do this

try:
    import requests, sys, json, time
    from datetime import datetime
except ImportError as e:
    print(e)

print("Crypto currency prices logger")
print("https://github.com/nullsc \n")

apiUrl = 'https://api.coinmarketcap.com/v1/ticker/'
btcalertPRICE = 7000.0 #float('7569.1')
TIME = 30 #time in minutes to poll
logFile = "log.txt"
printPrices = True #Will print the prices each time

RETRYTIME = 5 #time in minutes to retry after a connection failure


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

    def scrape(self):
        try:
            priceRequest = requests.get(apiUrl)
        except requests.exceptions.Timeout: #if it timesout, sleep then retry
            print("Connection Timed Out, Retrying")
            time.sleep(RETRYTIME * 60)
            return self.scrape()
        except requests.exceptions.RequestException as e: #if there is an error, sleep then retry
            print("Connection Error, Retrying")
            #print(e)
            time.sleep(RETRYTIME * 60)
            return self.scrape()

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
eth = checker("eth", 1, True, 100)


while (1):
    btc.scrape()#start scraping
    eth.scrape()
    time.sleep(TIME * 60)



