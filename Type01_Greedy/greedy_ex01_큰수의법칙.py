# 배열의 크기 N, 덧셈횟수 M, 반복가능수 K 입력
n, m, k = map(int, input().split())

# 탐색할 배열 입력
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

# k+1 셋이 반복되는 횟수 iter
iter = m //(k+1)
# 나머지
rest = m % (k+1)

answer = (first*k+second)*iter + (second * rest)
print(answer)