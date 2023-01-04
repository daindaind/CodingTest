# 맨 처음 접시 10
# 앞 접시랑 같으면 5 증가
# 앞 접시랑 다르면 10 증가

# bowl = input()     #((((     
# newBowl = bowl[1:] #(((       
# count = 10

# for i in newBowl:  #(((
#     # print(bowl[newBowl.index(i)])
#     if (bowl[newBowl.index(i)] == i):
#         count+=5
#     elif (bowl[newBowl.index(i)] != i):
#         count+=10

# # 10 +5 +5 +5
# print(count)

bowl = input()
count = 0

for i in range(len(bowl)):
    if i == 0:
        count += 10
    elif bowl[i] == bowl[i-1]:
        count += 5
    elif bowl[i] != bowl[i-1]:
        count += 10

print(count)
    