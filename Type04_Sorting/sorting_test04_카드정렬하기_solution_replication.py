import heapq

n = int(input())

# 힙(Heap)에 초기 카드 묶음을 삽입
heap = []
for _ in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

# 힙에 원소가 1개 남을때까지 반복
while len(heap) > 1:
    # 가장 작은 2개의 원소 꺼내기
    sum_val = heapq.heappop(heap) + heapq.heappop(heap)
    result += sum_val  # 비교횟수 업데이트
    heapq.heappush(heap, sum_val)  # 합친 묶음 삽입

print(result)
