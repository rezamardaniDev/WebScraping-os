import pandas as pd
import threading
import time

start = time.time()


def find_top():
    df = pd.read_csv('./video-game-sales.csv')
    df = df.dropna()
    top_sales = df.loc[df['Global_Sales'].idxmax()]
    print(top_sales)


def find_low():
    df = pd.read_csv('./video-game-sales.csv')
    df = df.dropna()
    low_sales = df.loc[df['Global_Sales'].idxmin()]
    print(low_sales)


t1 = threading.Thread(target=find_top)
t2 = threading.Thread(target=find_low)

t1.start()
t2.start()

t1.join()
t2.join()
end = time.time()
print(end - start)
