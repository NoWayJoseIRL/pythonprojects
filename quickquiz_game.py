#Quiz for my resume
print ("Welcome to my quiz!")
print ("Instructions:")
print ("Always type in lower cases")
print ("Simpler answers are the best!")

playing = input("Do you want to play the game? ")

if playing != "yes":
    quit()

print("The game shall begin!")
score = 0

answer = input("What code format is .py? ")
if answer == "python":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is 2 + 2? ")
if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("Would you hire me? ")
if answer == "yes":
    print("Correct, please contact me!!")
    score += 100
else:
    print("Incorrect")

print ("You got " + str(score) + " questions correct")
print ("You got " + str((score / 4) * 10000) + "%, here is my email you deserve it! jmendozah94#22@gmail.com.")