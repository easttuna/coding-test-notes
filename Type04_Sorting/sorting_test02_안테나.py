# 15:10
# 제한시간 20분

# 집의 위치가 주어짐
# 한 위치에 복수의 집이 존재할 수 있음
# 집이있는 위치에만 설치 가능
# 안테나로부터 집까지 거리의 합이 최소가 되는 설치위치는?

n = int(input())
loc =  list(map(int, input().split()))
loc.sort()

answers = []
save = None
for point in loc:
    if point == save:
        continue
    distance = [abs(l-point) for l in loc]
    answers.append(sum(distance))
    save = point

print(loc[answers.index(min(answers))])