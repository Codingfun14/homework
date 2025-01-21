import random

total_points = 0


def pointers(points):
    global total_points
    total_points = total_points + points 
    print(f"\nyou added {points} points, so now you have a total of {total_points}\n")
    points = 0


def intro():
    print ("Welcome to the life of an explorer game!!! you are a explorer you is looking for an artifact in a temple but you cannot find the temple so where will you look\n")
    search()
    
def search():
    
    print ("the places you can look for the temple are in the rainforest, the temple, or you could go gather supplies\n")
    
    choice1 = int(input("type 1 for rain forest, 2 for the desert, and 3 to go gather supplies: "))
    
    if choice1 == 1:
        print("\nyou search for the temple and end up being found by wolves who make you there lunch. Better luck next time")
        end("wolves")
    
    elif choice1 == 2:
        print("\nyou found the temple and decide to head inside")
        pointers(10)
        temple()
    
    elif choice1 == 3:
        print("\nyou go back and find the supplies where you have a map that tells you to go into the desert to find the temple and you head to the desert")
        pointers(20)
        temple()
    
    else:
        print("\n ivalid option, please try again\n")
        search()


def temple():
    print("you enter the temple and find a couple of ways to go you could go down corridor 1 or 2, or you could look at the pictures on the walls\n")
    
    choice2 = int(input("if corridor one type 1, if corridor two type 2, if pictures type 3: "))
    
    if choice2 == 1:
        print("\nyou have gone into the corridor and find the secret artifactttt\n")
        pointers(10)
        artifact1()
    
    elif choice2 == 2:
        print("\nyou walk into the corridor and you die to a bunch of spikes that come out of the walls better luck next time\n")
        end("spikes")
    
    elif choice2 == 3:
        print("\nyou examine the pictures and they tell you that there are two artifacts so be carfeul and they also tell you to go down a secret corridor to find the artifact and you do\n")
        pointers(20)
        artifact2()
    else:
        print("\n ivalid option, please try again\n")
        temple()

def artifact1():
    
    print("welcome to the artifact room !!! you can either take the artifact and run or carefully steal the aritfact with a puzzle\n")
    
    choice3 = int(input("If you want to take the aritfact and run type 1 if you want to do the puzzle type2: "))
    
    if choice3 == 1:
        
        print("\nyou take the artifact and RUNNNNNNN!!!!!\n")
        
        random_int = random.randint(1,10)
        
        if random_int == 7 or random_int == 3:
            print("you barely escaped but you realized the artifact was a fake but oh well you win \n")
            pointers(30)
            goodending()
        
        elif random_int in [1,2,4,5,6,8,9,10]:
            print("you lose, you thought you could just run hahahahaha\n")
            end("dumb decisions")
    
    elif choice3 == 2:
        print("\nYou solve the puzzle and you are taken out by a saw in the floor. Better luck next time!!\n")
        pointers(10)
        end("saw")

    else:
        print("\n ivalid option, please try again\n")
        artifact1()

def artifact2():
    
    print("You did it you found the correct temple room!!! you can either take the artifact and run or carefully steal the aritfact with a puzzle\n")
    
    choice4 = int(input("If you want to take the aritfact and run type 1 if you want to do the puzzle type2: "))
    
    if choice4 == 1:
        print("\nyou take the artifact and are immediatley dead to a floor saw. Better luck next time\n")
        pointers(-10)
        end("saw")
    
    elif choice4 == 2:
        print("\nyou take the artifact and there are no traps for you to die to so you waltz out of the temple and are now the greatest explorer congrats.\n")
        pointers(50)
        goodending()
    else:
        print("\n ivalid option, please try again\n")
        artifact2()

def end(deathmessage):
    print(f"\nYou unfortunatley died to {deathmessage}, but you had {total_points} points, \nyour point total could be in 1 of three categories\n1.10 points or less and you are a nonexplorer rank \n2.30 points or more you are a decent explorer \n3.50 points or more you are the greatest explorer!!!, \nthank you for playing my game.")

def goodending():
    print("YOU DID IT!!!!!! YOU ARE THE GREATEST EXPLORER TO EVER LIVE!!!!!!! \nI hope you had fun playing my game")


intro()





