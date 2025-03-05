import ffn
import numpy as np
import matplotlib.pyplot as plt # 畫出累積報酬走勢圖（需要 matplotlib）

# 1. 抓取股票資料
#   - 這裡以 AAPL (蘋果) 和 MSFT (微軟) 為例，時間範圍是 2020-01-01 到 2023-01-01
data = ffn.get(
    tickers='AAPL,MSFT',        # 股票代號（用逗號分隔可一次抓多支）
    start='2016-01-01',         # 開始日期 (YYYY-MM-DD)
    end='2025-01-01'            # 結束日期 (YYYY-MM-DD)
)

# 2. 查看前幾筆資料
print("=== 資料預覽 ===")
print(data.head(), "\n")

# 3. 計算並顯示績效統計 (calc_stats)
stats = data.calc_stats()       # 會計算多種績效指標
stats.display()                 # 在終端機列印結果

# 4. 計算並顯示累積報酬
#    (將股價轉換為累積收益率)
cumulative_returns = data.to_log_returns().dropna().cumsum().apply(np.exp)
print("\n=== 累積報酬 (log return 累積) ===")
print(cumulative_returns.tail())

cumulative_returns.plot(figsize=(10, 6))
plt.title("AAPL vs MSFT - Cumulative Returns (2020-01-01 to 2023-01-01)")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend(["AAPL", "MSFT"])
plt.show()
