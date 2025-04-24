import random

# 揃った状態（24ステッカー：U, R, F, D, L, B 各4ステッカー）
solved = [
    'G','G','G','G',  # U面 0-3
    'R','R','R','R',  # R面 4-7
    'W','W','W','W',  # F面 8-11
    'O','O','O','O',  # D面 12-15
    'Y','Y','Y','Y',  # L面 16-19
    'B','B','B','B'   # B面 20-23
]

# 各回転のステッカーインデックスの入れ替え（24個）
# 各関数は90度時計回りの回転をシミュレートする

def rotate_U(cube):
    f = cube.copy()
    f[0], f[1], f[2], f[3] = f[2], f[0], f[3], f[1]
    f[8], f[9], f[4], f[5], f[20], f[21], f[16], f[17] = \
        f[4], f[5], f[20], f[21], f[16], f[17], f[8], f[9]
    return f

def rotate_R(cube):
    f = cube.copy()
    f[4], f[5], f[6], f[7] = f[6], f[4], f[7], f[5]
    f[3], f[11], f[13], f[20] = f[20], f[3], f[11], f[13]
    f[1], f[9], f[15], f[22] = f[22], f[1], f[9], f[15]
    return f

def rotate_F(cube):
    f = cube.copy()
    f[8], f[9], f[10], f[11] = f[10], f[8], f[11], f[9]
    f[2], f[5], f[12], f[17] = f[17], f[2], f[5], f[12]
    f[3], f[4], f[13], f[16] = f[16], f[3], f[4], f[13]
    return f

def rotate_D(cube):
    f = cube.copy()
    f[12], f[13], f[14], f[15] = f[14], f[12], f[15], f[13]
    f[10], f[11], f[6], f[7], f[22], f[23], f[18], f[19] = \
        f[6], f[7], f[22], f[23], f[18], f[19], f[10], f[11]
    return f

def rotate_L(cube):
    f = cube.copy()
    f[16], f[17], f[18], f[19] = f[18], f[16], f[19], f[17]
    f[0], f[8], f[12], f[23] = f[23], f[0], f[8], f[12]
    f[2], f[10], f[14], f[21] = f[21], f[2], f[10], f[14]
    return f

def rotate_B(cube):
    f = cube.copy()
    f[20], f[21], f[22], f[23] = f[22], f[20], f[23], f[21]
    f[1], f[6], f[15], f[19] = f[19], f[1], f[6], f[15]
    f[0], f[7], f[13], f[18] = f[18], f[0], f[7], f[13]
    return f

# 回転関数リスト
rotations = [rotate_U, rotate_R, rotate_F, rotate_D, rotate_L, rotate_B]

# ランダムに3回回す関数
def apply_random_rotations(cube, count=3):
    for _ in range(count):
        move = random.choice(rotations)
        cube = move(cube)
    return cube

# 実行
random_state = apply_random_rotations(solved, 3)
print("list(sos).")
print("P([Z],[{}]).".format(",".join(random_state)))
print("end_of_list.")

