import random
import os

def count_inversions(puzzle_numbers):
    """逆転数 (inversion count) を計算する"""
    return sum(
        1 for i in range(len(puzzle_numbers)) 
        for j in range(i + 1, len(puzzle_numbers)) 
        if puzzle_numbers[i] > puzzle_numbers[j]
    )

def generate_solvable_puzzle():
    """解ける8パズルの盤面を生成する"""
    while True:
        puzzle_numbers = list(range(1, 9))  # 1～8の数字
        random.shuffle(puzzle_numbers)  # ランダムシャッフル
        puzzle_numbers.append("hole")  # "hole" を最後に配置

        # "hole" の位置を取得して除外
        hole_index = puzzle_numbers.index("hole")
        puzzle_numbers.remove("hole")

        # 逆転数を計算
        inversion_count = count_inversions(puzzle_numbers)

        # 解ける盤面 (逆転数が偶数)
        if inversion_count % 2 == 0:
            return ["hole" if i == hole_index else str(puzzle_numbers[i]) for i in range(9)]

def convert_to_logic_format(puzzle_state, file_path):
    """論理推論システムのフォーマットに変換し、ファイルに保存"""
    content = []
    content.append("set(para_into).")
    content.append("clear(print_kept).")
    content.append("clear(print_given).")
    content.append("list(usable).")
    content.append("EQUAL(l(hole,l(n(x),y)),l(n(x),l(hole,y))).")
    content.append("EQUAL(l(hole,l(y,l(z,l(u,l(n(w),v))))),l(n(w),l(y,l(z,l(u,l(hole,v)))))).")
    content.append("-STATE(l(n(1),l(n(2),l(n(3),l(end,l(n(4),l(n(5),l(n(6),l(end,l(n(7),l(n(8),l(hole,end)))))))))))).")
    content.append("end_of_list.")
    content.append("list(sos).")

    # パズルの状態をリスト化
    constr_list = ["STATE("]
    counter = 1

    for i, elem in enumerate(puzzle_state):
        if elem == "hole":
            constr_list.append("l(hole,")
        else:
            constr_list.append(f"l(n({elem}),")

        # 改行を入れる位置の修正
        if (i + 1) % 3 == 0 and (i + 1) != 9:
            constr_list.append("l(end,")

    # 最後の要素は `end` のみを追加
    constr_list.append("end")

    # `STATE(...)` の閉じカッコの数を正確に合わせる
    num_open_parens = sum(1 for c in constr_list if c.startswith("l("))
    constr_list.append(")" * num_open_parens + ").")
    
    content.append("".join(constr_list))
    content.append("end_of_list.")

    # ファイルに保存
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))

def main():
    """10個の解ける8パズルを生成し、ファイルに保存"""
    generated_puzzles = set()
    output_dir = "puzzle_outputs"

    # 出力ディレクトリがない場合は作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    while len(generated_puzzles) < 10:
        puzzle = tuple(generate_solvable_puzzle())  # タプル化して重複防止
        if puzzle not in generated_puzzles:
            generated_puzzles.add(puzzle)
            file_path = os.path.join(output_dir, f"puzzle_{len(generated_puzzles)}.txt")
            convert_to_logic_format(puzzle, file_path)
            print(f"Generated and saved: {file_path}")

if __name__ == "__main__":
    main()
