count = int(input())

cnt1 = 0
cnt0 = 0

list=[]
for i in range(count):
    vote = int(input())
    list.append(vote)

for j in list:
    if (j==0):
        cnt0+=1
    elif (j==1):
        cnt1+=1

if (cnt1>cnt0):
    print("Junhee is cute!")
elif (cnt1<cnt0):
    print("Junhee is not cute!")