print("Welcome to the adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!")
print()

userName = input("What is your name? ")
enemyName = input("What is your worst enemy's name? ")
superpower = input("What is your superpower? ")
userLive = input("Where do you live? ")
favFood = input("What is your favorite food? ")

print()

print("Hello", userName + "!", "Your ability to", superpower, "will make sure you never have to look at\033[31m", enemyName,"\033[0magain. Go eat", favFood, "as you walk down the streets of", userLive, "and use the power of", superpower, "for good and not evil!")