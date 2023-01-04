count = int(input())

list = []
for i in range(count):
    r, e, c = map(int, input().split())
    if (e<0):
        e+=-c
        if (r>e):
            list.append("do not advertise")
        elif (r<e):
            list.append("advertise")
        elif (r==e):
            list.append("does not matter")
    else:
        if (e-c) > r:
            list.append("advertise")
        elif (e-c) == r:
            list.append("does not matter")
        elif (e-c) < r:
            list.append("do not advertise")

for j in list:
    print(j)