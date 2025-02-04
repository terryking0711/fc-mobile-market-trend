import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from prices_clawer import get_player_market_value

# 讀取CSV檔案
df = pd.read_csv(r"fc mobile player prices.csv")

# 爬取的目標URL
url_initial = 'https://renderz.app/24/player/'

# 獲取當前時間，並格式化作為新列名
current_time = str(datetime.now().strftime("%Y-%m-%d %H:%M"))
print(current_time)    
prices = []
for player,code in zip(df["player name"],df['code']):
    url = url_initial + str(code)
    market_value = str(get_player_market_value(url))
    prices.append(market_value)
# 將 prices 列表中的值賦給 df[current_time] 列
df[current_time] = prices
df.to_csv(r"diagrame_analsis.py", index=False)
print(df)
