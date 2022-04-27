# 4.26 (화)
# 23:05~
# 20분

# 탐색과정, 그러나 계산결과를 저장해두는 방식
# 연산의 종류가 a,b,c,d가 있으므로 각 종류별 딕셔너리를 만들어서 메모이제이션

from collections import defaultdict, deque

x = int(input())
dp = defaultdict(int)
queue = deque()
queue.append(x)

while queue:
    n = queue.popleft()
    c_cnt = dp[n]

    if n%5 == 0:
        temp = n//5
        if temp > 0:
            queue.append(temp)
            if dp[temp] == 0:
                dp[temp] = c_cnt +1
            else:
                dp[temp] = min(c_cnt+1, dp[temp])
    if n%3 == 0:
        temp = n//3
        if temp > 0:
            queue.append(temp)
            if dp[temp] == 0:
                dp[temp] = c_cnt +1
            else:
                dp[temp] = min(c_cnt+1, dp[temp])
    if n%2 == 0:
        temp = n//2
        if temp > 0:
            queue.append(temp)
            if dp[temp] == 0:
                dp[temp] = c_cnt +1
            else:
                dp[temp] = min(c_cnt+1, dp[temp])
    if n > 1:
        temp = n-1
        queue.append(temp)
        if dp[temp] == 0:
            dp[temp] = c_cnt +1
        else:
            dp[temp] = min(c_cnt+1, dp[temp])

print(dp[1])

