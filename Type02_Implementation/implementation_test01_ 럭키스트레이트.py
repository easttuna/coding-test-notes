# 14:37~45
# 제한시간: 20 (-12)

# 현재 캐릭터의 점수N
# 자릿수기준 반절, 왼쪽 자릿수합과 오른쪽자릿수합이 동일 -> 기술사용
# N은 항상 짝수자리수

# 사용가능 LUCKY, 불가능 READY 출력

n =  input()
cut = int(len(n) / 2)

left_sum = 0
right_sum = 0

for num in n[:cut]:
    left_sum += int(num)

for num in n[cut:]:
    right_sum += int(num)

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')
