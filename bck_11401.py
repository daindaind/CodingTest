from sys import stdin
input = stdin.readline

N, K =map(int, input().split())
mod = 10**9 + 7

def Fectorial(number):
    num = 1
    for i in range(1, number+1):
        num *= i
        num %= mod
    return num

def Power(n, k):
    if (k==1):
        return n
    
    tmp = Power(n, k//2)
    if k%2: 
        return tmp * tmp * n % mod
    else:
        return tmp * tmp % mod

print(Fectorial(N)%mod * (Power(Fectorial(K)*Fectorial(N-K), mod-2))%mod)

# from sys import stdin
# input = stdin.readline

# def Fectorial(number):
#     fct = 1
#     for i in range(1, number+1):
#         fct *= i
#     return fct

# def Power(n, k):
#     if (k==1):
#         return n
#     elif (k==0):
#         return 1

#     tmp = Power(n, k//2)
#     if (k%2 == 0):
#         return tmp*tmp
#     else:
#         return n*tmp*tmp

# n, k = map(int, input().split())
# b = 10**9 + 7

# top = Fectorial(n)
# a = Fectorial(n-k) * Fectorial(k)

# # a : Fectorial(n-k) * Fectorial(k)
# print(Power(a, b-2)%b * top)


#---------------------------------------
# from sys import stdin
# input = stdin.readline

# n, k = map(int, input().split())

# #이항계수 
# # n! / k!(n-k)!

# def Fectorial(number):
#     fct = 1
#     for i in range(1, number+1):
#         fct *= i
#     return fct


# n_fct = Fectorial(n)
# k_fct = Fectorial(k)
# nk_fct = Fectorial(n-k)

# # print(n_fct)
# # print(k_fct)
# # print(nk_fct)

# bino_coff = n_fct/(k_fct*nk_fct)
# print(int(bino_coff%1000000007))


