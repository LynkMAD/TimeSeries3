import pandas as pd
import os

# Đọc dữ liệu gốc
train = pd.read_csv('data/train.csv', parse_dates=['Date'])
test = pd.read_csv('data/test.csv', parse_dates=['Date'])

# Gộp lại để tạo chuỗi liên tục
df = pd.concat([train, test], ignore_index=True)

# Thư mục xuất chuỗi riêng
output_dir = 'data/custom_series'
os.makedirs(output_dir, exist_ok=True)

# Tách từng (store, product) và chỉ lấy store0
for (store, product), group in df.groupby(['store', 'product']):
    if store != 0:
        continue  # chỉ lấy store0

    group = group.sort_values('Date')
    group = group[['Date', 'number_sold']]
    group.columns = ['date', 'number_sold']
    filename = f"store{store}_product{product}.csv"
    group.to_csv(os.path.join(output_dir, filename), index=False)

print(f"✅ Đã tách xong các chuỗi cho store0 tại {output_dir}")
