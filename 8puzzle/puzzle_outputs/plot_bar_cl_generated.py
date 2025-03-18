import os
import matplotlib.pyplot as plt

# ディレクトリのパス（適宜変更）
directory = "/mnt/d/otter-book/8puzzle/puzzle_outputs"

# ファイル名と最後の値を格納するリスト
data = {}

# 'cl_generated' で始まるファイルを取得
files = sorted([f for f in os.listdir(directory) if f.startswith("cl_generated")])

for filename in files:
    filepath = os.path.join(directory, filename)
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
            if lines:
                last_value = lines[-1].strip()
                try:
                    data[filename] = float(last_value)  # 数値に変換
                except ValueError:
                    print(f"警告: {filename} の最後の行は数値ではありません: {last_value}")
    except Exception as e:
        print(f"エラー: {filename} を処理中に問題が発生しました - {e}")

# グラフの描画
if data:
    plt.figure(figsize=(12, 6))
    plt.bar(data.keys(), data.values())
    plt.xticks(rotation=90)  # X軸のラベルを90度回転
    plt.ylabel("最終値")
    plt.title("cl_generated ファイルの最終値の棒グラフ")
    plt.tight_layout()
    plt.show()
else:
    print("データがありません。")
