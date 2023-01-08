# #물품의 수 n   버틸 수 있는 무게 k
# #물건의 무게 w 물건의 가치 v

# #table
# #    (i)0 1 2 3 4 5 6 7   (버틸 수 있는 무게)
# #(j)                      (무게에 따른 가능한 가치)
# # 6 13  0 0 0 0 0 0 13 13 
# # 4  8  0 0 0 0 8 8 13 13 
# # 3  6  0 0 0 6 8 8 13 14
# # 5  12 0 0 0 6 8 12 13 14

# w = [6,4,3,5]
# v = [13,8,6,12]
# #table[j][i]

# #배열의 초기값 생성
# n, k = map(int, input().split())    # n:4 k:7
# stuff = [[0,0]]  #물건의 무게와 가치를 배열로 표현
# ks = [[0 for i in range(k+1)] for j in range(n+1)]

# # ks
# #[[0, 0, 0, 0, 0, 0, 0, 0],   x축: 가방의 무게
# # [0, 0, 0, 0, 0, 0, 0, 0],   y축: 물건 개수
# # [0, 0, 0, 0, 0, 0, 0, 0], 
# # [0, 0, 0, 0, 0, 0, 0, 0], 
# # [0, 0, 0, 0, 0, 0, 0, 0]]

# for k in range(n):
#     stuff.append(list(map(int, input().split())))

# #      (w) (v)
# #stuff  0  1
# #0    [[0, 0], 
# #1     [6, 13], 
# #2     [4, 8], 
# #3     [3, 6], 
# #4     [5, 12]]



# #ks  0  1  2  3  4  5  6  7
# #0 [[0, 0, 0, 0, 0, 0, 0, 0],   x축: 가방의 무게
# #1  [0, 0, 0, 0, 0, 0, 0, 0],   y축: 물건 개수
# #2  [0, 0, 0, 0, 0, 0, 0, 0], 
# #3  [0, 0, 0, 0, 0, 0, 0, 0], 
# #4  [0, 0, 0, 0, 0, 0, 0, 0]]

# for i in range(1, n+1):     # i : 1 2 3 4        (현재 물건)
#     for j in range(1, k+1): # j : 1 2 3 4 5 6 7  (현재 가방 무게)
#         weight = stuff[i][0]  # 6  4 3 5
#         value = stuff[i][1]   # 13 8 6 12

#         if j < weight:    #j: 현재 물건 (1~7)    weight: 현재 돌고있는 물건 (6)
#             ks[i][j] = ks[i-1][j]
#         else:
#             ks[i][j] = max(value + ks[i-1][j-weight], ks[i-1][j])



n, k = map(int, input().split())
stuff = [[0,0]]
ks = [[0 for i in range(k+1)] for j in range(n+1)]

for p in range(n):
    stuff.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = stuff[i][0]
        value = stuff[i][1] 

        if j < weight:
            ks[i][j] = ks[i-1][j]
        else:
            ks[i][j] = max(value + ks[i-1][j-weight], ks[i-1][j])
            
print(ks[n][k])



# for i in range(n):
#     w, v = map(int, input().split())

# listW = []    #6  4 3  5
# listV = []    #13 8 6 12
# for i in range(n):
#     w, v = map(int, input().split())
#     listW.append(w)
#     listV.append(v)


# maxList = []
# while True:
#     value = 0
#     for i in range(len(listW)):
#         if (i == len(listW)):
#             break
#         if (listW[i] <= k):
#             value += listV[i]
#             maxList.append(value)
#             value = 0
#         if (i == len(listW)-1):
#             break
#         elif (listW[i] + listW[i+1] <= k):
#             value += listV[i]
#             value += listV[i+1]
#             maxList.append(value)
#     break

# print(max(maxList))

        
        
        # if (listW[i] > k):
        #     break
        # if (weight > k):
        #     break
        # value += listV[i]
        # weight += listW[i]

            



        #     if (weight > k):
        #         maxList.append(value)
        #         break
        #     value += listV[i]
        #     weight += listW[i]  
    
# while True:
#     addW = 0
#     addV = 0
#     j=0
#     while (listW[j] < k and addW < k):
#         addW += listW[j]
#         addV += listV[j]
#         j+=1
#     maxList.append(addV)


#     for j in range(len(listW)):
#         if (listW[j] < k and addW < k):