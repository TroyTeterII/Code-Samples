

#PART 1
import datetime
import csv
import urllib.request
#open up web link to stock into in csv format

#show last trade, change, date, open ,and previous close.
choice=input("Enter a company's stock symbol:")

def getStockData(company):
    #dynamic URL request for different companies
    URL1="http://quote.yahoo.com/d/quotes.csv?s="
    URL2=company
    URL3="&f=sl1d1t1c1ohgvj1pp2owern&e=.csv"
    URL4=URL1+URL2+URL3
    #print(URL4)
    #URL opener
    web_page = urllib.request.urlopen(URL4)
    contents = web_page.read() .decode(errors="replace")
    contents=contents.replace('>','<').split('<')
    #taking a look at the data unsorted
    for entry in contents:
        pieces=entry.split(",")
    #change date to dateime object
    date=pieces[2]
    date=date[1:-1]
    date=date.split("/")
    #Format date
    fmt="%b %d, %y"
    date=datetime.date(int(date[2]),int(date[0]),int(date[1]))
    dateFmt=date.strftime(fmt)
    print("The last trade for",company,"was",pieces[1],"and the change was",pieces[4], "on",dateFmt,"The open was",pieces[6],"the previous close was",pieces[5])
getStockData(choice)

#PART 2

stock_comps=["AAPL","GOOG","NKE","AXP","JMP","WMT","CVX","DD","V","KO"]

for item in stock_comps:
    getStockData(item)

    
