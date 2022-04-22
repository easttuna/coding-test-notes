# 17:53 ~
# 30분

# NxM 크기의 얼음틀
# 구멍뚫린 부분은 0 막힌곳은 1
# 뚫린부분끼리 상하좌우 붙은것은 연결
# 연결된 부분은 하나의 아이스크림이 될 때, 총 몇개의 아이스크림이 만들어지는가?

n, m = map(int, input().split())
# 얼음틀 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(r,c):
    global n, m
    # 주어진 위치가 탐색 불가능할 시 종료
    if r not in range(n) or c not in range(m):
        return False
    
    # 아직 미방문한 노드일 시
    if graph[r][c] == 0:
        graph[r][c] = 1
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)
        return True
    # 방문된 노드이면
    else:
        return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)