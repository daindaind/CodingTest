from sys import stdin
import sys
input = stdin.readline

def mul(n, a, b):    #n: 2(행렬크기), a: 행렬 b:지수
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j]%1000000
    return result

def power(n, k, a):
    if (k==1):
        return a
    elif (k==2):
        return mul(n, a, a)
    else:
        tmp = power(n, k//2, a)
        if (k%2 == 0):
            return mul(n, tmp, tmp)
        else:
            return mul(n, mul(n, tmp, tmp), a)

# def fibo(n):
#     tmp1 = 1
#     tmp2 = 1
#     if n>=3:
#         for i in range(n-2):
#             tmp3 = tmp2
#             tmp2 = tmp1 + tmp2
#             tmp1 = tmp3
#         return tmp2

a = [[1,1], [1,0]]
number = int(input())

result = power(2, number, a)
print(result[0][1]%1000000)
