x_list = []
y_list = []
for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for j in range(3):
    if x_list.count(x_list[j]) == 1:
        x4 = x_list[j]
    if y_list.count(y_list[j]) == 1:
        y4 = y_list[j]

print(x4, y4)


# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# x3, y3 = map(int, input().split())

# if x1>x2:
#     x4 = x1
# elif x2>x1:
#     x4 = x1
# elif x3>x2>=x1 or x3>x1>=x2:
#     x4 = x3

# if y1==y2:
#     y4 = y3
# elif y1==y3:
#     y4 = y2
# elif y2==y3:
#     y4 = y1

# print(x4, y4)