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
            if cave[ny][nx] == '.':             #동굴에 x가(미네랄이) 없는 부분일 때 다시 탐색
                continue
            if visited[ny][nx]:                 #방문 한적 있는 부분일 때 다시 탐색
                continue


            q.append((ny, nx))    #q에 미네랄이 있는 위치 입력
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

#어디까지 내려갈 수 있는지 확인
def fallHeight(minY_list):   #minY_list : [-1, -1, 5, 4, 5, 5, -1, -1]
    min_diff = max_r + 1     #max_r : 100
    for x, min_y in enumerate(minY_list):   #x : 리스트 인덱스 확인, min_y : 인덱스 x에 따른 요소
        if min_y == -1 :    #아래로 내릴 클러스터 외 다른 부분은 확인하지 않는다
            continue        

        for y in range(min_y+1, r):  #아래로 내릴 클러스터의 밑 부분들을 확인
            if cave[y][x] == 'x':                        #그 밑에 미네랄이 있으면 내려갈 수 없으니까 멈추기
                min_diff = min(min_diff, y - min_y -1)   
                break
            if y == r-1:
                min_diff = min(min_diff, y - min_y)
    return min_diff     #내려갈 수 있는 정도 반환


#클러스터를 내려주기
def fall(fall_h, visited):                  #h: 내려갈 수 있는 정도, visited: 클러스터 열의 맨 아래부분에 있는 미네랄들
    for y in range(r-1, -1, -1):
        for x in range(c):
            if not visited[y][x]:      #visited[y][x]가 False값을 가지면
                continue               #다시 반복
            cave[y][x] = '.'
            cave[y+fall_h][x] = 'x'         #내려갈 수 있는 곳까지 클러스터를 내린다
    


#창영, 상근 순서대로 던지기
turn = chang
for h in height:   #[6,6,4,3,1]
    h = r-h
    target_x, target_y = -1, -1
    if turn == chang:
        target_y, target_x = throwStickLeft(h)
        turn = sang
    else:
        target_y, target_x = throwStickRight(h)
        turn = chang

    if (target_y, target_x) == (-1, -1):    #cave에서 해당되는 좌표를 얻지 못했을 때 다시 던지기 시도
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

        fall_height = fallHeight(minY_list) #내릴 클러스터가 최대한 내려갈 수 있는 정도를 fall_height에 넣기
        fall(fall_height, visited)          #최대로 내려갈 수 있는 높이와, 내릴 클러스터의 가장 아래부분을 모은 visited를 전달
        break                               

#클러스터를 내린 결과를 출력
for row in range(r):
    for colunm in range(c):
        print(cave[row][colunm], end="")
    print()
#------------------------------------------------------------------------

#[['.', '.', '.', '.', '.', '.', '.', '.'], 
# ['.', '.', '.', '.', '.', '.', '.', '.'], 
# ['.', '.', '.', '.', '.', 'x', '.', '.'], 
# ['.', '.', '.', 'x', 'x', 'x', '.', '.'], 
# ['.', '.', '.', 'x', 'x', '.', '.', '.'], 
# ['.', '.', 'x', '.', 'x', 'x', '.', '.'], 
# ['.', '.', 'x', '.', '.', '.', 'x', '.'], 
# ['.', '.', 'x', 'x', '.', '.', 'x', '.']]

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


import sys
from collections import deque
CHANG_YOUNG, SANG_GEUN = 0, 1
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
MAX_R = 100

R, C = map(int, sys.stdin.readline().rstrip().split())
cave = []
for _ in range(R):
    cave.append(list(sys.stdin.readline().rstrip()))
    # 입력 받으면서 뭔가 할 수 있지 않을까? 
N = int(sys.stdin.readline().rstrip())
H = list(map(int, sys.stdin.readline().rstrip().split()))

# 매번 BFS 돌리는 건 에바고
# 매번 없앨 수 있는 미네랄은 한개
# 그 한개의 상하좌우에 미네랄이 있으면, 그 미네랄 섬이 떨어질 수도 있는 후보.
# 각 미네랄 섬에 대해서 BFS를 했을 때, 섬 중 최저 y 좌표를 구한다. 
# y 좌표가 0이면 break, 0이 아니면 그만큼 떨굼.
# https://chldkato.tistory.com/62

def throw_stick_from_left(h):
    for x in range(C):
        if cave[h][x] == 'x':
            cave[h][x] = '.'
            return h, x
    return -1, -1

def throw_stick_from_right(h):
    for x in range(C-1, -1, -1):
        if cave[h][x] == 'x':
            cave[h][x] = '.'
            return h, x
    return -1, -1

def print_cave():
    for row in cave:
        print(*row, sep='')

def get_cluster_visited(start_y, start_x):
    visited = [[False]*C for _ in range(R)]
    q = deque([(start_y, start_x)])
    visited[start_y][start_x] = True
    while q:
        y, x = q.popleft()
        for dy, dx in DIRS:
            ny, nx = y+dy, x+dx
            if not (0 <= ny < R and 0 <= nx < C):
                continue
            if cave[ny][nx] == '.':
                continue
            if visited[ny][nx]:
                continue
            q.append((ny, nx))
            visited[ny][nx] = True
    return visited

def get_min_y_list(visited):
    min_y_list = [-1]*C
    for x in range(C):
        for y in range(R-1, -1, -1):
            if visited[y][x]:
                min_y_list[x] = y
                break
    return min_y_list
            
def get_fall_height(min_y_list):
    min_diff = MAX_R + 1
    for x, min_y in enumerate(min_y_list):
        if min_y == -1: # 엣지 케이스
            continue
        for y in range(min_y + 1, R):
            if cave[y][x] == 'x':
                min_diff = min(min_diff, y - min_y - 1) # 처음 만난 미네랄이 5, min_y가 3이라면 1칸 내릴 수 있음
                break
            if y == R-1: # 바닥
                min_diff = min(min_diff, y - min_y) # 바닥이 5, min_y가 3이라면 2칸 내릴 수 있음
                # break # 어차피 마지막
    return min_diff

def fall(h, visited):
    # 아래서부터 내린다.
    for y in range(R-1, -1, -1):
        for x in range(C):
            if not visited[y][x]:
                continue
            cave[y][x] = '.'
            cave[y+h][x] = 'x'

turn = CHANG_YOUNG
for h in H:
    # 1 -> R-1, 2 -> R-2, ..., R -> 0
    h = R-h
    mineral_y, mineral_x = -1, -1
    if turn == CHANG_YOUNG:
        mineral_y, mineral_x = throw_stick_from_left(h)
        turn = SANG_GEUN
    else:
        mineral_y, mineral_x = throw_stick_from_right(h)
        turn = CHANG_YOUNG
    if (mineral_y, mineral_x) == (-1, -1): # 깨진 미네랄이 없을 때
        continue
    # 후보는, 없어진 미네랄의 상하좌우
    for dy, dx in DIRS:
        ny, nx = mineral_y + dy, mineral_x + dx
        if not (0 <= ny < R and 0 <= nx < C):
            continue
        if cave[ny][nx] == '.':
            continue
        # 주의. 클러스터가 떨어질 때, **그 클러스터 각 열의 맨 아래 부분 중 하나**가 바닥 또는 미네랄 위로 떨어지는 입력만 주어진다!
        visited = get_cluster_visited(ny, nx)
        
        # 오답.
        # 맨 아래 층에 있던 애들만 닿는 건 아니다!!!
        # **각 열**의 맨 아래 요소에 대해서 다 체크해야 함. 
        min_y_list = get_min_y_list(visited)
        
        if R-1 in min_y_list: # 바닥에 닿은 맨 아래 요소가 있다면
            continue
                    
        # 최저점이 바닥이 아닌 경우 == 현재 떠 있는 경우
        fall_height = get_fall_height(min_y_list)
        fall(fall_height, visited)

        # 주의. 두 개 이상의 클러스터가 동시에 떨어지는 경우는 없다. 
        break

print_cave()









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
