print('Welcome to my computer quiz')

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Russia? ")
if answer.lower() == "moscow":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the color of the Saudi Arabia flag ? ")
if answer.lower() == "green":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the CEO of Apple? ")
if answer.lower() == "tim cook":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)* 100) + "%.")