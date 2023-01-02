list = []
while 1:
    a, b = map(int, input().split())
    if a==b==0:
        break
    elif a==b:
        list.append("No")
    elif a>b:
        list.append("Yes")
    else:
        list.append("No")
for i in list:
    print(i)