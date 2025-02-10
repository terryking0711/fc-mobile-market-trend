# FC Mobile 球員價格追蹤器

在 FC Mobile 遊戲中，我們只能透過市場內建的曲線圖來大致追蹤球員的價格走向，但無法得知具體的價格變化。因此，本專案使用爬蟲技術來定期抓取 [RenderZ](https://www.renderz.com/) 網站上的球員價格，並儲存這些數據，以供玩家進行市場趨勢分析。

## 功能特點
- **定期爬取**：使用爬蟲技術自動擷取球員價格變化。
- **歷史價格記錄**：儲存數據，讓使用者可以查看球員的價格趨勢。
- **數據可視化**：透過圖表顯示球員價格變動，幫助玩家更好地做出投資決策。
- **自訂爬取間隔**：可設定爬蟲的執行頻率。
- **數據匯出**：支援將數據匯出為 CSV 以供進一步分析。

## 安裝與使用
### 1. 環境需求
本專案使用 Python 來運行，請確保您的環境已安裝以下套件：
- Python 3.x
- `requests`
- `BeautifulSoup4`
- `pandas`
- `matplotlib` (可選，用於視覺化數據)

### 2. 安裝步驟
```bash
# 克隆本倉庫
git clone https://github.com/yourusername/fc-mobile-price-tracker.git
cd fc-mobile-price-tracker

# 安裝所需套件
pip install -r requirements.txt
```

### 3. 運行爬蟲
```bash
python tracker.py
```

### 4. 查看數據
運行完畢後，數據會被存儲於 `data/players_prices.csv`，你可以使用 Excel 或 Python 來分析數據。

如果希望可視化數據，可以運行：
```bash
python visualize.py
```

## 目錄結構
```
fc-mobile-price-tracker/
│── data/                     # 儲存爬取到的數據
│── scripts/                  # 輔助腳本
│── tracker.py                # 主要爬蟲程式
│── visualize.py              # 可視化工具
│── README.md                 # 本文件
│── requirements.txt          # 依賴套件清單
```

## 未來計劃
- [ ] 增加更多數據來源，以提高準確性。
- [ ] 建立 Web 介面，讓使用者能夠更直觀地查看數據。
- [ ] 增加通知功能，當某些球員價格變化劇烈時發送提醒。

## 貢獻
如果你對此專案有興趣，歡迎提出 issue 或提交 pull request。

