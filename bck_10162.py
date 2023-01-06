T = int(input())

a = 300
b = 60
c = 10

list = []
time = T  #T = 100
while time:
    if (time<10):
        break
    elif (time>=a):
        time-=a
        list.append(a)
    elif (time>=b):
        time-=b
        list.append(b)
    elif (time>=c):
        time-=c
        list.append(c)

if (time==0):
    cntA = 0
    cntB = 0
    cntC = 0
    for i in list:
        if (i == 300):
            cntA += 1
        elif (i == 60):
            cntB += 1
        elif (i == 10):
            cntC += 1
    print(cntA, cntB, cntC)

else:
    print(-1)

# print(time)
# for i in list:
#     print(i)
    
