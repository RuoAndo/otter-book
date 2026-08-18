import random

lex = ['*', '+', 'a', 'b', 'c', 'x', 'y', 'z']

for _ in range(10):
    perm = lex[:]          # コピー
    random.shuffle(perm)   # ランダム並べ替え
    print("lex([" + ",".join(perm) + "]).")
