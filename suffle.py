deck = []
suits = ["♠","♣","♢","♡"]

for i in range(4):
    for j in range(1,14):
        value = str(j)
        if(j == 1):
            value = "A"
        if(j == 11):
            value = "J"
        if(j == 12):
            value = "Q"
        if(j == 13):
            value = "K"
        deck.append(f"{value} {suits[i]}")


import random
  
print ("The original deck is : " + str(deck)) 
  

for i in range(len(deck)-1, 0, -1): 
    
    j = random.randint(0, i + 1)  
    
     
    deck[i], deck[j] = deck[j], deck[i]  

print ("The shuffled deck is : " +  str(deck)) 
