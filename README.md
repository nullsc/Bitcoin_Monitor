# Bitcoin Monitor
Tool to monitor crypto prices written in python.
This tool will poll the mcap site and download the json from the API, it will log the prices and print out an alert if it dips below a user provided number.

## How To use
You must have Python 3.5+ and the requests library installed (use 'pip install requests' to do this or you can use the requirements file).
Declare a new variable of instance checker. The first argument is a label which can be anything, the second is the coin index, the third argument sets whether the logging to file feature is active. The fourth argument will be the value that will send out an alert if the price goes below that. If you do not want to use the alerts feature then set it to 0 or just don't put anything for the third argument.

eth = checker("eth", 0, True, 140)

In the main loop add the code to start scraping tp call the function. If you are using the api link below you can see all the json data for all the coins and these start at number 0. Check for which coin you want and use the number as the argument below, so for example bitcoin is number 0.

eth.scrape()

https://api.coinmarketcap.com/v1/ticker/

Save the details in the file and now run the python programming and it will start logging.

## TODO
Add HTML logging, add the feature to disable logging(done), neaten up the class and make is call on init, single call function to operate, add a function to draw a graph

#bitcoin #crypto #api #monitor

![alt text](https://github.com/nullsc/Bitcoin_Monitor/blob/master/cryptoJson.PNG "Screen Shot")
