from sys import stdin
import sys
input = stdin.readline


#두 행렬을 곱함
def mul(n, a, b):    #n: 2(행렬크기), a: 행렬 b:지수
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
                result[i][j] %= 1000000
    return result

#실제로 행렬을 곱함 (피보나치, 주어진 n에 대해 기본 행렬을 n번 곱함)
def matrix_mul(x, n):
    base = [[1,1], [1,0]]
    result = [[1,1], [1,0]]
    for _ in range(x):
        result = [[0,0], [0,0]]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += base[i][k] * base[k][j]
                    result[i][j] %= 1000000
        base = result

    return result


value  = int(input())
number = format(value, 'b')  # 1111101000
print(number)

result = [[1,0], [0,1]]
for i in range(len(number)):
    if number[-i-1] == '1':    #입력받은 수의 1이 있는 만큼 연산
        result = mul(2, result, matrix_mul(i, 2))
        print(result)

print(result[0][1] % 1000000)

