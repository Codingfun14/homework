def search():
    print ("the places you can look for the temple are in the rainforest, the temple, or you could go gather supplies")
    choice1 = input("type r for rain forest, d for the desert, and s to go gather supplies")
    if choice1 == "r":
        print("you search for the temple and end up being found by wolves who make you there lunch. Better luck next time")
        intro()
    elif choice1 == "d":
        print("you found the temple and decide to head inside")
        temple()
    elif choice1 == "s":
        print("you go back and find the supplies where you have a map that tells you to go into the desert to find the temple and you head to the desert")
        temple()




def intro():
    print ("Welcome to the life of an explorer game!!! you are a explorer you is looking for an artifact in a temple but you cannot find the temple so where will you look")
    search()

def temple():
    print("you enter the temple and find a couple of ways to go you could go down corridor 1 or 2, or you could look at the pictures on the walls")
    choice2 = input("if corridor one type c-one, if corridor two type c-two, if pictures type p")
    if choice2 == "c-one":
        print("you have gone into the corridor and find the secret artifactttt")
    elif choice2 == "c-two":
        print("you wal into the corridor and you die to a bunch of spikes that come out of the walls better luck next time")
    elif choice2 == "p":
        print("you examine the pictures and they tell you that there are two artifacts so be carfeul and they also tell you to go down corridor on to find the artifact and you do")