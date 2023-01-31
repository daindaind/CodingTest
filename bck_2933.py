# r, c = map(int, input().split())  
# #r: 행, c: 열

# # cave = [[*map(str, input().split())] for _ in range(r)]
# # print(cave)

# cave = [list(input().strip()) for _ in range(r)]

# # print(cave)
# # . : 빈칸, x : 미네랄
# #      0    1    2    3    4    5
# # 0 [['.', '.', '.', '.', '.', '.'], 
# # 1  ['.', '.', 'x', 'x', '.', '.'], 
# # 2  ['.', '.', 'x', '.', '.', '.'], 
# # 3  ['.', '.', 'x', 'x', '.', '.'], 
# # 4  ['.', 'x', 'x', 'x', 'x', '.']]

# #......
# #..xx..
# #..x...
# #..xx..
# #.xxxx.

# cnt = int(input())  #막대를 던진 횟수             1
# height = int(input()) #막대를 던지는 동굴의 높이   3

# #미네랄 파괴
# for i in range(c):
#     if (cave[r-height][i] == 'x'):
#         cave[r-height][i] = '.'
#         break

# #      0    1    2    3    4    5
# # 0 [['.', '.', '.', 'x', '.', '.'], 
# # 1  ['.', '.', 'x', 'x', '.', '.'], 
# # 2  ['.', '.', '.', '.', '.', '.'], 
# # 3  ['.', '.', 'x', 'x', '.', '.'], 
# # 4  ['.', 'x', 'x', 'x', 'x', '.']]

# for i in range(r-height):
#     for j in range(c):
#         if (cave[i][j] == 'x') and (cave[i+1][j] == '.'):
#             cave[i+1][j] = cave[i][j]
#             cave[i][j] = '.'

# #[['.', '.', '.', '.', '.', '.'], 
# # ['.', '.', '.', '.', '.', '.'], 
# # ['.', '.', 'x', 'x', '.', '.'], 
# # ['.', '.', 'x', 'x', '.', '.'], 
# # ['.', 'x', 'x', 'x', 'x', '.']]

# print(cave)
            


#----------------------------------------
from collections import deque
r, c = map(int, input().split())  
cave = [list(input().strip()) for _ in range(r)]

cnt = int(input())  #막대를 던진 횟수
height = [int(x) for x in input().strip().split()]  #[6,6,4,3,1]

dirs = [(-1, 0), (1,0), (0, -1), (0, 1)]
chang, sang = 0, 1
max_r = 100

# cave
#    0     1    2    3    4    5    6    7
#0 [['.', '.', '.', '.', '.', '.', '.', '.'], 
#1  ['.', '.', '.', '.', '.', '.', '.', '.'], 
#2  ['.', '.', '.', 'x', '.', 'x', 'x', '.'], 
#3  ['.', '.', '.', 'x', 'x', 'x', '.', '.'], 
#4  ['.', '.', 'x', 'x', 'x', '.', '.', '.'], 
#5  ['.', '.', 'x', '.', 'x', 'x', 'x', '.'], 
#6  ['.', '.', 'x', '.', '.', '.', 'x', '.'], 
#7  ['.', 'x', 'x', 'x', '.', '.', 'x', '.']]

#왼쪽에서 시작(창영이 차례)  
def throwStickLeft(h):
    for i in range(c):
        if (cave[h][i] == 'x'):
            cave[h][i] = '.'
            return h, i
    return -1, -1
        
        
#오른쪽에서 시작(상근이 차례)
def throwStickRight(h):
    for i in range(c-1, -1, -1):
        if (cave[h][i] == 'x'):
            cave[h][i] = '.'
            return h, i
    return -1, -1

# def findSearch(target_x, target_y):
#     #방문 표시 위치 리스트
#     visited =  [[False]*c for _ in range(r)]
#     visited[target_x][target_y] = 1
#     q = deque([(target_x, target_y)])
#     cave[target_x][target_y] = '.'


#클러스터 방문 탐색하기
def clusterVisited(start_y, start_x):   
    visited = [[False]*c for _ in range(r)]   #기록할 리스트
    q = deque([(start_y, start_x)])           #
    visited[start_y][start_x] = True          #부숴진 미네랄 상하좌우를 살펴봤을 때 미네랄이 있는 좌표

    while q:     #부숴진 미네랄 상하좌우에 또 다른 미네랄이 있을 때 (붙어있는 미네랄이 있을 때)
        y, x = q.popleft()

        for dy, dx in dirs:   #그 미네랄 상하좌우도 탐색 (또 붙어있는게 있나 살펴보기)
            ny = y+dy
            nx = x+dx

            if not (0 <= ny < r and 0 <= nx < c):  #탐색하려는 부분이 동굴 범위 밖에 있을 때 다시 탐색
                continue
            if visited[ny][nx]:                 #방문 한적 있는 부분일 때 다시 탐색
                continue
            if cave[ny][nx] == '.':             #동굴에 x가(미네랄이) 없는 부분일 때 다시 탐색
                continue

            q.append((nx, ny))    #q에 미네랄이 있는 위치 입력
            visited[ny][nx] = True  #cave 탐색 후 미네랄이 있는 곳 False -> True

    return visited  #방문 기록이 담긴 visited 리스트 반환

#각 열의 맨 아래부분의 y값
def minYList(visited):
    minY_list = [-1]*c
    for x in range(c):
        for y in range(r-1, -1, -1):
            if visited[y][x]:       #True이면
                minY_list[x] = y    #그때의 y값 저장
                break
    return minY_list


def fallHeight(minY_list):
    min_diff = max_r + 1
    


#창영, 상근 순서대로 던지기
turn = chang
for h in height:   #[6,6,4,3,1]
    h = r-h
    target_x, target_y = -1, -1
    if turn == chang:
        target_x, target_y = throwStickLeft(h)
        turn = sang
    else:
        target_x, target_y = throwStickRight(h)
        turn = chang

    if (target_x, target_y) == (-1, -1):    #cave에서 해당되는 좌표를 얻지 못했을 때 다시 던지기 시도
        continue
    #[['.', '.', '.', '.', '.', '.', '.', '.'], 
    # ['.', '.', '.', '.', '.', '.', '.', '.'], 
    # ['.', '.', '.', '.', '.', 'x', '.', '.'], 
    # ['.', '.', '.', 'x', 'x', 'x', '.', '.'], 
    # ['.', '.', '.', 'x', 'x', '.', '.', '.'], 
    # ['.', '.', 'x', '.', 'x', 'x', '.', '.'], 
    # ['.', '.', 'x', '.', '.', '.', 'x', '.'], 
    # ['.', '.', 'x', 'x', '.', '.', 'x', '.']]

    #부숴진 미네랄의 상하좌우 살피기
    for dy, dx in dirs:  #[(-1, 0), (1,0), (0, -1), (0, 1)]
        ny, nx = target_y + dy, target_x + dx
        if not (0 <= ny < r and 0 <= nx < c): 
            continue
        if cave[ny][nx] == '.':
            continue
        visited = clusterVisited(ny, nx)
        minY_list = minYList(visited)

        #클러스터를 이루는 미네랄의 각 열 맨 아래가 바닥에 닿아 있으면
        if r-1 in minY_list:    #mivY_list안에 r-1이 있으면 True
            continue

        fall_height = fallHeight(minY_list)
        fall(fall_height, visited)
        break

print(visited)
print(minY_list)

#[[False, False, False, False, False, False, False, False], 
# [False, False, False, False, False, False, False, False], 
# [False, False, False, False, False, False, False, False], 
# [False, False, False, True, True, True, False, False], 
# [False, False, False, True, True, False, False, False], 
# [False, False, True, False, True, True, False, False], 
# [False, False, False, False, False, False, False, False], 
# [False, False, False, False, False, False, False, False]]

    #[['.', '.', '.', '.', '.', '.', '.', '.'], 
    # ['.', '.', '.', '.', '.', '.', '.', '.'], 
    # ['.', '.', '.', '.', '.', 'x', '.', '.'], 
    # ['.', '.', '.', 'x', 'x', 'x', '.', '.'], 
    # ['.', '.', '.', 'x', 'x', '.', '.', '.'], 
    # ['.', '.', 'x', '.', 'x', 'x', '.', '.'], 
    # ['.', '.', 'x', '.', '.', '.', 'x', '.'], 
    # ['.', '.', 'x', 'x', '.', '.', 'x', '.']]

#[-1, -1, 5, 4, 5, 5, -1, -1]













# for i in range(cnt):   # 던지는 횟수 만큼 반복
#     visited = [[-1]*c for _ in range(r)]   #방문좌표기록
#     cluster = []       # 미네랄이 있는 좌표 리스트
#     count = 0          
#     for x in range(r):
#         for y in range(c):
#             if cave[x][y] == 'x' and visited[x][y] == -1:
#                 tmp = []
#                 q = deque()
#                 q.append([x, y])     #한번도 방문한 적 없는 곳이면서 미네랄이 있는 위치를 q에 넣기
                
#                 while q:             #미네랄이 있는 좌표가 존재하면 다음을 시작
#                     px, py = q.popleft()

#                     for i in range(4):
#                         nx = px + dx[i]
#                         ny = px + dy[i]

#                         if nx<0 or nx>=r or ny<0 or ny>=c:  # 탐색하려는 부분이 동굴 범위 밖에 있을 때 다시 탐색
#                             continue
#                         if visited[nx][ny] != -1:    # 방문 한적 있는 부분일 때 다시 탐색
#                             continue
#                         if cave[nx][ny] == '.':      # 동굴에 x가(미네랄이) 없는 부분일 때 다시 탐색
#                             continue

#                         q.append([nx, ny])    # q에 미네랄이 있는 위치 입력
#                         visited[nx][ny] = count  # 방문좌표확인 리스트에 0 입력
#                         tmp.append([nx, ny])  # tmp 리스트에 미네랄이 있는 좌표 입력

#                 tmp.sort(reverse=True)  #내림차순 정렬
#                 cluster.append(tmp)
#                 count += 1


# print(visited)  #방문좌표기록 출력
# print(cluster)  #미네랄 있는 좌표 리스트 출력
# print(cave)     #동굴 모양 출력
# print(count)    

#[[-1, -1, -1, -1, -1, -1, -1, -1], 
# [-1, -1, -1, -1, -1, -1, -1, -1], 
# [-1, -1, -1, -1, -1, -1, -1, -1], 
# [-1, -1, -1, -1, 1, -1, -1, -1], 
# [-1, -1, -1, 1, -1, -1, -1, -1], 
# [-1, -1, -1, -1, 1, -1, -1, -1], 
# [-1, -1, -1, -1, -1, -1, -1, -1], 
# [-1, -1, -1, -1, -1, -1, 6, -1]]

#[[], [[5, 4], [4, 3], [3, 4]], [], [], [], [], [[7, 6]], [], [], []]

#[['.', '.', '.', '.', '.', '.', '.', '.'], 
# ['.', '.', '.', '.', '.', '.', '.', '.'], 
# ['.', '.', '.', '.', '.', 'x', '.', '.'], 
# ['.', '.', '.', 'x', 'x', 'x', '.', '.'], 
# ['.', '.', '.', 'x', 'x', '.', '.', '.'], 
# ['.', '.', 'x', '.', 'x', 'x', '.', '.'], 
# ['.', '.', 'x', '.', '.', '.', 'x', '.'], 
# ['.', '.', 'x', 'x', '.', '.', 'x', '.']]

#10


#클러스터 바닥에서부터 내려주기
# for k in range(count):
#     clu = cluster[k]
#     n_cnt = k
#     c_b = clu[0][0]

#     if c_b == r-1:
#         continue

#     fall = 1

#     while True:
#         flag = False
#         for x, y in clu:
#             nx = x+fall
#             if nx >= r:
#                 flag = True
#                 break
#             if cave[nx][y] == 'x' and visited[nx][y] != n_cnt:
#                 flag = True
#                 break
#         if flag:
#             fall -= 1
#             break
#         fall += 1

#     for x, y in clu:
#         cave[x][y] = '.'
#         cave[x+fall][y] = 'x'


#[[-1, -1, -1, -1, -1, -1, -1, -1], 
# [-1, -1, -1, -1, -1, -1, -1, -1], 
# [-1, -1, -1, -1, -1, -1, -1, -1], 
# [-1, -1, -1, -1, 1, -1, -1, -1], 
# [-1, -1, -1, 1, -1, -1, -1, -1], 
# [-1, -1, -1, -1, 1, -1, -1, -1], 
# [-1, -1, -1, -1, -1, -1, -1, -1], 
# [-1, -1, -1, -1, -1, -1, 6, -1]]

#[[], [[5, 4], [4, 3], [3, 4]], [], [], [], [], [[7, 6]], [], [], []]

#[['.', '.', '.', '.', '.', '.', '.', '.'], 
# ['.', '.', '.', '.', '.', '.', '.', '.'], 
# ['.', '.', '.', '.', '.', 'x', '.', '.'], 
# ['.', '.', '.', 'x', 'x', 'x', '.', '.'], 
# ['.', '.', '.', 'x', 'x', '.', '.', '.'], 
# ['.', '.', 'x', '.', 'x', 'x', '.', '.'], 
# ['.', '.', 'x', '.', '.', '.', 'x', '.'], 
# ['.', '.', 'x', 'x', '.', '.', 'x', '.']]

#10









def bfs(matrix, sx, sy):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    block = [[sx, sy]]
    q = deque([[sx, sy]])
    matrix[sx][sy] = '.'

    if sx == r-1:
        down = False
    else:
        down = True

    while q:
        sx, sy = q.popleft()

        for i in range(4):
            nx, ny = sx+dx[i], sy+dy[i]
            if (0 <= nx < r) and (0 <= ny < c):
                matrix[nx][ny] = 'x'

            if nx == r-1:
                down = False
            else:
                down = True
            
            block.append([nx, ny])
            q.append([nx, ny])
            matrix[nx, ny] = '.'

    return block, down






# visited
#[[False, False, False, False, False, False, False, False], 
# [False, False, False, False, False, False, False, False], 
# [False, False, False, False, False, False, False, False], 
# [False, False, False, False, False, False, False, False], 
# [False, False, False, False, False, False, False, False], 
# [False, False, False, False, False, False, False, False], 
# [False, False, False, False, False, False, False, False], 
# [False, False, False, False, False, False, False, False]]

# print(cave)

#------------------------------------------------

# turn 1
#........
#........
#.....xx.
#...xxx..
#..xxx...
#..x.xxx.
#..x...x.
#.xxx..x.

# turn 2
#........
#........
#.....x..
#...xxx..
#..xxx...
#..x.xxx.
#..x...x.
#.xxx..x.

# turn 3
#........
#........
#.....x..
#...xxx..
#...xx...
#..x.xxx.
#..x...x.
#.xxx..x.

# turn 4
#........
#........
#.....x..
#...xxx..
#...xx...
#..x.xx..
#..x...x.
#.xxx..x.

# turn 5
#........
#........
#.....x..
#...xxx..
#...xx...
#..x.xx..
#..x...x.
#..xx..x.

# faling
#........
#........
#........
#........
#.....x..
#..xxxx..
#..xxx.x.
#..xxxxx.
