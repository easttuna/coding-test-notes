# 17:10 ~
# 풀이시간 30분  ()

# 1~N번의 도시, M개의 단방향 도로
# 주어진 출발도시 X에서 최단경로가 K인 타 도시의 수를 구하라

# 횟수카운트를 해가며 k만큼 움직였을때 중지하면 되므로, 
# dfs로 재귀함수로 탐색했을 때, k번 이동시 노드를 모두구할수있으나, 최단임을 어떻게 보장?
# 탐색한 곳을 기록해가면 될듯...
# k번 혹은 k번 이하로 간곳만 기억하면 됨

from collections import defaultdict, deque

# N, M, K, X 입력
n, m ,k, x = map(int, input().split())

# 단방향 도로 입력
edge_dict = defaultdict(list)
for _ in range(m):
    o,d = map(int, input().split())
    edge_dict[o].append(d)

# 노드 방문횟수 리스트 생성
visit_count = defaultdict(lambda: -1)
visit_count[x] = 0
# 큐를 생성해 시작점 추가하고
queue = deque()
queue.append(x)

while queue:
    cur_node = queue.popleft()  # 큐에서 한 원소 pop
    cur_cnt = visit_count[cur_node]  # 해당 원소의 방문 카운트 저장
    if cur_cnt == k:
        continue
    # pop한 노드로부터 향하는 모든 노드에 대해 반복
    for n_node in edge_dict[cur_node]:
        if visit_count[n_node] == -1:
            visit_count[n_node] = cur_cnt + 1
            queue.append(n_node)

answers = [node for node,cnt in visit_count.items() if cnt == k]
if len(answers) == 0:
    print(-1)
else:
    for a in sorted(answers):
        print(a)

