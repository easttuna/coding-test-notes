
# 10:40 ~
# 30분

# 식량창고가 일직선으로 있음
# 각 창고에 정해진 수량의 식량, 선택적으로 약탈할거임
# 좌우 인접 창고 약탈시 들킴 


n = int(input())
k =  list(map(int, input().split()))

# 좌측부터 늘려가며 최대 식량 구함.

dp = [0] * (n+1)

dp[0] = k[0]
dp[1] = k[1]

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + k[i])

print(dp[n-1])



