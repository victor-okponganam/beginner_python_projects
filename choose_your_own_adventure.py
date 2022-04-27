name = input("Type in your name")

answer = input("You are walking on a dirt road and you are faced with two paths. Which path would you like to take? (left/right)")

if answer == "right":
    answer = input("You went right and you see a river and bicycle. Do you swim or ride? (swim/ride)")
    
    if answer == 'swim':
        print("You jump into the river but get eaten by alligators. Sorry!")

    elif answer == "ride":
        print("You ride the bicycle downhill and discover the breaks do not work which leads to you crashing into a tree. Sorry!")

    else:
        print("Type a valid option")

elif answer == "left":
    answer = input("You went left and you see a man with crowbar and a car with the keys in it. Which do you choose?(man/car)")

    if answer == "man":
        print(" You walk to man to ask for direction, you tap him on the shoulder and he swings the crowbar at you. Sorry!")

    elif answer == "car":
        print("You get into the car drive on the road. The car explodes with you in it. Sorry!")

    else:
        print("Type a vlid option")
    
print("Thank you for playing,", name)