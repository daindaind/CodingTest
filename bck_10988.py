# word = input()

# answer=0
# for i in range(len(word)):
#     if (word[i] == word[(len(word)-1)-i]):
#         answer=1
#     else:
#         answer=0
# print(answer)

word = list(input())

if list(reversed(word)) == word:
    print(1)
else:
    print(0)
