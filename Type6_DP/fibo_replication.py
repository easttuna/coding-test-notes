
# 1) 동일한 함수가 반복되어 호출되어 연산량이 기하급수적으로 증가함
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))


# top-down 다이나믹 프로그래밍 
# 재귀적으로 구현한 피보나치 수열
d = [0] * 100
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

# bottom-up 다이나믹 프로그래밍 
# 재귀적으로 구현한 피보나치 수열
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])
