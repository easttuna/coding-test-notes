# 계수정렬 소스코드 replication

import random

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [random.randint(1,100) for _ in range(10)]
print('정렬 전 : ', array)

# 초기값을 0으로 두어 모든 범위를 포괄하는 리스트 선언
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가

print('정렬 후: ')
for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')

