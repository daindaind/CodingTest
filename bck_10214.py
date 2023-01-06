T = int(input())


for j in range(T):
    cntY = 0
    cntK = 0
    for i in range(9):
        y, k = map(int, input().split())
        cntY += y
        cntK += k

    if (cntY > cntK):
        print("Yonsei")
    elif (cntK > cntY):
        print("Korea")
    else:
        print("Draw")


    
    
            
