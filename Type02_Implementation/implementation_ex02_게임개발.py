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
row, col, face = map(int, input().split())

# 육지바다 정보는 row 수만큼 받음 -> dict로 저장하자
map_dict = {}
for r in range(n):
    map_dict[r] = []
    map_dict[r] = map_dict[r]+ list(map(int, input().split()))

# 방향 시퀀스 0 3 2 1 0 3 2 1...


# 방향 바꾸는 함수
def rotate():
    global face
    """
    반시계 방향으로 회전
    """
    if face == 0:
        face = 3
    else:
        face -= 1
    return None

def move_proposal(forward=True):
    global row, col, face
    x = 1 if forward else -1
    row_to, col_to = row, col
    if face == 0:
        row_to -= 1*x
    elif face == 1:
        col_to += 1*x
    elif face == 2:
        row_to += 1*x
    else:
        col_to -= 1*x
    return row_to, col_to


# 4 방향을 탐색한다
search_count = 0

total_count = 0
map_dict[row][col] = 1
total_count += 1

while True:
    rotate()  # 반시계 회전
    next_row, next_col = move_proposal()

    # 맵을 벗어나지 않을 시
    try:
        # 제안받은 곳이 육지일 시
        if map_dict[next_row][next_col] == 0:
            row, col = next_row, next_col  # 이동
            total_count += 1
            map_dict[row][col] = 1  # 이동하게된 곳 바다로 변경 
            search_count = 0  # 탐색 카운트 0초기화
        # 육지가 아니거나 가본 곳일시 search_count + 1
        else:
            search_count += 1
    # 맵을 벗어날 시
    except:
        search_count +=1

    # 4방향을 모두 탐색해본 경우
    if search_count == 4:
        next_row, next_col = move_proposal(forward=False)  # 뒤로 한칸 이동 제안

        # 이동 가능한 경우
        try:
            if map_dict[next_row][next_col] == 0:
                row, col = next_row, next_col  # 이동
                total_count += 1
                map_dict[row][col] = 1  # 이동하게된 곳 바다로 변경 
                search_count = 0  # 탐색 카운트 0초기화
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




