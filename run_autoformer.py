import os
import subprocess

# Đường dẫn chứa các chuỗi thời gian
series_dir = 'data/custom_series'

# Lọc các file bắt đầu bằng store0_
series_files = [f for f in os.listdir(series_dir) if f.startswith('store0_')]

# Chạy Autoformer cho từng file
for file in series_files:
    model_id = file.replace('.csv', '')
    cmd = [
        "python", "-u", "Autoformer/run.py",
        "--is_training", "1",
        "--train_epochs", "3",
        "--root_path", "data/custom_series/",
        "--data_path", file,
        "--model_id", f"{model_id}_96_96",
        "--model", "Autoformer",
        "--data", "custom",
        "--features", "S",
        "--target", "number_sold",
        "--seq_len", "96",
        "--label_len", "48",
        "--pred_len", "96",
        "--e_layers", "2",
        "--d_layers", "1",
        "--factor", "3",
        "--enc_in", "1",
        "--dec_in", "1",
        "--c_out", "1",
        "--des", "Exp",
        "--itr", "1"
    ]

    print(f"\n🚀 Đang huấn luyện: {model_id}")
    subprocess.run(cmd)
