# 4.26 (화)
# 40분 

# 주어진 떡을 절단기로 자름
# 설정값보다 긴떡은 잘리고, 짧은 떡은 잘리지 않음
# 손님에게 일정한 양 이상의 떡을 잘라서 줘야함

# 떡의 개수 N과 손님이 요청한 길이 M
n, m = map(int, input().split())

heights = list(map(int, input().split()))
heights.sort()

# m의 떡을 가져가려면, m이하의 떡
cut_val = 0

while True:
    for idx in range(len(heights)):
        if heights[idx] > cut_val:
            start = idx
            break
    cutted_sum = sum([h-cut_val for h in heights[start:]])
    if cutted_sum <= m:
        break
    cut_val += 1

print(cut_val)
    




