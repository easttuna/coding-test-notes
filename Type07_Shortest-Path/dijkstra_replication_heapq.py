import heapq
import sys


input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 그래프 (간선 정보) 입력 리스트
graph = [list() for _ in range(n+1)]
# 최단거리 테이블 초기화
distance = [INF] * (n+1)

# 간선 정보 입력받기
for _ in range(m):
    o, d, cost = map(int, input().split())  # 기점, 종점, 비용
    graph[o].append((d, cost))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # start에 가기위한 비용 0으로 초기화
    distance[start] = 0
    while q:
        # 최단거리가 가장 짧은 노드 꺼냄
        dist, now = heapq.heappop(q)
        # 이미 처리된 경우 무시 (최단경로 테이블의 비용이 꺼낸 비용보다 낮은 경우)
        if distance[now] < dist:
            continue
        # 현 노드와 인접노드 확인
        for (d, cost) in graph[now]:
            cand_distance = dist + cost
            if cand_distance <  distance[d]:
                distance[d] = cand_distance
                heapq.heappush(q, (cand_distance, d))
# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기위한 최단 거리 출력
for i in range(n+1):
    # 도달 불가한 경우 INFINITY 출력
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])






