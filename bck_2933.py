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
r, c = map(int, input().split())  
cave = [list(input().strip()) for _ in range(r)]

cnt = int(input())  #막대를 던진 횟수
height = []
for i in range(cnt):
    ht = int(input())
    height.append(ht)

print(height)
print(cave)






