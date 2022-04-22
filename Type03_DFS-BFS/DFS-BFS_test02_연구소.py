# 18:47 ~19:17
# 제한시간 40분

# NxM크기의 직사각형 맵
# 빈칸, 벽으로 이루어짐. 벽은 칸 하나 점유
# 일부칸 바이러스 존재. 상하좌우로 퍼져나감
# 새로이 벽 '3개'를 꼭 세움
# 빈칸의 개수는 3개 이상
# 0: 빈칸 / 1: 벽 / 2: 바이러스

# ㅇ벽을 3개 세워 바이러스가 안퍼지는곳은 안전영역
# 안전영역 크기의 최대값은?


# 풀이)
# 맵의 크기가 작기대문에, 벽을 세우는 경우를 모두 적용
# 그 case에 따른 바이러스 퍼지는 값을 계산
from itertools import combinations
import copy

# 공간의 크기 입력 (3 <= N, M<=8)
n, m = map(int, input().split())

# 지도 정보 입력
lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))

# 벽 3개 생성기
def build_wall(lab_map):
    n_size, m_size = len(lab_map),len(lab_map[0]) 
    # 지도를 돌며 빈칸(0)인 후보 좌표 튜플로 저장
    empty_spots = []
    for r in range(n_size):
        for c in range(m_size):
            if lab_map[r][c] == 0:
                empty_spots.append((r,c))

    build_here = combinations(empty_spots, 3)  # 백을 세우는 조합 설정

    new_maps = []  # 벽을 세운 새 지도를 저장할 리스트
    for spots in build_here:
        temp_map = copy.deepcopy(lab_map)
        for s in spots:
            temp_map[s[0]][s[1]] = 1
        new_maps.append(temp_map)
    return new_maps

# DFS로 상하좌우 바이러스가 퍼질수있는 곳을 면적을 세며 확인
# 2인 곳에서 시작해, 0인곳을 2로 바꾸어 나감

def dfs(r, c, lab_map):
    if lab_map[r][c] != 2:
        return None

    drs = [-1,1,0,0]
    dcs = [0,0,-1,1]

    for dr, dc in zip(drs, dcs):
        n_r, n_c = r+dr, c+dc
        if n_r not in range(len(lab_map)) or n_c not in range(len(lab_map[0])):
            continue
        if lab_map[n_r][n_c] == 0:
            lab_map[n_r][n_c] = 2
            dfs(n_r, n_c, lab_map)
    return None

def safezone_counter(lab_map):
    cnt = 0
    for row in lab_map:
        for v in row:
            if v == 0:
                cnt += 1
    return cnt

answers = []
for lab_ in build_wall(lab):
    for a in range(len(lab_)):
        for b in range(len(lab_[0])):
            dfs(a, b, lab_)
            answers.append(safezone_counter(lab_))

print(max(answers))
