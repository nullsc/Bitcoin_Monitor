# Bitcoin Monitor
Tool to monitor crypto prices written in python.
This tool will poll the mcap site and download the json from the API, it will log the prices and print out an alert if it dips below a user provided number.

## How To use
You must have Python 3.5+ and the requests library installed.
Declare a new variabe of instance checker. The first argument is a label which can be anything, the second argument will be the value that will send out an alert if the price goes below that. If you do not want to use the alerts feature then set it to 0 or just don't put anything for the second argument.

eth = checker("eth", 140)

In the main loop add the code to start scraping. If you are using the api link below you can see all the json data for all the coins and these start at number 0. Check for which coin you want and use the number as the argument below, so for example bitcoin is number 0.

eth.scrape(0)

https://api.coinmarketcap.com/v1/ticker/

Save the details in the file and now run the python programming and it will start logging.

## TODO
Add HTML logging, add the feature to disable logging
