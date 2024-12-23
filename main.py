# intro for the quiz
print("Welcome to my quiz!")

playing = input("Do you want to play? ")

# after intro

# if user says anything other than yes, the code stops running
if playing != "yes":
    quit()

print("Okay!! Let's play!")

# first question

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect! :(")

# <---- second question
answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("Correct!")
else:
    print("Incorrect! :(")

# <---- third question
answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("Correct!")
else:
    print("Incorrect! :(")

# <---- fourth question
answer = input("What does PSU stand for? ")
if answer == "power supply unit":
    print("Correct!")
else:
    print("Incorrect! :(")
