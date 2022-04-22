# 12:07
# 12:20

# 연속된 문자를 한꺼번에 뒤집을 수 있음

s = input()

zero_count = 0  # 0 덩어리의 개수 저장
one_count = 0  # 1 덩어리의 개수 저장
save_point = None  # 숫자가 변화되는 지점을 찾기 위해 이전 숫자 저장

for num in s:
    # 이전 숫자와 다를 시 -> 새로운 덩어리 등장
    if num != save_point:
        # 현 숫자가 '0'이면 0 카운트 +1
        if num == '0':
            zero_count += 1
        # 나머지는 1 카운트 +1
        else:
            one_count += 1
    save_point = num  # 이전 숫자 업데이트
print(min(zero_count, one_count))

