import random

numFlips = int(input("How many flips? "))

flips = [0] * 2

i = 0
while(i<numFlips):
    flip = random.randint(0,1)
    flips[flip-1] += 1
    i += 1

print(f"Heads: {flips[0]}/{numFlips} = {flips[0]/numFlips*100}%")
print(f"Tails: {flips[1]}/{numFlips} = {flips[1]/numFlips*100}%")
