
# 거리의 제곱합을 최소화
# a,b,c위치가 있을 때 거리의 제곱합은 3x^2 - 2(a+b+c)x + (a^2+b^2+c^2)
# convex한 2차함수 이므로, 최소지점이 결정되어있음
# 해당 지점은 실수로 (a+b+c) /len(loc) 이며, 여기서 가장 가까운 원소를 찾는다. --> 틀린접근.. 실수세계가 아님

n = int(input())
loc =  sorted(list(map(int, input().split())))
print(loc[((n-1) // 2)])
