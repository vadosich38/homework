percent_first = int(input("На сколько % вырастут цены в первый год: "))
percent_sec = int(input("На сколько % вырастут цены во второй год: "))
def get_higher_price(price, percent):
    return round(price * (1 + percent / 100), 2)

prices = [1.09, 23.56, 57.84, 4.56, 6.78]

#one_year_prices = [price * (1 + percent_first/100) for price in prices]
#sec_year_prices = [price * (1 + percent_sec/100) for price in prices]
one_year_prices = [get_higher_price(price, percent_first) for price in prices]
sec_year_prices = [get_higher_price(price, percent_sec) for price in prices]


print("Сумма цен за каждый год:", round(sum(prices), 2), round(sum(one_year_prices), 2), round(sum(sec_year_prices), 2))