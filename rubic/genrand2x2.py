import random

def generate_2x2x2_prolog_sos_block():
    # 各色4つずつ（6色）で24ステッカー
    colors = ['G', 'W', 'B', 'R', 'O', 'Y']
    full_state = [color for color in colors for _ in range(4)]

    # シャッフル
    random.shuffle(full_state)

    # Prolog形式で出力（f-string 非使用版）
    print("list(sos).")
    print("P([Z],[{}]).".format(','.join(full_state)))
    print("end_of_list.")

# 実行
generate_2x2x2_prolog_sos_block()
