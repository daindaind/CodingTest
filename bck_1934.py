# import sys

# count = int(sys.stdin.readline())
# list = []
# for i in range(count):
#     a, b = map(int, sys.stdin.readline().split())
#     i=1
#     while(1):
#         if i%a == 0 and i%b == 0:
#             break
#         i+=1
#     list.append(i)

# for j in list:
#     print(j)


import sys
count = int(sys.stdin.readline())

list = []
for i in range(count):
    a, b = map(int, sys.stdin.readline().split())
    aa, bb = a, b
    n=1
    while n!=0:
        n = aa%bb
        aa=bb
        bb=n
    value = (a*b)/aa
    list.append(int(value))

for j in list:
    print(j)
    
