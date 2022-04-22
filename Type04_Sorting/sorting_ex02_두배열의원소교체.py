# 14:19
# 제한시간 20분

# 두 배열  A,B가있을 때, 최대 K번 원소를 교체하여 배열 A의 합이 최대가 되도록함
# 이때 최대 합의 값을 출력

# B에서 가장 큰값, A에서 가장 작은 값을 매번 구해서 구함
# 이때 A,B가 정렬되어있으면 연산 속도가 줄어줌
# B에서 가져온 가장 큰값보다  A에서 나갈 작은 값이 크거나 같으면 종료.


# N, K 입력
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for idx in range(k):
    if a[idx] >= b[idx]:
        break
    a[idx], b[idx] = b[idx], a[idx]

print(sum(a))
