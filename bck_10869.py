def 덧셈(a,b):
    return a+b
def 뺄셈(a,b):
    return a-b
def 곱셈(a,b):
    return a*b
def 나누기(a,b):
    return int(a//b)
def 나머지(a,b):
    return a%b
A,B=map(int, input().split())
print(덧셈(A,B))
print(뺄셈(A,B))
print(곱셈(A,B))
print(나누기(A,B))
print(나머지(A,B))