import requests
from bs4 import BeautifulSoup

def get_player_market_value(url):
    # 發送 GET 請求取得網頁內容
    response = requests.get(url)

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找目標數據
    # market_value = soup.find('div', class_='market-data--value flex items-center space-x-2 svelte-18han0u').find('span').text
    market_value = soup.find('div', class_='market-data--value flex items-center space-x-2 svelte-1kdaqxj').find('span').text

    return market_value

if __name__ == '__main__':
    url = 'https://renderz.app/24/player/30902460'
    market_value = get_player_market_value(url)
    print(market_value)
