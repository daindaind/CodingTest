# from sys import stdin
# input = stdin.readline

# case = int(input())

# # . : 빈공간
# # * : 지나갈 수 없는 벽
# # # : 문                                                
# # $ : 죄수의 위치

# #사람 주변 문 탐색 함수 (상 하 좌 우)
#     #만약 문이 있으면 true
#     #만약 문이 없으면 false  -> 결과 끝

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def search_door(p, d):
#     for dx, dy in p:
#         nx, ny = 


# #문 주변 빈공간 탐색 함수 (상 하 좌 우)
#     #만약 빈 공간이 있으면 true
#     #만약 빈 공간이 없으면 false  -> 결과 끝




# result = []

# for i in range(case):

#     h, w = map(int, input().split())
#     prison = [list(input().strip()) for _ in range(h)]

#     door = []   #문 좌표 저장
#     people = []  #사람 좌표 저장

#     for j in range(h):
#         for k in range(w):
#             if prison[h][w] == "#":
#                 door.append((h,w))    #문이 있는 좌표 저장 (h,w)
            
#             if prison[h][w] == "$":
#                 people.append((h,w))  #사람이 있는 좌표 저장 (h,w)


# for i in result:
#     print(i)



#---------------------------------------------------
# 1 case


h, w = map(int, input().split())
prison = [list(input().strip()) for _ in range(h)]

#문 좌표 저장 함수
def find_door(h, w):
    for j in range(h):
        for k in range(w):
            if prison[j][k] == "#":
                return j, k
    return -1, -1


#사람 좌표 저장 함수
def find_people(h, w):
    for j in range(h):
        for k in range(w):
            if prison[j][k] == "$":
                return j, k
    return -1, -1



dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]



#사람 주변에 빈공간 -> 그 자리로 이동
#사람 주변에 문 -> 문 주변에 빈공간 -> 그 자리로 이동 -> 문을 빈공간(.)으로 변경

#문 주변 탐색
door = []
for i in range(h):
    for j in range(w):
        if prison[i][j] == "#":
            door.append([i, j])

print(door)



#이동 가능한 문 위치 확인
door_check = [[False]*w for _ in range(h)]
#[[False, False, False, False, False, False, False, False, False], 
# [False, False, False, False, False, False, False, False, False], 
# [False, False, False, False, False, False, False, False, False], 
# [False, False, False, False, False, False, False, False, False], 
# [False, False, False, False, False, False, False, False, False]]

# for i in range(h):
#     for j in range(w):
#         if 





fail = 0   #fail 이 2면 탈출 x 
for i in range(2):
    target_x, target_y= find_people(h, w)
    
    for dy, dx in dirs:
        ny, nx = target_y + dy, target_x + dx
        if not (0 <= ny < h and 0 <= nx <w):
            continue
        if prison[ny][nx] != "#":
            continue
        # if
        # 문 주변에 이동가능한 공간이 있는지 확인하는 함수 => 결과가 true
            #그때 사람 위치를 그 문이 있던 위치로 변경
        # 문 주변에 이동가능한 공간이 있는지 확인하는 함수 => 결과가 false
            #



