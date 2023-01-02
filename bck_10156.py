#과자 한개 가격 k       30
#사려고 하는 과자 개수 n 4
#현재 가진 돈의 액수 m   100

#30*4 = 120 - 100 = 20

k, n, m = map(int, input().split())
value = k*n-m
if value<0:
    print(0)
else:
    print(value) 


