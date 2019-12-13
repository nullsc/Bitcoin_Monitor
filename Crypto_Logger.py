#Basic project to monitor crypto currency prices
#07/12/2019
#work in progress
#to do: log to file, add multi coins

try:
    import requests, sys, json, time
except ImportError as e:
    print(e)

print("Crypto currency price logger")

apiUrl = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/' #https://api.coinmarketcap.com/v1/ticker dir
alertPRICE = float('7569.1')
TIME = 5 #time in minutes to poll

while (1):
    priceRequest = requests.get(apiUrl)

    #print(priceRequest.json())
    cryptoData = json.loads(priceRequest.text)

    print(cryptoData[0]['name']) #select the first json part
    print(cryptoData[0]['price_usd'])
    price = float(cryptoData[0]['price_usd'])
    if price < alertPRICE:
        print("[ALERT]Price has dipped below {}".format(str(alertPRICE)))

    time.sleep(TIME * 60)
