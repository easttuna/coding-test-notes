# https://www.acmicpc.net/problem/1715
# 14:36 ~ 
# 제한시간 30분

# 최소 비교 방법!
# 누적으로 합해지므로, 큰 카드묶음일수록 나중에 합치는게 좋음
# greedy하게 현 상태에서 가장 낮은 두 카드묶음을 더한다.

from collections import deque

n = int(input())  # 카드 묶음의 개수 입력
queue = deque(sorted([int(input()) for _ in range(n)]))

answer = 0

while len(queue) >= 2:
    new_val = queue.popleft() + queue.popleft()  # 가장 작은 두 값을 꺼내 더함
    answer +=  new_val  # 덧셈 발생 횟수 추가

    inserted = False
    for idx in range(len(queue)):
        if new_val < queue[idx]:
            queue.insert(idx, new_val)
            inserted = True
            break
    if not inserted:
        queue.append(new_val)

print(answer)

        



