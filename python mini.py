print("Welcome to my computer quiz! :")

player=input("Do you wanna play? ")

if player.lower() != "yes":
    quit()

print("Let's Play :")

score = 0

answer=input("what is RAM stand for ?")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("You are wrong!")

answer=input("what is GPU stand for ?")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score+=1
else:
    print("You are wrong!")

answer=input("what is PSU stand for ?")
if answer.lower() == "power supply unit":
    print("Correct!")
    score+=1
else:
    print("You are wrong!")

answer=input("what is HDD stand for ?")
if answer.lower() == "hard disk drive":
    print("Correct!")
    score+=1
else:
    print("You are wrong!")

print("You got " + str(score) + " question correct !")
print("You got " + str((score / 4) *100)+"%")
print("thanks for using my mini project and I will gift one thing.".upper())

if score >= 3:
    from urllib.request import urlretrieve

link=input('image download link :')

fileName=input('File Name :')

urlretrieve(link,'image/'+fileName+'.jpg')

print("Thanks")


