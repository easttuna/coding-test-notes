# 시작: 17:20 ~ 34 4.12(화) / 20:40~       9:06
# 종료: 
# 제한시간: 40 ()
 

# NxM 크기의 맵 각각의 칸은 육지 or 바다, 동서남북중 한곳을 바라봄
# (A,B) A는 북에서 떨어진 칸의 수, B는 서로부터 떨어진 칸의 수
# 바다는 못감

# 1. 현 위치에서 왼쪽 방향부터 탐색
# -> 아직 안가본곳, 회전하여 그곳으로 전진
# -> 가본칸 -> 회전만 하고 1번으로
# 3.  4방향 모두 가보거나 바다이면 -> 바라보는 방향 유지하고 뒤로 간뒤 1번, 뒤로도 못가면 멈춤

# 방문한 칸의 수 출력

# 첫째줄 'n m'  3<= N,M<= 50
# 둘째줄 '행 열 방향' 방향은 북동남서 (0,1,2,3)
# 셋째줄부터 육지바다 정보


# 맵크기 입력

n, m = map(int, input().split())
# 캐릭터 위치 및 방향
row, col, direction = map(int, input().split())

# 육지바다 정보는 row 수만큼 받음 -> 2차원 리스트로 저장
game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))

# 방향 바꾸는 함수
def rotate():
    global direction
    """
    반시계 방향으로 회전
    """
    if direction == 0:
        direction = 3
    else:
        direction -= 1
    return None

# 북동남서 -> 0123
def move_proposal(forward=True):
    global row, col, direction
    f = 1 if forward else -1
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    row_to = row + dr[direction]*f
    col_to = col + dc[direction]*f
    return row_to, col_to

# 4 방향을 탐색한다
total_count = 0
rotation_count = 0

# 시작점 방문지 처리 (1->2)
game_map[row][col] = 2
total_count += 1
# 안가본 육지 0, 바다 1, 가본육지 2

while True:
    rotate()  # 반시계 회전
    next_row, next_col = move_proposal()

    # 맵을 벗어나지 않을 시
    try:
        # 제안받은 곳이 육지일 시
        if game_map[next_row][next_col] == 0:
            row, col = next_row, next_col  # 이동
            total_count += 1
            game_map[row][col] = 2  # 이동하게된 곳 체크
            rotation_count = 0  # 탐색 카운트 0초기화
        # 육지가 아니거나 가본 곳일시 rotation_count + 1
        else:
            rotation_count += 1
    # 맵을 벗어날 시
    except:
        rotation_count +=1

    # 4방향을 모두 탐색해본 경우
    if rotation_count == 4:
        next_row, next_col = move_proposal(forward=False)  # 뒤로 한칸 이동 제안

        # 이동 가능한 경우
        try:
            if game_map[next_row][next_col] != 1:
                row, col = next_row, next_col  # 이동
                # 안가본곳일 때만 전체 카운트 +1
                if game_map[next_row][next_col] == 0:
                    total_count += 1
                game_map[row][col] = 2  # 이동하게된 곳 체크
                rotation_count = 0  # 탐색 카운트 0초기화
                continue
            # 이동할 곳이 바다인 경우
            else:
                break
        # 이동 불가능한 경우
        except:
            break
    else:
        pass

print(total_count)




