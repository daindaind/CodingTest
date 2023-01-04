
list = []
boolean = True
while (boolean):
    a, b = map(int, input().split())
    if (a==0 and b==0):
        boolean = False
    elif (a%b==0):
        list.append("multiple")
    elif (b%a==0):
        list.append("factor")
    else:
        list.append("neither")

for i in list:
    print(i)
