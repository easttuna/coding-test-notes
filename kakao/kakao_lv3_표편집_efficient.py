class Node:
    def __init__(self, value):
        self.value = value
        self.up = None
        self.down = None
        
class Table:
    def __init__(self, size, start_pointer):
        self.head = Node(0)
        self.pointer = start_pointer
        self.trash_bin = []

        cur = self.head
        for idx in range(1, size):
            cur.down = Node(idx)
            cur.down.up = cur
            cur = cur.down

        cur = self.head
        for _ in range(start_pointer):
            cur = cur.down
        self.pointing_node = cur


    def pop(self):
        temp = self.pointing_node  # 현재 가리키고 있는 노드

        if temp == self.head:  # 현재 head이면, 
            self.head = temp.down

        if temp.down is None:  # 마지막 노드 삭제시
            self.pointing_node = temp.up  # 위 노드 가리킴
            temp.up.down = None
        elif temp.up is None:  # 첫 노드 삭제시
            self.pointing_node = temp.down  # 아래 노드 가리킴
            temp.down.up = None
        elif temp.up is None and temp.down is None:
            self.pointing_node = None
        else:
            self.pointing_node = temp.down  # 아래 노드 가리킴
            temp.down.up = temp.up
            temp.up.down = temp.down
        self.trash_bin.append(temp)


    def restore(self):
        restoring_node = self.trash_bin.pop()
        if self.pointing_node is None:
            self.head = restoring_node
            self.pointing_node = restoring_node
        elif restoring_node.up is None:
            restoring_node.down.up = restoring_node
        elif restoring_node.down is None:
            restoring_node.up.down = restoring_node
        else:
            restoring_node.up.down = restoring_node
            restoring_node.down.up = restoring_node

    def move(self, action):
            action = action.split()
            if action[0] == 'U':
                for _ in range(int(action[1])):
                    self.pointing_node = self.pointing_node.up
            else:
                for _ in range(int(action[1])):
                    self.pointing_node = self.pointing_node.down

    def display(self):
        cur = self.head
        while cur is not None:
            print(cur.value)
            cur = cur.down



def solution(n, k, cmd):
    table = Table(size = n, start_pointer=k)
    for action in cmd:
        if action == 'C':
            table.pop()
        elif action == 'Z':
            table.restore()
        else:
            table.move(action)

    answer = ['X'] * n
    cur_node = table.head
    while cur_node is not None:
        answer[cur_node.value] = 'O'
        cur_node = cur_node.down

    return ''.join(answer)

case = 8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

print(solution(*case))