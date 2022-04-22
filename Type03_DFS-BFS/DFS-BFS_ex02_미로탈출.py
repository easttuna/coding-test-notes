# NxM 형태의 맵
# (1,1)에 위치, 출구는 (n,m)
# 출구로 반드시 나갈수있으며, 출구로 가는 최단경로 탐색
# 괴물이 있는 곳은 0, 없는 곳은 1
# BFS를 해가면, 시행 횟수는 동일한 여러가지 경우의 수들이 기록됨
# 그중에 가장 먼저 끝부분에 닿은 횟수를 기록하면 된다.

from collections import deque


n, m = map(int, input().split()) # 미로 크기 입력

maze = []
# 괴물정보 입력
for _ in range(n):
    maze.append(list(map(int, input())))

def move(r,c):
    """
    입력받은 위치를 기준으로 움직일수 있는 위치를 반환.
    맵을 벗어나거나 괴물이 있는 곳(0)은 가지 못하므로 제외
    """
    global maze
    move_to = []
    for x, y in [(r-1, c), (r+1,c), (r, c-1), (r, c+1)]:
        if x in range(n) and y in range(m) and maze[x][y] != 0:
            move_to.append((x,y))
    return move_to

# 각 지점까지의 최소방문횟수를 더해 누적
step_count = list()
for _ in range(n):
    step_count.append([0]*m)

# 출발지점의 방문 카운트 초기화
step_count[0][0] = 1
queue = deque()
queue.append((0,0))  # 출발지점 입력

# 모든 경우를 탐색할 때까지 반복
while queue:
    loc = queue.popleft()  # 큐에서 하나 추출
    current_count = step_count[loc[0]][loc[1]]  # 해당 위치의 카운트 저장
    for r,c in move(loc[0], loc[1]):
        next_count = step_count[r][c]  # 새로 이동한 곳의 기존 카운트
        # 미방문 지이거나, 기존 카운트보다 이번 이동의 카운트가 낮을 때 업데이트.
        if next_count == 0 or current_count+1 < next_count:
            queue.append((r, c))  # 큐에 새로운 위치 추가
            step_count[r][c] = current_count+1

print(step_count[n-1][m-1])


