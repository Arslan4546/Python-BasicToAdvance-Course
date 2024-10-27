import random
target = random.randint(1,100)
while True:
    userChoice = int(input("Enter The Choice:" ))
    if(userChoice==target):
        print("Successfully Targeted!")
        break
    elif(userChoice > target):
        print("Your Choice is to hight than target! Try Again.")
    else:
        print("Your Choice is to low than target! Try Again.")

print("Game Over!")

# in this program the i use the python library  to generate randon numbers and also put some logic to guess the targeted numebr according to user choice 

