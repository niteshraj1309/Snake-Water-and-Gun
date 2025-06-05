import random
computer = random.choice([1, -1, 0])
youstr = input("input your choice: ")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]

print(f"you choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

if(computer == you):
    print("it's a draw")

else:

#     if(computer==1 and you==-1): (computer - you) = 2
#         print("you lose!")
#     elif(computer==1 and you==0): (computer - you) = 1
#         print("you win!")
#     elif(computer==-1 and you==1): (computer - you) = -2
#         print("you win!")
#     elif(computer==-1 and you==0): (computer - you) = -1
#         print("you lose!")
#     elif(computer==0 and you==1): (computer - you) = -1
#         print("you lose!")
#     elif(computer==0 and you==-1): (computer - you) = 1
#         print("you win!")
#     else:
#         print("something went wrong!")

    if((computer - you) == -1 or (computer - you) == 2):
        print("you lose!")
    else:
        print("you win!")