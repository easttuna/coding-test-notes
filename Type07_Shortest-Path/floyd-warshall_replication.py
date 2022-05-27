
from calendar import c


INF = int(1e9)

# 노드와 간선의 갯수 입력
n = int(input())
m = int(input())

# 2차원 리스트 생성 후 무한으로 초기화
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]


# 자기 자신으로 향하는 비용은 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0


# 간선 정보 입력
for _ in range(m):
    o, d, cost = map(int, input().split())
    graph[o][d] = cost

# 플로이드 워셜 알고리즘 수향
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()