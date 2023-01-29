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

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

chang, sang = 0, 1

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
# for i in range(c-1, -1, -1):
#     print(cave[2][i])

def findSearch(target_x, target_y):
    #방문 표시 위치 리스트
    visited =  [[False]*c for _ in range(r)]
    visited[target_x][target_y] = 1
    q = deque([(target_x, target_y)])
    cave[target_x][target_y] = '.'


turn = chang
for h in height:
    h = r-h
    target_x, target_y = -1, -1
    if turn == chang:
        target_x, target_y = throwStickLeft(h)
        turn = sang
    else:
        target_x, target_y = throwStickRight(h)
        turn = chang

    if (target_x, target_y) == (-1, -1):
        continue
    #[['.', '.', '.', '.', '.', '.', '.', '.'], 
    # ['.', '.', '.', '.', '.', '.', '.', '.'], 
    # ['.', '.', '.', '.', '.', 'x', '.', '.'], 
    # ['.', '.', '.', 'x', 'x', 'x', '.', '.'], 
    # ['.', '.', '.', 'x', 'x', '.', '.', '.'], 
    # ['.', '.', 'x', '.', 'x', 'x', '.', '.'], 
    # ['.', '.', 'x', '.', '.', '.', 'x', '.'], 
    # ['.', '.', 'x', 'x', '.', '.', 'x', '.']]

#클러스터 구역 확인
for i in range(cnt):   # 던지는 횟수 만큼 반복
    visited = [[-1]*c for _ in range(r)]   #방문좌표확인 리스트
    cluster = []       
    count = 0
    for x in range(r):
        for y in range(c):
            if cave[x][y] == 'x' and visited[x][y] == -1:
                tmp = []
                q = deque()
                q.append([x, y])     #한번도 방문한 적 없는 곳이면서 미네랄이 있는 위치를 q에 넣기
                
                while q:             #미네랄이 있는 좌표가 존재하는 만큼 반복
                    px, py = q.popleft()

                    for i in range(4):
                        nx = px + dx[i]
                        ny = px + dy[i]

                        if nx<0 or nx>=r or ny<0 or ny>=c:  # 탐색하려는 부분이 동굴 범위 밖에 있을 때
                            continue
                        if visited[nx][ny] != -1:    # 방문 한적 있는 부분일 때
                            continue
                        if cave[nx][ny] == '.':      # 동굴에 x가(미네랄이) 없는 부분일 때 다시 탐색
                            continue

                        q.append([nx, ny])    # q에 미네랄이 있는 위치 입력
                        visited[nx][ny] = count  # 방문좌표확인 리스트에 0 입력
                        tmp.append([nx, ny])  # tmp 리스트에 미네랄이 있는 좌표 입력

                tmp.sort(reverse=True)  #내림차순 정렬
                cluster.append(tmp)
                count += 1




print(visited)





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
