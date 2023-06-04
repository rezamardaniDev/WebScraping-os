import pandas as pd
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


find_top()
print(26 * "*")
find_low()
end = time.time()
print(end - start)
