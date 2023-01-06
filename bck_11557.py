N = int(input())

list = []
for i in range(N):
    dic = {}
    nameList = []
    S = int(input())
    for j in range(S):
        name, liter = map(str, input().split())
        nameList.append(name)
        dic[name] = int(liter)

    max = nameList[0]
    for k in range(S-1):   # 0 1 2
        if dic[nameList[k+1]] > dic[max]:
            max = nameList[k+1]
    list.append(max)

for h in list:
    print(h)
