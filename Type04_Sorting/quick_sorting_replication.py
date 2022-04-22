# 퀵정렬 소스코드 replication
import random


array = [random.randint(1,100) for _ in range(10)]
print('정렬 전 : ', array)

def quick_sort_v1(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return None
    pivot = start  # 첫 원소를 피벗으로 설정
    left = start + 1
    right = end

    # 좌가 우보다 커지면 중지
    while left <= right:
        # 왼쪽에서부터 피벗보다 큰 데이터를 찾아감
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 오른쪽에서부터 피벗보다 작은 데이터를 찾아감
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 좌우 인덱스가 엇갈리면, 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 나머지 경우, 작은데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후, 왼쪽부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

# 파이썬의 장점을 살린 퀵 정렬 소스코드
# 정통 퀵 정렬 분할 방식과 조금 다르며, 피벗과 데이터 간 비교연산 횟수가 증가해 시간적으로 비효율적
# 그러나 가독성은 더 좋다
def quick_srot_v2(array):
    # 리스트 원소의 수가 하나 이하일 시 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]  # 첫 원소를 피벗지정
    tail = array[1:]  # 나머지 어레이

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽과 오른쪽 부분에서 각기 정렬을 수행, 전체리스트 반환
    return quick_srot_v2(left_side) + [pivot] + quick_srot_v2(right_side)

quick_sort_v1(array, 0, len(array)-1)
print('정렬 후: ', array)





    