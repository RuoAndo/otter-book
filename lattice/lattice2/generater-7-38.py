import random
import itertools

lex = ['*', '+', '<=', 'x', 'y', 'z', 'u', 'a', 'b', 'c']

# 全順列からランダムに10通り選ぶ
perms = list(itertools.permutations(lex, len(lex)))
samples = random.sample(perms, 10)

for p in samples:
    print("lex([" + ",".join(p) + "]).")

