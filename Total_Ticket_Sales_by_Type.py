import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# ファイルパスとシート名
data_path = '/Users/eusyoicloud.com/Desktop/プログラミング特訓/データ分析/movie.xlsx'
sheet_name = "工作表1"

# エクセルデータを読み込む
df = pd.read_excel(data_path, sheet_name=sheet_name)

# "Category"列の最初のジャンルだけを抽出
df['Category'] = df['Category'].apply(lambda x: x.split(',')[0] if isinstance(x, str) else x)

# 必要な列を取得して集計
grouped_data = df.groupby('Category')['總票數 Total number of votes'].sum().reset_index()

# 列名を英語に変換
grouped_data.columns = ['Genre', 'Total Votes']

# 棒グラフの作成
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['Genre'], grouped_data['Total Votes'], color='skyblue')

# 通常の数値形式に変更
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))

# グラフの装飾
plt.title('Total Revenue by Genre', fontsize=14)
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Total Votes', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()

# グラフの表示
plt.show()
