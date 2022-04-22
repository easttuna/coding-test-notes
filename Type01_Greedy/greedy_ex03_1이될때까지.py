n, k = map(int, input().split())

count = 0

# while n > 1:
#   # k로 나눠질 시 나눠주고 count +1
#   if  n % k == 0:
#     n = round(n/k)
#     count += 1
#   else:
#     n -= 1
#     count += 1

# print(count)


while True:
  target = (n // k) * k  # k로 나눗셈이 가능한 지점 target 설정
  count += n-target  # 뺄셈 횟수만큼 연산 횟수 추가
  n = target
 
  # k로 나눔
  n //= k
  count += 1

  if n < k:
    break

count += (n-1)
print(count)

  
