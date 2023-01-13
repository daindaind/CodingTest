from sys import stdin
input = stdin.readline

n, k = map(int, input().split())

def Power(n, k):    # 3  5
    if (k==1):
        return n
    tmp = Power(n, k//2)
    if (k%2 == 0):
        return tmp*tmp
    else:
        return n*tmp*tmp

print(Power(n, k))

 




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


