import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from prices-clawer import get_player_market_value
import re

# 讀取CSV檔案
df = pd.read_csv(r"fc-mobile-player-prices.csv")

def remove_leading_zeros(s: str) -> str:
    return re.sub(r'\b0+(?!0)(\d+)\b', r'\1', s)

# 爬取的目標URL
url_initial = 'https://renderz.app/24/player/'

# 獲取當前時間，並格式化作為新列名
current_time = str(datetime.now().strftime("%Y-%m-%d %H:%M"))
current_time = remove_leading_zeros(current_time)
print(current_time)    
prices = []
for player,code in zip(df["player name"],df['code']):
    url = url_initial + str(code)
    market_value = str(get_player_market_value(url))
    prices.append(market_value)
# 將 prices 列表中的值賦給 df[current_time] 列
df[current_time] = prices
df.to_csv(r"fc-mobile-player-prices.csv", index=False)
print(df)
