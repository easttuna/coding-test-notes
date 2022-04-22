# 4.20 (수)
# 제한시간 15분

# 내림차순!

# 수열의 길이가 주어지고 값의 범위가 1,000만 이하인 100,000이므로 계수정렬을 써보자
# (그냥 sorted() 써도됨)
n = int(input())
# 수열 입력
array = [int(input()) for _ in range(n)]

# 수의 등장횟수 저장 리스트 초기화 (최대값 100,000의 자연수로 주어짐)
MAX_VAL = 100_000
count = [0] * (MAX_VAL+1)

for i in array:
    count[i] += 1

for i in range(len(count)-1, -1, -1):
    for _ in range(count[i]):
        print(i, end=' ')






