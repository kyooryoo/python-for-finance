def appointment(place="4F", time="10AM"):
    print("Your appointment is on {} at {}.".format(place,time))

appointment()
appointment("2F","2PM")
appointment(time="3PM",place="3F")

price=300
import math
print(math.sqrt(price))
print(price**(1/2))

stock_index="SP500"
print(stock_index[2:])

print("The {stock} is at {price} today.".format(stock=stock_index,price=price))

stock_info = {'sp500':{'today':300,'yesterday': 250}, 'info':['Time',[24,7,365]]}
# Yesterday's SP500 price (250)
print(stock_info['sp500']['yesterday'])
# The number 365 nested inside a list nested inside the 'info' key.
print(stock_info['info'][1][2])

def source_finder(aString):
    alen = len(aString)
    for i in range(alen):
        if aString[alen-i-1]=="-" and aString[alen-i]=="-":
            return aString[alen-i+1:]
source_finder("PRICE:345.324:SOURCE--QUANDL")

def price_finder(aString):
    alen = len(aString)
    find = False
    for i in range(alen):
        if aString[i].lower() == "p":
            if aString[i:i+5].lower() == "price":
                find = True
    print(find)
price_finder("PRICE:345.324:SOURCE--QUANDL")
price_finder("What is the price?")
price_finder("The price is 300")
price_finder("Today is Monday")

def avg_price(price_list):
    sum_price = 0
    for price in stock_price:
        sum_price = sum_price + price
    stock_numbers = len(stock_price)
    return sum_price/stock_numbers
stock_price = [100,101,102]
avg_price(stock_price)