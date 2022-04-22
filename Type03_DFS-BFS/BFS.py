from collections import deque

# BFS는 선입선출의 queue를 사용하여 간단히 구현가능

# BFS 메서드 저의
def bfs(graph, start, visited):
    # 첫번째 노드를 첫원소로하는 큐 초기화
    queue = deque([start])
    # 방문처리
    visited[start] = True
    # queue에 원소가 남아있을 때까지 반복
    while queue:
        # 큐에서 원소를 뽑아 출력
        p = queue.popleft()
        print(p, end=' ')
        # 뽑아낸 노드에 연결된 노드를 큐에 추가
        for i in sorted(graph[p]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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
bfs(graph, 1, visited)