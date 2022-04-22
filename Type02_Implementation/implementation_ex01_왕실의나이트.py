# 시작: 16:32 4.12(화)
# 종료: 16:50
# 제한시간: 20 (-2)
 
# 8x8 체스판

# 나이트의 이동가능 경우
# 수평 2칸: (2, 1) (2, -1) (-2, 1) (-2, -1)
# 수직 2칸: (1, 2) (1, -2) (-1, 2) (-1, -2)

# 행은 1~8, 열은 a~h

# 예시입력 a1
loc = input()

row = int(loc[1])  # 행위치
col_encoder = {k:v for k,v in zip('abcdefgh', range(1,9))}
col = col_encoder[loc[0]]

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

count = 0
for step in steps:
    r = row + step[0]
    c = col + step[1]
    if r in range(1,9) and c in range(1,9):
        count += 1 

print(count)