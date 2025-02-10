import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as mtick
import matplotlib.image as mpimg

#　pip freeze > requirements.txt
# Load the CSV file
print("start_loading")
df = pd.read_csv(r"fc_mobile_player_prices.csv")
print(df)
# Preprocess data to make it suitable for plotting
# Convert the wide format to a long format for easier plotting
df_long = df.melt(id_vars=['player name', 'overall', 'code'],
                  var_name='date',
                  value_name='price')

# Remove rows with missing price values
df_long = df_long.dropna(subset=['price'])

# Convert 'price' to numeric values (removing commas)
df_long['price'] = df_long['price'].str.replace(',', '').astype(float)

# Convert 'date' to datetime format
df_long['date'] = pd.to_datetime(df_long['date'], format='%Y-%m-%d %H:%M')

# Create output directory if it doesn't exist
output_dir = 'prices_trend'
os.makedirs(output_dir, exist_ok=True)

# Plot price trends for each player and save the plots
for player in df_long['player name'].unique():
    player_data = df_long[df_long['player name'] == player]
    
    plt.figure(figsize=(10, 6))
    plt.plot(player_data['date'], player_data['price'], marker='o', linestyle='-', linewidth=2)
    plt.title(f'Price Trend for {player}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.xticks(rotation=45)
    plt.grid(visible=True, linestyle='--', alpha=0.6)
    plt.gca().yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x):,}'))
    plt.tight_layout()
    
    # Save the plot to the specified folder
    file_name = f'{player}_price_trend.png'
    plt.savefig(os.path.join(output_dir, file_name))
    plt.close()


# 顯示所有生成的圖片
for player in df_long['player name'].unique():
    file_path = os.path.join(output_dir, f'{player}_price_trend.png')
    if os.path.exists(file_path):
        img = mpimg.imread(file_path)
        plt.figure(figsize=(10, 6))
        plt.imshow(img)
        plt.axis('off')  # 移除坐標軸
        plt.title(f'Price Trend for {player}')
        plt.show()
