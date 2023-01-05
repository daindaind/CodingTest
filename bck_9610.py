count = int(input())
q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0
for i in range(count):
    a, b= map(int, input().split())
    if (a==0 or b==0):
        axis+=1
    elif (a>0 and b>0):
        q1+=1
    elif (a>0 and b<0):
        q4+=1
    elif (a<0 and b>0):
        q2+=1
    elif (a<0 and b<0):
        q3+=1

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("Q4:", q4)
print("AXIS:", axis)