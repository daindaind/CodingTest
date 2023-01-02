a, b, c = map(int, input().split())
if a==b==c:
    print(10000+a*1000)
elif a==b or b==c or a==c:
    if a==b:
        print(1000+a*100)
    elif b==c:
        print(1000+b*100)
    elif a==c:
        print(1000+a*100)
else:
    if a>b>c or a>c>b:
        print(a*100)
    elif b>a>c or b>c>a:
        print(b*100)
    elif c>a>b or c>b>a:
        print(c*100)