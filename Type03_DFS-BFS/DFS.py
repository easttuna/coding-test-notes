# 스택, 재귀함수 개념활용
# 재귀함수 이용시 시스템 동작 특성상 수행시간이 느려질수있음
# 이를 해결하기 위해 스택 사용하면 되나, 책의범위를 벗어나므로 코테에서는 BFS가 DFS보다 조금더 빠르게 동작한다는점을 기억

def dfs(graph, v, visited):
    # 현 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현 노드와 연결된 노드를 재귀적 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각노드의 방문여부 리스트
visited = [False] * 9
dfs(graph, 5, visited)
