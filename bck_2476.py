count = int(input())

list = []
for i in range(count):
    a, b, c = map(int, input().split())
    if a==b==c:
        value = 10000+a*1000
    elif a==b or b==c or a==c:
        if a==b:
            value = 1000+a*100
        elif b==c:
            value = 1000+b*100
        elif a==c:
            value = 1000+a*100
    else:
        if a>b>c or a>c>b:
            value = a*100
        elif b>a>c or b>c>a:
            value = b*100
        elif c>a>b or c>b>a:
            value = c*100
    list.append(value)

print(max(list))


    