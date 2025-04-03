import random

options = ("rock","paper","scissor")
user = None
computer = random.choice(options)

user = input("enter the the option given:")
print(f"user:{user}")
print(f"computer:{user}")

def comp():
    if user == computer:
        print("tie")
    elif user == "rock" and computer == "scissor":
        print("user win")
    elif user == "paper" and computer == "rock":
        print("you win")
    elif user == "rock" and computer == "scissor":
        print("you win")
    else:
        print("lose")

