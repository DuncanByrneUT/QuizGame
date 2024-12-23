# intro for the quiz
print("Welcome to my quiz!")

playing = input("Do you want to play? ")

# after intro

# if user says anything other than yes, the code stops running
if playing.lower() != "yes":
    quit()

print("Okay!! Let's play!")

# score
score = 0

# first question

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! :(")

# <---- second question
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! :(")

# <---- third question
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! :(")

# <---- fourth question
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! :(")

print("You got " + str(score) + " questions correct!")
print("You got " + str(score/4 * 100) + "%")

