
from collections import deque

def solution(board):
    size = len(board)
    max_idx = size - 1

    dp = [[dict() for _ in range(size)] for _ in range(size)]  # 방향별 최소값을 저장하는 dp테이블
   
    # 각 방향별 이동 (e: east, 동쪽으로부터 한칸 움직임)
    MOVES = {'e':(0,1), 'w':(0, -1), 's':(-1,0), 'n':(1,0)}
    # 같은 그룹의 움직임이 연속 되면 직선도로만 건설, 아닌 경우엔 코너까지 건설
    GROUP = {'e':1, 'w':1, 's':0, 'n':0}
    
    for d in MOVES.keys():  # 출발지 모든 방향 가격 0으로 초기화
        dp[0][0][d] = 0

    queue = deque()
    queue.append((0,0))  # 출발지 큐 삽입

    while queue:
        cur_loc = queue.popleft()
        for direction, (dy,dx) in MOVES.items():  # 4방향 움직임 시도
            new_loc = (cur_loc[0] + dy , cur_loc[1] + dx)
            # 새로운 location이 보드 범위를 벗어나거나 벽인 경우 넘어감
            if new_loc[0] not in range(0, size) or  \
                new_loc[1] not in range(0,size) or  \
                    board[new_loc[0]][new_loc[1]] == 1:
                continue

            pre_directions = [d for d in dp[cur_loc[0]][cur_loc[1]].keys()]  # 기존 위치에 존재하는 방향들
            temp = []
            for pre_d in pre_directions:
                pre_price = dp[cur_loc[0]][cur_loc[1]][pre_d]  # 방향에 따른 가격을 가져옴
                if GROUP[pre_d] == GROUP[direction]:  # 같은 그룹의 방향일 시 100원 추가
                    new_price = pre_price + 100
                else:  # 다른 그룹의 방향일 시 600원 추가
                    new_price = pre_price + 600
                temp.append(new_price)
            opt_price = min(temp)  # 최적의 가격만 저장

            # 위에서 구한 최적 가격이 기존 최적보다 낮으면 업데이트 (처음이어도 업데이트.)
            try:
                if opt_price < dp[new_loc[0]][new_loc[1]][direction]:
                    queue.append(new_loc)
                    dp[new_loc[0]][new_loc[1]][direction] = opt_price
            except:
                queue.append(new_loc)
                dp[new_loc[0]][new_loc[1]][direction] = opt_price

    answer = min(dp[max_idx][max_idx].values())  # 종점 좌표로 각 방향에서 온 가격중 최소값을 최종 정답으로 선택
    return answer

case = [[0,0,0],[0,0,0],[0,0,0]]
print(solution(case))


