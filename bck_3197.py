# r, c = map(int, input().split())

# # . 물공간
# # X 빙판공간
# # L 백조가 있는 공간

# for i in range(r):
#     text = map(str, input().split())

# ks = [[0 for i in range(c)] for j in range(r)]

# # ks
# #[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
# #  . L      .  .   X   X   X  X    X  X    X  X    X  X    X  X    .  .    L  L

def DFS(start_node):
    stack = [start_node, ]

    while True:
        if len(stack) == 0:
            print('All node searched')
            return None
        
        node = stack.pop()

        if node == target:
            print('The target fount')
            return node

        children = expand(node)
        stack.expand(children)


def BFS(start_node):
    queue = [start_node, ]

    while True:
        if len(queue) == 0:
            print('All node searched')
            return None

        node = queue.pop(0)

        if node == target:
            print('The target found')
            return node

        children = expand(node)
        queue.expand(children)