#행렬 n*n

n, b = map(int, input().split())                      # n: 행렬 크기, b: 제곱(지수)
a = [[*map(int, input().split())] for _ in range(n)]  # a: 행렬  [[1, 2], [3, 4]]


#행렬 곱셈 과정
def mul(n, a, b):
    result = [[0 for _ in range(n)] for _ in range(n)]    #[[0, 0], [0, 0]]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000
    return result

def power(n, b, a):
    if (b == 1):
        return a
    elif (b == 2):
        return mul(n,a,a)
    else:
        tmp = power(n, b//2, a)
        if b%2 == 0: #지수부분이 짝수    ex) a^4 = ((a^2)^2)
            return mul(n, tmp, tmp)
        else:        #지수부분이 홀수    ex) a^5 = ((a^2)^2)*a
            return mul(n, mul(n, tmp, tmp), a)

result = power(n, b, a)

for row in result:
    for num in row:
        print(num%1000, end=' ')
    print()


# list = []
# for i in range(a):
#     num1, num2 = map(int, input().split())
#     list.append(num1)
#     list.append(num2)
#     for j in range(a):
#         matx[a][a] = num1
#         matx[a][a+1] = num2


# for j in range(a):



# for j in list:
#     print(j)
# matx[a][a]