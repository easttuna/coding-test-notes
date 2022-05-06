
# O(V^2)의 시간복잡도를 가지고있는 다익스트라 경로탐색 구현

import sys


input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 입력
start = int(input())
# 엣지를 입력할 그래프
graph = [[] for i in range(n+1)]
# 방문 여부 기록 테이블
visited = [False] * (n+1)
# 최단거리 테이블 무한 초기화
distance = [INF] * (n+1)

# 엣지 정보 입력
for _ in range(m):
    o, d, cost = map(int, input().split())
    graph[o].append((d,cost))

def get_smallest_node():
    """
    미방문 노드 중 최단거리가 가장 짧은 노드 번호 반환
    """
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index= i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        # 현재 최단거리가 가장짧은 노드 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현노드와 연결된 타 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 최단거리가 업데이트 될 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단경로 길이 출력
for i in range(1, n+1):
    if distance[i] == INF:  # 도달 할 수 없는 경우
        print('INFINITY')
    else:  # 도달 가능한 경우 거리 출력
        print(distance[i])

    
    