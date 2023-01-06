
list = []
while True:
    number = int(input())
    if (number == -1):
        break
    
    divisor = []
    for i in range(1,number):
        if (number%i == 0):
            divisor.append(i)
    if (number == sum(divisor)):
        string = str(number) + " = " + " + ".join(str(h) for h in divisor)
        list.append(string)
    elif (number != sum(divisor)):
        string = str(number) + " is NOT perfect."
        list.append(string)

for j in list:
    print(j)
