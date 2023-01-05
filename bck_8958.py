count = int(input())

list = []
for i in range(count):
    answer = input()
    score = 0
    section = 1
    if (answer[0]=="O"):
        score+=1
    for j in range(len(answer)):
        j+=1
        if (j == len(answer)):
            break
        elif (answer[j] == "O" and answer[j-1] == "O"):
            section+=1
            score+=section
        elif (answer[j] == "O" and answer[j-1] != "O"):
            score+=1
            section=1
    list.append(score)


for k in list:
    print(k)
