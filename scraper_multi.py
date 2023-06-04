import requests
from bs4 import BeautifulSoup
import pandas as pd
import threading
import time

start = time.time()


def func1():
    url = "https://www.mobile.ir/phones/prices.aspx"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.select('a.phone')
    price = soup.select('td.price a')

    list_title = [t.text for t in title]
    list_price = [int(p.text.replace(',', '')) for p in price]

    database = dict(list(zip(list_title, list_price)))

    df = pd.DataFrame(list(database.items()), columns=['گوشی', 'قیمت'])
    df = df.dropna()
    df = df.drop_duplicates()
    print(df)

    high_price_phone = df.loc[df['قیمت'].idxmax()]
    low_price_phone = df.loc[df['قیمت'].idxmin()]

    avg_price = df['قیمت'].mean()

    print("\nگران‌ترین گوشی: ", high_price_phone['گوشی'])
    print("ارزان‌ترین گوشی: ", low_price_phone['گوشی'])
    print("میانگین قیمت گوشی‌ها: ", int(avg_price))


def func2():
    url = "https://www.mobile.ir/phones/prices.aspx?page=2"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.select('a.phone')
    price = soup.select('td.price a')

    list_title = [t.text for t in title]
    list_price = [int(p.text.replace(',', '')) for p in price]

    database = dict(list(zip(list_title, list_price)))

    df = pd.DataFrame(list(database.items()), columns=['گوشی', 'قیمت'])
    df = df.dropna()
    print(df)

    high_price_phone = df.loc[df['قیمت'].idxmax()]
    low_price_phone = df.loc[df['قیمت'].idxmin()]

    avg_price = df['قیمت'].mean()

    print("\nگران‌ترین گوشی: ", high_price_phone['گوشی'])
    print("ارزان‌ترین گوشی: ", low_price_phone['گوشی'])
    print("میانگین قیمت گوشی‌ها: ", int(avg_price))


def func3():
    url = "https://www.mobile.ir/phones/prices.aspx?page=3"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.select('a.phone')
    price = soup.select('td.price a')

    list_title = [t.text for t in title]
    list_price = [int(p.text.replace(',', '')) for p in price]

    database = dict(list(zip(list_title, list_price)))

    df = pd.DataFrame(list(database.items()), columns=['گوشی', 'قیمت'])
    df = df.dropna()
    print(df)

    high_price_phone = df.loc[df['قیمت'].idxmax()]
    low_price_phone = df.loc[df['قیمت'].idxmin()]

    avg_price = df['قیمت'].mean()

    print("\nگران‌ترین گوشی: ", high_price_phone['گوشی'])
    print("ارزان‌ترین گوشی: ", low_price_phone['گوشی'])
    print("میانگین قیمت گوشی‌ها: ", int(avg_price))


t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t3 = threading.Thread(target=func3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.time()
print(end - start)
