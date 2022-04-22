
# 정렬기준: 국어 내림차 -> 영어 오름차 -> 수학 내림차 -> 이름 오름차

# 이름:0, 국어:1, 영어:2, 수학3

# 전체 학생 수 입력
n = int(input())

# 학생 이름 및 성적 입력
records = []
for _ in range(n):
    records.append(input().split())

records.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for row in records:
    print(row[0])