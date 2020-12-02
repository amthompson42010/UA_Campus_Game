##############################################################
#
# The University of Alabama Campus Game
# Created by Alexander Mark Thompson
# 
# Hosted on Github: 
# https://github.com/amthompson42010/UA_Campus_Game 
#
##############################################################


######################################################################################
#
# Level Functions
#
# These functions write what enemies/challenges or stores are present per level.
#
#######################################################################################

def riverSideLiving():
    return 0
def lakeSideLiving():
    return 0
def ridgeCrestLiving():
    return 0
def gorgasLibrary():
    return 0
def quadLevel():
    return 0
def fergLevel():
    return 0
def lakesideDining():
    return 0
def engrLevel():
    return 0
def recLevel():
    return 0
def presidentialLiving():
    return 0
def engrLibrary():
    return 0
def mcLureLibrary():
    return 0
def brunoLibrary():
    return 0
def stadiumLevel():
    return 0
def adminLevel():
    print("hello")
def musicLevel():
    return 0
def basketballLevel():
    return 0
def baseballLevel():
    return 0

###########################
#
# End of Level Functions
#
###########################

######################################
#
# Start of Character Stat Functions
#
######################################

def lakeSideStartingCharacter():
    lakeside_character = {
        "vitality": 90,
        "strength": 75,
        "special": 60,
        "health_potions": 25,
        "strength_potions": 25
    }
    return lakeside_character

def riverSideStartingCharacter():
    riverside_character = {
        "vitality": 85,
        "strength": 70,
        "special": 65,
        "health_potions": 25,
        "strength_potions": 25
    }
    return riverside_character

def presidentialStartingCharacter():
    presidential_character = {
        "vitality": 80,
        "strength": 80,
        "special": 75,
        "health_potions": 25,
        "strength_potions": 25
    }
    return presidential_character

def ridgecrestStartingCharacter():
    ridgecrest_character = {
        "vitality": 95,
        "strength": 74,
        "special": 25,
        "health_potions": 25,
        "strength_potions": 25
    }
    return ridgecrest_character

def defaultStartingCharacter():
    default_character = {
        "vitality": 75,
        "strength": 50,
        "special": 50,
        "health_potions": 10,
        "strength_potions": 10
    }
    return default_character

def generalEasyEnemy():
    return 0

def generalMediumEnemy():
    return 0

def generalHardEnemy():
    return 0

def bossEnemy():
    return 0

def bossEndEnemy():
    return 0

######################################
#
# End of Character Stat Functions
#
######################################

def startingCharacter(area):
    if(area == "lakeside"):
        return lakeSideStartingCharacter()
    elif(area == "riverside"):
        return riverSideStartingCharacter()
    elif(area == "presidential"):
        return presidentialStartingCharacter()
    elif(area == "ridgecrest"):
        return ridgecrestStartingCharacter()
    else:
        return defaultStartingCharacter()

def printMap():
    print("|----------|           |--------------|")
    print("|          |           |              |")
    print("| lakeside |===========| presidential |")
    print("|  dorms   |           | dorms        |") 
    print("|----------|           |--------------|")


def pauseMenu():
    print("(1) Continue")
    print("(2) Map")
    print("(3) Change Character")
    print("(4) Quit")
    pause_option = int(input("\nPlease select an option from above...\n"))
    #print(type(pause_option))
    if(pause_option in range(1, 5)):
        return pause_option
    else:
        print("Please enter a number 1-3 as your response.")
        pauseMenu()

def getLevel(level):
    if(level == "riverside"):
        riverSideLiving()
    elif(level == "lakeside"):
        lakeSideLiving()
    elif(level == "ridgecrest"):
        ridgeCrestLiving()
    elif(level == "gorgas"):
        gorgasLibrary()
    elif(level == "quad"):
        quadLevel()
    elif(level == "ferg"):
        fergLevel()
    elif(level == "lakesideDining"):
        lakesideDining()
    elif(level == "engr"):
        engrLevel()
    elif(level == "rec"):
        recLevel()
    elif(level == "presidential"):
        presidentialLiving()
    elif(level == "engrLib"):
        engrLibrary()
    elif(level == "mcLureLib"):
        mcLureLibrary()
    elif(level == "brunoLib"):
        brunoLibrary()
    elif(level == "stadium"):
        stadiumLevel()
    elif(level == "admin"):
        adminLevel()
    elif(level == "music"):
        musicLevel()
    elif(level == "basketball"):
        basketballLevel()
    elif(level == "baseball"):
        baseballLevel()

def getPausedState():
    paused = input("\nWould you like to pause? (yes or no)")
    if(paused == "yes" or paused == "no"):
        return paused
    else:
        print("Your input was not interpreted. Make sure to check your spelling and capitalization.")
        getPausedState()

def canMove(direction, curr_location):
    canMove = False
    if(curr_location == "lakeside"):
        if(direction == "north"):
            canMove = False
        elif(direction == "west"):
            canMove = False
        elif(direction == "south"):
            canMove = True
        elif(direction == "east"):
            canMove = True
    elif(curr_location == "presidential"):
        if(direction == "north"):
            canMove = False
        elif(direction == "west"):
            canMove = True
        elif(direction == "south"):
            canMove = True
        elif(direction == "east"):
            canMove = True
    elif(curr_location == "riverside"):
        if(direction == "north"):
            canMove = False
        elif(direction == "west"):
            canMove = True
        elif(direction == "south"):
            canMove = True
        elif(direction == "east"):
            canMove = False
    elif(curr_location == "ridgecrest"):
        if(direction == "north"):
            canMove = True
        elif(direction == "west"):
            canMove = False
        elif(direction == "south"):
            canMove = True
        elif(direction == "east"):
            canMove = True
    return canMove


def move(curr_location):
    direction = input("Which cardinal direction would you like to go? Options are north, south, east or west.")
    cordinal_direction = ["north", "south", "west", "east"]
    if(direction in cordinal_direction):
        return direction
    else:
        print('The answer you gave was not accepted. Please enter one of the choices as they show in the prompt.')
        move()

def play(character_name, character_stats, starting_location):

    starting_character = checkContinue(starting_location, character_stats)

    isMove = canMove(direction, curr_location)
    if(isMove == True)
    
    isPaused = getPausedState()
    
    if(isPaused == "yes"):
        pauseOption = pauseMenu()
        if(pauseOption == 1):
            isPaused = "no"
        elif(pauseOption == 2):
            printMap()
        elif(pauseOption == 3):
            print("working changing character")
        elif(pauseOption == 4):
            exit()

    print("testing after pause")

def getPlayerName():
    player_name = input("\nWhat will your character's name be?\n")
    return player_name

def getStartingLocation():
    starting_location = input("\nWhich dorm will you start at? Or would you like the default option?\n(example answers: ridgecrest, lakeside, riverside, presidential, default)\n")
    return starting_location

def getStartingLocation():
    starting_location = getStartingLocation()
    return starting_location

def getStartingCharacter(starting_location):
    
    print("\nHere are the stats on your character: ")
    starting_character = startingCharacter(starting_location)
    print("\nHealth: ", starting_character.get("vitality"))
    print("Strength: ", starting_character.get("strength"))
    print("Special Ability Level: ", starting_character.get("special"))
    print("Number of health potions: ", starting_character.get("health_potions"))
    print("Number of strength potions: ", starting_character.get("strength_potions"))

    return starting_character

def intro():
    print('\n')
    print(' |      |      /\\           -------\\     /\\        /\\      /\\      |-------')
    print(' |      |     /  \\         |            /  \\      /  \\    /  \\     |_______')
    print(' |      |    /----\\        |    ----   /----\\    /    \\  /    \\    |')
    print(' |______|   /      \\       |________| /      \\  /      \\/      \\   |_______')
    print('                                                                                 ')
    print('                       Created by: Alexander Mark Thompson                       ')
    info()
    
def info():
    print("\nWelcome to the adventure game through the campus of The University of Alabama!\n")
    print("This is a game that will take you through different locations at The University of Alabama.\n")
    print("The play style of this game is similar to that of the game known as Pokemon.\nYou will face different challenges with various levels of enemy battles.\nYou will create a character based off your starting location,and have stats based off of that.\nThe stats include health, strength, special ability level, and number of potions for health and strength.\nMake sure to use these values effectively or the game will be lost quickly.\n")

def checkContinue(starting_location, starting_character):
    continued = input("\nWould you like to continue with this character or swap? (yes or no)\nThis will swap your starting location as well\n")
    if(continued == "yes" or continued == "no"):
        if(continued == "yes"):
            starting_character = getStartingCharacter(starting_location)
            checkContinue(starting_character)
            return starting_character
        else:
            return starting_character
    else:
        print("Please enter a valid answer. (yes or no)")
        checkContinue(starting_location, starting_character)

def main():
    intro()
    player_name = getPlayerName()
    starting_location = getStartingLocation()
    print("\nWelcome {}!\n".format(player_name))
    starting_character = getStartingCharacter(starting_location)
    play(player_name, starting_character, starting_location)

if __name__ == "__main__":
    main() 