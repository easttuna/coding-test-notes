# 시작: 13:20분
# 종료: 13:55
# 제한시간: 30분 (초과 +5)

# 규칙
# 공포도가 x인 모험가는 최소 x명과 같은 그룹에 속해야함
# 그룹 수의 최대값을 구한다, 모든 모험가가 그륩에 속할 필요는 없다

# 풀이
# 정렬
# 공포도가 낮은 모험가부터 배정해야함
# 공포도가 높은 모험가를 나중에 추가로 배정하는 것은 새로운 그룹을 늘리는데 도움이 되지 않는다!!

# 모험가의 수 M
n = int(input())
# 모험가의 공포도 어레이
fear_levels = list(map(int, input().split()))
fear_levels.sort()

group_cnt = 0
# 대기 인원 수
queue = 0

# 낮은 모험가부터 반복
for level in fear_levels:
  # 현 대기자가 없으면, threshold 새로 부여
    if queue == 0:
        threshold = level

  # 대기열에 한명 추가
    queue += 1
  # 누적 대기자가 한계값과 같아지고, 현 level이 trheshold 이하일 때
    if queue == threshold and level <= threshold:
        group_cnt += 1  # 그룹 추가
        queue = 0  # 대기열 초기화
print(group_cnt)


# solution
# 낮은 모험가부터 반복
for level in fear_levels:
  # 현 대기자가 없으면, threshold 새로 부여
    queue += 1
  # 누적 대기자가 한계값과 같아지고, 현 level이 trheshold 이하일 때
    if queue >= level:
        group_cnt += 1  # 그룹 추가
        queue = 0  # 대기열 초기화
print(group_cnt)