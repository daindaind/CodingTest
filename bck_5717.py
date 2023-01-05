
list = []
boolean = True
while (boolean):
    a, b = map(int, input().split())
    if (a==0 and b==0):
        boolean=False
    elif (a>0 and b>0):
        list.append(a+b)

for i in list:
    print(i)
