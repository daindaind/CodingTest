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


from sys import stdin
from collections import deque
input = stdin.readline

r, c = map(int, input().split())  # r: 행, 열: c
board = [list(input().strip()) for i in range(r)]    # 호수 전체

water_q1, water_q2 = deque(), deque()   #water_q2 : 물이랑 닿아있는 얼음 좌표
swan_q1, swan_q2 = deque(), deque()     #swan_q2 : 다른 백조를 찾아가는 길에 막힌 좌표

water_check = [[False]*c for _ in range(r)]
swan_check = [[False]*c for _ in range(r)]
swan2_x, swan2_y = 0, 0   # 두번째 백조의 좌표 (-> 도착 위치)


# 백조 좌표, 물 좌표 저장
for i in range(r):
    for j in range(c):
        if board[i][j] == 'L':
            if not swan_q1:             # swan_q1이 비어있으면 다음을 실행 (찾아가는 백조 한마리 위치만 저장)
                swan_q1.append((i,j))   # swan_q1에 백조가 있는 좌표 넣기
                swan_check[i][j] = True # swan_check에서 현재 확인 중인 좌표에 True 넣기

            else:
                swan2_x, swan2_y = i, j # 아니라면 현재 좌표를 swan2_x, swan2_y 로 표현
            board[i][j] = '.'           # 현재 확인 중인 좌표에 (백조가 있는 모든 좌표에) 물 넣기

        if board[i][j] == '.':          # 만약 호수에서 현재 확인 중인 좌표에 있는 것이 물이라면
            water_q1.append((i,j))      # water_q1에 그 좌표 넣기
            water_check[i][j] = True    # water_check에서 현재 확인 중인 좌표에 True 넣기


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


#만날 수 있는지 확인
def check():
    while swan_q1:
        x, y = swan_q1.popleft()   # 첫번째 백조가 있는 곳
        if x == swan2_x and y == swan2_y:  # 만약 두번째 백조를 가로막는 좌표가 첫번째 백조가 있는 곳과 같다면
            return True                    # 만날 수 있다 => True 반환
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]      
            if ( 0 <= nx < r ) and ( 0 <= ny < c ) and swan_check[nx][ny]==False:  #nx와 ny가 board 안에서 표현되고, nx, ny 좌표에 있는 것이 첫번째 백조가 아니라면 다음을 실행
                if board[nx][ny] == '.':
                    swan_q1.append((nx, ny))  # nx, ny 좌표가 물이 있는 곳이라면 그 곳은 첫 번째 백조가 갈 수 있는 곳
                else:
                    swan_q2.append((nx, ny))  # nx, ny 좌표가 얼음이 있는 곳이라면 그 곳은 다른 백조를 찾아가는 길에 막힌 곳임

                swan_check[nx][ny] = True     # 확인한 곳은 True로 표시

    return False # 이걸 다 반복했는데 첫번째 백조가 있는 곳과 두번째 백조가 만나지 못했다 => False 반환 (만나지 못한다)




def melt():
    while water_q1:
        x, y = water_q1.popleft()
        board[x][y] = '.'
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < r) and (0 <= ny < c) and water_check[nx][ny]==False:
                if board[nx][ny] == '.':
                    water_q1.append((nx, ny))
                else:
                    water_q2.append((nx, ny))
                water_check[nx][ny] = True


answer = 0

while True:
    melt()
    if check():  #만날때까지 반복
        break
    water_q1 = water_q2  #얼음이 있는 위치를 녹여서 물로
    swan_q1 = swan_q2    #얼음이 있는 위치를 녹여서 물로 -> 백조 이동 가능
    water_q2, swan_q2 = deque(), deque()   #얼음 있는 곳 초기화 (함수를 통해 다시 확인 가능)
    answer += 1

print(answer)



# board (호수)
#    0     1
#0 [['.', 'L'], 
#1 ['.', '.'], 
#2 ['X', 'X'], 
#3 ['X', 'X'], 
#4 ['X', 'X'], 
#5 ['X', 'X'], 
#6 ['X', 'X'], 
#7 ['X', 'X'], 
#8 ['.', '.'], 
#9 ['.', 'L']]










# -------------------------------------------------------
# def DFS(start_node):
#     stack = [start_node, ]

#     while True:
#         if len(stack) == 0:
#             print('All node searched')
#             return None
        
#         node = stack.pop()

#         if node == target:
#             print('The target fount')
#             return node

#         children = expand(node)
#         stack.expand(children)


# def BFS(start_node):
#     queue = [start_node, ]

#     while True:
#         if len(queue) == 0:
#             print('All node searched')
#             return None

#         node = queue.pop(0)

#         if node == target:
#             print('The target found')
#             return node

#         children = expand(node)
#         queue.expand(children)

#---------------------------------------------------