#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random

POne = [random.randint(1, 50) for _ in range(10)]
PTwo = [random.randint(1, 50) for _ in range(10)]

POneW = 0
PTwoW = 0

for i in range(10):
    if POne[i] > PTwo[i]:
        POneW += 1
    elif POne[i] < PTwo[i]:
        PTwoW += 1

HOne = max(POne)
LOne = min(POne)
HOneI = POne.index(HOne)
LOneI = POne.index(LOne)

HTwo = max(PTwo)
LTwo = min(PTwo)
HTwoI = PTwo.index(HTwo)
LTwoI = PTwo.index(LTwo)

print(f"Player One = {POne}")
print(f"Player One = {PTwo}")

print(f"Player one won {POneW} times")
print(f"Player two won {PTwoW} times")

print(f"Player one's highest number is {HOne} at {HOneI}")
print(f"Player two's highest number is {HTwo} at {HTwoI}")

print(f"Player one's lowest number is {LOne} at {LOneI}")
print(f"Player two's lowest number is {LTwo} at {LTwoI}")