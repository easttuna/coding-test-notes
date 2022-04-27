# 4.25
# 17:05
# 제한시간 30분 ~

# 부품이 N개, M개 종류의 부품
# 각 부품의 존재여부 출력 ex. yes no no

# 부품의 개수
n = int(input())
# 재고 입력 및 정렬
stock = sorted(map(int, input().split()))

m = int(input())
search_list = map(int, input().split())

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:  # mid 기준 왼쪽인 경우
            end = mid - 1
        else:  # mid 기준 오른쪽인 경우
            start = mid + 1
    return None

for item in search_list:
    if binary_search(stock, item, 0, n-1) is None:
        print('no', end=' ')
    else:
        print('yes', end=' ')





    
