# 4.26 (화)
# 40분 

# 주어진 떡을 절단기로 자름
# 설정값보다 긴떡은 잘리고, 짧은 떡은 잘리지 않음
# 손님에게 일정한 양 이상의 떡을 잘라서 줘야함

# 떡의 개수 N과 손님이 요청한 길이 M
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

answer = None
while start <= end:
    mid = (start + end) // 2
    cut_sum = sum([x-mid for x in array if x > mid])

    if cut_sum >= m:  # 떡길이의 합이 요청한 것보다 많은 경우 -> 오른쪽 탐색
        answer = mid
        start = mid + 1
    else:  # 떡길이의 합이 요청한 것보다 적은 경우 -> 왼쪽 탐색
        end = mid - 1

print(answer)