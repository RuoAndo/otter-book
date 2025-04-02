import random

def generate_prolog_sos_block():
    # 各色を9個ずつ = 54個
    full_state = ['G'] * 9 + ['W'] * 9 + ['B'] * 9 + ['R'] * 9 + ['O'] * 9 + ['Y'] * 9

    # 中心インデックス（各面の中央位置）
    center_indices = [4 + i * 9 for i in range(6)]

    # 中央6個を除いた48個を抽出
    tail = [full_state[i] for i in range(54) if i not in center_indices]

    # ランダムにシャッフル
    random.shuffle(tail)

    # Prolog形式で出力
    print("list(sos).")
    print(f"P([Z],[{','.join(tail)}]).")
    print("end_of_list.")

# 実行
generate_prolog_sos_block()
