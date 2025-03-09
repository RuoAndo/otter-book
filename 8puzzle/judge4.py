import csv
import sys
import chardet

def detect_encoding(filename):
    """ファイルのエンコーディングを自動検出"""
    with open(filename, "rb") as f:
        result = chardet.detect(f.read())
    return result["encoding"]

def read_csv(filename):
    """エンコーディングを自動検出してCSVを読み込む"""
    encoding = detect_encoding(filename)
    
    try:
        with open(filename, "r", encoding=encoding, errors="replace") as csv_file:
            f = csv.reader(csv_file, delimiter=",", doublequote=True, quotechar='"', skipinitialspace=True)
            line = []
            for row in f:
                for i in row:
                    line.append(i.strip())  # 空白を削除してリストに追加
        return line
    except Exception as e:
        print(f"Error: ファイルの読み込みに失敗しました - {e}")
        sys.exit(1)

def count_inversions(puzzle_numbers):
    """逆転数 (inversion count) を計算する"""
    inversion_count = 0
    n = len(puzzle_numbers)
    
    for i in range(n):
        for j in range(i + 1, n):
            if puzzle_numbers[i] > puzzle_numbers[j]:
                inversion_count += 1
    
    return inversion_count

def main():
    # コマンドライン引数のチェック
    if len(sys.argv) < 2:
        print("Error: CSVファイルのパスを指定してください。")
        sys.exit(1)

    csv_filename = sys.argv[1]

    # CSVファイルを読み込み
    line = read_csv(csv_filename)

    # "hole" の位置を取得
    if "hole" not in line:
        print("Error: 'hole' が見つかりません。")
        sys.exit(1)

    hole_index = line.index("hole")  # "hole" のインデックス
    line.remove("hole")  # "hole" をリストから削除

    # 数値リストに変換
    try:
        puzzle_numbers = list(map(int, line))
    except ValueError:
        print("Error: 数値変換に失敗しました。CSVのフォーマットを確認してください。")
        sys.exit(1)

    # 逆転数の計算
    inversion_count = count_inversions(puzzle_numbers)

    # 結果の表示
    print(f"Inversion count: {inversion_count}")

    # 8パズルの判定 (3×3盤面用)
    if inversion_count % 2 == 0:
        print("この8パズルは解くことができます。")
    else:
        print("この8パズルは解くことができません。")

if __name__ == "__main__":
    main()
