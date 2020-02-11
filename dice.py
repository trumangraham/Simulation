someNum = float(input("roll times: "))
print("You entered : " + str(someNum))
print(f"You entered : {someNum}")

import random
roll = random.randint(1,6)


one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

i=0
while(i < someNum):
    roll = random.randint(1,6)
    print (roll)
    i+= 1


    if (someNum == 1):
        one+=1
        print(one)
    elif(someNum == 2):
        two+=1
        print(two)
    elif(someNum == 3):
        three+=1
        print(three)
    elif(someNum == 4):
        four+=1
        print(four)
    elif(someNum == 5):
        five+=1
        print(five)
    elif(someNum == 6):
        six+= 1
        print(six)
       
print(one/someNum)
print(two/someNum)
print(three/someNum)
print(four/someNum)
print(five/someNum)
print(six/someNum)
