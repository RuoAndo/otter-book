from itertools import product

people = ['A', 'B', 'C', 'D']

# 各人の選択肢（自分以外に対して、有罪 or 無罪）
def get_statements(person):
    result = []
    for target in people:
        if target != person:
            result.append(("says(" + person + ",G(" + target + "))",
                           "says(" + person + ",I(" + target + "))"))
    return result

# 各人の全6パターンを作成
choices_per_person = [get_statements(p) for p in people]

# 6通りずつある中から1つずつ選ぶ：6^4 = 1296通り
all_statements = product(*[sum(c, ()) for c in choices_per_person])

# 表示
count = 1
for pattern in all_statements:
    # print("%4d: P(%s). P(%s). P(%s). P(%s)." % (count, pattern[0], pattern[1], pattern[2], pattern[3]))
    print("P(%s). P(%s). P(%s). P(%s)." % (pattern[0], pattern[1], pattern[2], pattern[3]))
    count += 1
