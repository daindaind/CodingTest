time, minute = map(int, input().split())

if (time==0) and (minute<45):
    time=23
    minute+=15
elif (minute<45) :
    minute+=15
    time-=1
elif (minute>=45):
    minute-=45

print(time, minute)
