# 맨해튼 거리 2이하.
# 막혀있는 곳을 제외하고 2칸 이동했는데-> 다른 응시자 발견시 거리두기 x
# 모든 P에 대해 반복

# 위치와 이동 카운트를 큐에 넣어 탐색


from collections import deque

def distancing(place):
    dr = (1, -1 , 0, 0)
    dc = (0, 0, 1, -1)
    queue = deque()
    # 사람 인덱스 생성

    for r_idx, row in enumerate(place):
        for c_idx, location in enumerate(row):
            if location == 'P':
                queue.append((r_idx, c_idx, 0, r_idx, c_idx))   
    while queue:
        cur_loc = queue.popleft()   
        for i in range(4):
            new_loc = (cur_loc[0]+dr[i], cur_loc[1]+dc[i], cur_loc[2]+1, cur_loc[3], cur_loc[4])
            move_cnt = new_loc[2]

            if new_loc[0] not in range(5) or new_loc[1] not in range(5):  # 범위 벗어날 시 continue
                continue

            if place[new_loc[0]][new_loc[1]] == 'P':
                if new_loc[0] != new_loc[3] or new_loc[1] != new_loc[4]:
                    return False

            elif place[new_loc[0]][new_loc[1]] == 'O':
                if move_cnt < 2:
                    queue.append(new_loc)
            else:  # 'X'
                continue
    return True


def solution(places):
    answer = []
    for place in places:
        answer.append(int(distancing(place)))
    return answer

