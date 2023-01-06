count = int(input())

user1 = 100
user2 = 100

for i in range(count):
    num1, num2 = map(int, input().split())
    if (num1>num2):
        user2 -= num1
    elif (num1<num2):
        user1 -= num2

print(user1)
print(user2)

