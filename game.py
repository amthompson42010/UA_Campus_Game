##############################################################
#
# The University of Alabama Campus Game
# Created by Alexander Mark Thompson
# 
# Hosted on Github: 
# https://github.com/amthompson42010/UA_Campus_Game 
#
##############################################################

import math
import random

######################################################################################
#
# Level Functions
#
# These functions write what enemies/challenges or stores are present per level.
#
#######################################################################################

# Stores
def lakesideDining(current_character):
    updated_character = store(current_character, 3, 2, 3, 1, 1, 1)
    return updated_character

def mcLureLibrary(current_character):
    updated_character = store(current_character, 3, 2, 3, 1, 1, 1)
    return updated_character

def basketballLevel(current_character):
    updated_character = store(current_character, 3, 2, 3, 1, 1, 1)
    return updated_character

# Starting Levels
def riverSideLiving():
    enemy = tutorialEnemy()
    return enemy
def lakeSideLiving():
    enemy = tutorialEnemy()
    return enemy
def ridgeCrestLiving():
    enemy = tutorialEnemy()
    return enemy
def presidentialLiving():
    enemy = tutorialEnemy()
    return enemy

# Intermediate Levels
def gorgasLibrary():
    enemy = getEnemyStats()
    return enemy
def quadLevel():
    enemy = getEnemyStats()
    return enemy
def fergLevel():
    enemy = getEnemyStats()
    return enemy
def engrLevel():
    enemy = getEnemyStats()
    return enemy
def recLevel():
    enemy = getEnemyStats()
    return enemy
def engrLibrary():
    enemy = getEnemyStats()
    return enemy
def brunoLibrary():
    enemy = getEnemyStats()
    return enemy
def adminLevel():
    enemy = getEnemyStats()
    return enemy
def musicLevel():
    enemy = getEnemyStats()
    return enemy
def baseballLevel():
    enemy = getEnemyStats()
    return enemy

# End Level
def stadiumLevel():
    boss = bossEndEnemy()
    return boss

###########################
#
# End of Level Functions
#
###########################

def attack(current_character, enemy_character, attack_type, which_enemy, active_character):
    
    curr_character_health = current_character.get("vitality")
    curr_character_strength = current_character.get("strength")
    curr_character_special = current_character.get("special")
    curr_character_health_potions = current_character.get("health_potions")
    curr_character_strength_potions = current_character.get("strength_potions")

    curr_enemy_health = enemy_character.get("vitality")
    curr_enemy_strength = enemy_character.get("strength")
    curr_enemy_special = enemy_character.get("special")

    # attack 1 = base attack
    # attack 2 = special
    # active_character 0 = you the player
    # active_character 1 = enemy

    if(attack_type == 1 and which_enemy == "tutorial" and active_character == 0):
        base_attack = 0.1 * curr_character_strength
        if(curr_enemy_health != 0):
            curr_enemy_health -= base_attack
            curr_character_strength += 1
        else:
            curr_enemy_health = curr_enemy_health
            curr_character_strength = curr_character_strength

    elif(attack_type == 2 and which_enemy == "tutorial" and active_character == 0):
        special_attack = 0.25 * curr_character_strength
        if(curr_enemy_health != 0):
            curr_enemy_health -= special_attack
            curr_character_special -= 1
        else:
            curr_enemy_health = curr_enemy_health
            curr_character_special = curr_character_special
    elif(attack_type == 1 and which_enemy == "easy" and active_character == 0):
        base_attack = 0.1 * curr_character_strength
        if(curr_enemy_health != 0):
            curr_enemy_health -= base_attack
            curr_character_strength += 1
        else:
            curr_enemy_health = curr_enemy_health
            curr_character_strength = curr_character_strength
    elif(attack_type == 2 and which_enemy == "easy" and active_character == 0):
        special_attack = 0.25 * curr_character_special
        if(curr_enemy_health != 0):
            curr_enemy_health -= special_attack
            curr_character_special -= 1
        else:
            curr_enemy_health = curr_enemy_health
            curr_character_strength = curr_character_strength
    elif(attack_type == 1 and which_enemy == "medium" and active_character == 0):
        base_attack = 0.15 * curr_character_strength
        if(curr_enemy_health != 0):
            curr_enemy_health -= base_attack
            curr_character_strength += 2
        else:
            curr_enemy_health = curr_enemy_health
            curr_character_strength = curr_character_strength
    elif(attack_type == 2 and which_enemy == "medium" and active_character == 0):
        special_attack = 0.35 * curr_character_special
        if(curr_enemy_health != 0):
            curr_enemy_health -= special_attack
            curr_character_special -= 2
        else:
            curr_enemy_health = curr_enemy_health
            curr_character_strength = curr_character_strength
    elif(attack_type == 1 and which_enemy == "hard" and active_character == 0):
        base_attack = 0.40 * curr_character_strength
        if(curr_enemy_health != 0):
            curr_enemy_health -= base_attack
            curr_character_strength += 5
        else:
            curr_enemy_health = curr_enemy_health
            curr_character_strength = curr_character_strength
    elif(attack_type == 2 and which_enemy == "hard" and active_character == 0):
        special_attack = 0.40 * curr_character_special
        if(curr_enemy_health != 0):
            curr_enemy_health -= special_attack
            curr_character_special -= 5
        else:
            curr_enemy_health = curr_enemy_health
            curr_character_strength = curr_character_strength
    elif(attack_type == 1 and which_enemy == "boss" and active_character == 0):
        base_attack = 0.45 * curr_character_strength
        if(curr_enemy_health != 0):
            curr_enemy_health -= base_attack
            curr_character_strength += 10
        else:
            curr_enemy_health = curr_enemy_health
            curr_character_strength = curr_character_strength
    elif(attack_type == 2 and which_enemy == "boss" and active_character == 0):
        special_attack = 0.50 * curr_character_special
        if(curr_enemy_health != 0):
            curr_enemy_health -= special_attack
            curr_character_special -= 10
        else:
            curr_enemy_health = curr_enemy_health
            curr_character_strength = curr_character_strength
    elif(attack_type == 1 and which_enemy == "end" and active_character == 0):
        base_attack = 0.50 * curr_character_strength
        if(curr_enemy_health != 0):
            curr_enemy_health -= base_attack
            curr_character_strength += 15
        else:
            curr_enemy_health = curr_enemy_health
            curr_character_strength = curr_character_strength
    elif(attack_type == 2 and which_enemy == "end" and active_character == 0):
        special_attack = 0.70 * curr_character_special
        if(curr_enemy_health != 0):
            curr_enemy_health -= special_attack
            curr_character_special -= 15
        else:
            curr_enemy_health = curr_enemy_health
            curr_character_strength = curr_character_strength
    elif(attack_type == 1 and which_enemy == "tutorial" and active_character == 1):
        base_attack = 0.05 * curr_enemy_strength
        if(curr_enemy_health != 0):
            curr_enemy_health -= base_attack
            curr_enemy_strength += 1
        else:
            curr_enemy_health = curr_enemy_health
            curr_enemy_strength = curr_enemy_strength
    elif(attack_type == 2 and which_enemy == "tutorial" and active_character == 1):
        special_attack = 0.05 * curr_enemy_special
        if(curr_enemy_health != 0):
            curr_enemy_health -= special_attack
            curr_enemy_special -= 5
        else:
            curr_enemy_health = curr_enemy_health
            curr_enemy_strength = curr_enemy_strength
    elif(attack_type == 1 and which_enemy == "easy" and active_character == 1):
        base_attack = 0.1 * curr_enemy_strength
        if(curr_enemy_health != 0):
            curr_enemy_health -= base_attack
            curr_enemy_strength += 1
        else:
            curr_enemy_health = curr_enemy_health
            curr_enemy_strength = curr_enemy_strength
    elif(attack_type == 2 and which_enemy == "easy" and active_character == 1):
        special_attack = 0.1 * curr_enemy_special
        if(curr_enemy_health != 0):
            curr_enemy_health -= special_attack
            curr_enemy_special -= 5
        else:
            curr_enemy_health = curr_enemy_health
            curr_enemy_strength = curr_enemy_strength
    elif(attack_type == 1 and which_enemy == "medium" and active_character == 1):
        base_attack = 0.15 * curr_enemy_strength
        if(curr_enemy_health != 0):
            curr_enemy_health -= base_attack
            curr_enemy_strength += 1
        else:
            curr_enemy_health = curr_enemy_health
            curr_enemy_strength = curr_enemy_strength
    elif(attack_type == 2 and which_enemy == "medium" and active_character == 1):
        special_attack = 0.15 * curr_enemy_special
        if(curr_enemy_health != 0):
            curr_enemy_health -= special_attack
            curr_enemy_special -= 5
        else:
            curr_enemy_health = curr_enemy_health
            curr_enemy_strength = curr_enemy_strength
    elif(attack_type == 1 and which_enemy == "hard" and active_character == 1):
        base_attack = 0.25 * curr_enemy_strength
        if(curr_enemy_health != 0):
            curr_enemy_health -= base_attack
            curr_enemy_strength += 1
        else:
            curr_enemy_health = curr_enemy_health
            curr_enemy_strength = curr_enemy_strength
    elif(attack_type == 2 and which_enemy == "hard" and active_character == 1):
        special_attack = 0.25 * curr_enemy_special
        if(curr_enemy_health != 0):
            curr_enemy_health -= special_attack
            curr_enemy_special -= 5
        else:
            curr_enemy_health = curr_enemy_health
            curr_enemy_strength = curr_enemy_strength
    elif(attack_type == 1 and which_enemy == "boss" and active_character == 1):
        base_attack = 0.40 * curr_enemy_strength
        if(curr_enemy_health != 0):
            curr_enemy_health -= base_attack
            curr_enemy_strength += 1
        else:
            curr_enemy_health = curr_enemy_health
            curr_enemy_strength = curr_enemy_strength
    elif(attack_type == 2 and which_enemy == "boss" and active_character == 1):
        special_attack = 0.40 * curr_enemy_special
        if(curr_enemy_health != 0):
            curr_enemy_health -= special_attack
            curr_enemy_special -= 5
        else:
            curr_enemy_health = curr_enemy_health
            curr_enemy_strength = curr_enemy_strength
    elif(attack_type == 1 and which_enemy == "end" and active_character == 1):
        base_attack = 0.50 * curr_enemy_strength
        if(curr_enemy_health != 0):
            curr_enemy_health -= base_attack
            curr_enemy_strength += 1
        else:
            curr_enemy_health = curr_enemy_health
            curr_enemy_strength = curr_enemy_strength
    elif(attack_type == 2 and which_enemy == "end" and active_character == 1):
        special_attack = 0.50 * curr_enemy_special
        if(curr_enemy_health != 0):
            curr_enemy_health -= special_attack
            curr_enemy_special -= 5
        else:
            curr_enemy_health = curr_enemy_health
            curr_enemy_strength = curr_enemy_strength

    updated_character = {
        "vitality": curr_character_health,
        "strength": curr_character_strength,
        "special": curr_character_special,
        "health_potions": curr_character_health_potions,
        "strength_potions": curr_character_strength_potions
    }

    updated_enemy = {
        "vitality": curr_enemy_health,
        "strength": curr_enemy_strength,
        "special": curr_enemy_special,
    }

    return updated_character, updated_enemy

def usePotion(potion_type, current_character):
    
    curr_health = current_character.get("vitality")
    curr_strength = current_character.get("strength")
    curr_special = current_character.get("special")
    curr_health_potions = current_character.get("health_potions")
    curr_strength_potions = current_character.get("strength_potions")

    if(potion_type == "health"):
        curr_health += 5
        curr_health_potions -= 1
    else:
        curr_strength += 5
        curr_strength_potions -= 1

    updated_character = {
        "vitality": curr_health,
        "strength": curr_strength,
        "special": curr_special,
        "health_potions": curr_health_potions,
        "strength_potions": curr_strength_potions
    }

    return updated_character

def updateCharacterStats(current_character, health, strength, special, health_potions, strength_potions):
    
    # So this does not get messy
    curr_health = current_character.get("vitality")
    curr_strength = current_character.get("strength")
    curr_special = current_character.get("special")
    curr_health_potions = current_character.get("health_potions")
    curr_strength_potions = current_character.get("strength_potions")

    if(health > 0):
        curr_health += health

    if(strength > 0):
        curr_strength += strength

    if(special > 0):
        curr_special += special
    
    if(health_potions > 0):
        curr_health_potions += health_potions

    if(strength_potions > 0):
        curr_strength_potions += strength_potions

    updated_character = {
        "vitality": curr_health,
        "strength": curr_strength,
        "special": curr_special,
        "health_potions": curr_health_potions,
        "strength_potions": curr_strength_potions
    }

    return updated_character

def storeHealthPotions(character_stats, h_stock):
    h_potions_amt = int(input("How many health potions would you like?"))
    if(h_potions_amt > 0 and h_potions_amt <= h_stock):
        updated_character = updateCharacterStats(character_stats, 0, 0, 0, h_potions_amt, 0)
    else:
        print("The number of requested potions is not available.")
        storeHealthPotions(character_stats, h_stock)
    
    return updated_character, h_potions_amt

def storeStrengthPotions(character_stats, s_stock):
    s_potions_amt = int(input("How many strength potions would you like?"))
    if(s_potions_amt > 0 and s_potions_amt <= s_stock):
        updated_character = updateCharacterStats(character_stats, 0, 0, 0, 0, s_potions_amt)
    else:
        print("The number of requested potions is not available.")
        storeStrengthPotions(character_stats, s_stock)
    
    return updated_character, s_potions_amt

def store(character_stats, h_stocks, potion_limits, s_stocks, s_timess, upgrade_limits, ss_timess):
    print("Welcome to the store!\n")
    h_stock = h_stocks
    s_stock = s_stocks
    s_times = s_timess
    ss_times = ss_timess
    potion_limit = potion_limits
    upgrade_limit = upgrade_limits

    if(s_times == 1 and ss_times == 0):
        store_option = int(input("Would you like to see what I have for sell?\nUpgrades can only be done once per store.\n(1) Health Potion (Stock: {})\n(2) Strength Potion (Stock: {}) \n(3) Upgrade Strength (+2 to strength value)\nThis option is no longer available at this store. \n(5) Exit\n".format(h_stock, s_stock)))
    elif(ss_times == 1 and s_times == 0):
        store_option = int(input("Would you like to see what I have for sell?\nUpgrades can only be done once per store.\n(1) Health Potion (Stock: {})\n(2) Strength Potion (Stock: {}) \nThis option is no longer available at this store. \n(4) Upgrade Special (+2 to special value)\n(5) Exit\n".format(h_stock, s_stock)))
    elif(s_times == 1 and ss_times == 1):
        store_option = int(input("Would you like to see what I have for sell?\nUpgrades can only be done once per store.\n(1) Health Potion (Stock: {})\n(2) Strength Potion (Stock: {}) \n(3) Upgrade Strength (+2 to strength value)\n(4) Upgrade Special (+2 to special value)\n(5) Exit\n".format(h_stock, s_stock)))

    store_options = [1,2,3,4,5]

    if(store_option in store_options):
        if(store_option == 1):
            if(potion_limit > 0):
                updated_character, h_amount = storeHealthPotions(character_stats, h_stock)
                h_stock -= h_amount
                potion_limit -= 1
            else:
                print("Sorry! You have reached the limit for potions at this store.")
                updated_character = character_stats
            store(updated_character, h_stock, potion_limit, 3, 1, 1, 1)
        elif(store_option == 2):
            if(potion_limit > 0):
                updated_character, s_amount = storeStrengthPotions(character_stats, s_stock)
                s_stock -= s_amount
                potion_limit -= 1
            else:
                print("Sorry! You have reached the limit for potions at this store.")
                updated_character = character_stats
            store(updated_character, 3, potion_limit, s_stock, 1,1,1)
            
        elif(store_option == 3):
            if(upgrade_limit > 0):
                updated_character = updateCharacterStats(character_stats, 0, 2, 0, 0, 0)
                s_times -= 1
                upgrade_limit -= 1
            else:
                print("Sorry! You have reached the limit for upgrades at this store.")
                updated_character = character_stats
                upgrade_limit = 0
                s_times = 0
            store(updated_character, 3, 2, 3, s_times, upgrade_limit, 1)
        elif(store_option == 4):
            if(upgrade_limit > 0):
                updated_character = updateCharacterStats(character_stats, 0, 0, 2, 0, 0)
                ss_times -= 1
                upgrade_limit -= 1
            else:
                print("Sorry! You have reached the limit for upgrades at this store.")
                updated_character = character_stats
            store(updated_character, 3, 2, 3, 1, upgrade_limit, ss_times)
        elif(store_option == 5):
            updated_character = character_stats
    else:
        print("You have entered an answer that can not be understood. Please enter\na numerical value, 1 through 5.")
        store(character_stats)

    return updated_character

def getEnemyStats():
    boss_level = random.randInt(0, 10)
    if(boss_level >= 8):
        enemy = bossEnemy()
    elif(boss_level >= 6 and boss_level < 7):
        enemy = generalHardEnemy()
    elif(boss_level >= 4 and boss_level < 5):
        enemy = generalMediumEnemy()
    elif(boss_level < 4 and boss_level >= 0):
        enemy = generalMediumEnemy()

    return enemy

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

def tutorialEnemy():
    tutorial_enemy = {
        "vitality": 10,
        "strength": 10,
        "special": 10,
    }
    return tutorial_enemy

def generalEasyEnemy():
    easy_enemy = {
        "vitality": 75,
        "strength": 50,
        "special": 50,
    }
    return easy_enemy

def generalMediumEnemy():
    medium_enemy = {
        "vitality": 80,
        "strength": 70,
        "special": 65,
    }
    return medium_enemy

def generalHardEnemy():
    hard_enemy = {
        "vitality": 90,
        "strength": 80,
        "special": 80,
    }
    return hard_enemy

def bossEnemy():
    boss_enemy = {
        "vitality": 95,
        "strength": 90,
        "special": 90,
    }
    return boss_enemy

def bossEndEnemy():
    end_boss = {
        "vitality": 100,
        "strength": 100,
        "special": 100,
    }
    return end_boss

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
    print("|----------|    |--------------|    |------------|")
    print("|          |    |              |    |            |")
    print("| lakeside |====| presidential |====|  riverside |")
    print("|  dorms   |    | dorms        |    |  dorms     |") 
    print("|----------|    |--------------|    |------------|")
    print("     ||                ||                 ||      ")
    print("     ||                ||                 ||      ")
    print("     ||                ||                 ||      ")
    print("|----------  |    |------------|    |------------|    |-----|")
    print("|            |    |            |    |            |    |     |")
    print("| ridgecrest |====| lakeside   |====|  ENGR      |====| REC |")
    print("|  dorms     |    | dining     |    |  Square    |    |     |") 
    print("|------------|    |------------|    |------------|    |-----|")
    print("     ||                ||                 ||      ")
    print("     ||                ||                 ||      ")
    print("     ||                ||                 ||      ")
    print("     ||           |------------|          ||      ")
    print("     ||           |            |          ||      ")
    print("     ||           |   FERG     |          ||      ")
    print("     ||           |            |          ||      ") 
    print("     ||           |------------|          ||      ")
    print("     ||                ||                 ||      ")
    print("     ||                ||                 ||      ")
    print("     ||                ||                 ||      ")
    print("|----------  |    |------------|    |------------|    |----------|")
    print("|            |    |            |    |            |    |          |")
    print("| Bruno      |====| Gorgas     |====|  QUAD      |====| ENGR     |")
    print("| Library    |    | Library    |    |            |    | Library  |") 
    print("|------------|    |------------|    |------------|    |----------|")
    print("     ||                ||                 ||      ")
    print("     ||                ||                 ||      ")
    print("     ||                ||                 ||      ")
    print("     ||           |------------|          ||      ")
    print("     ||           |            |          ||      ")
    print("     ||           | McLure     |          ||      ")
    print("     ||           | Library    |          ||      ") 
    print("     ||           |------------|          ||      ")
    print("     ||                ||                 ||      ")
    print("     ||                ||                 ||      ")
    print("     ||                ||                 ||      ")
    print("|----------|    |--------------|    |------------|")
    print("|          |    |              |    |            |")
    print("| Stadium  |====| Rose         |====|  Moody     |")
    print("| (End)    |    | Admin        |    |  Music     |") 
    print("|----------|    |--------------|    |------------|")
    print("                       ||                 ||      ")
    print("                       ||                 ||      ")
    print("                       ||                 ||      ")
    print("                |--------------|    |-------------|")
    print("                |              |    |             |")
    print("                | Baseball     |====|  Basketball |")
    print("                | Stadium      |    |  Stadium    |") 
    print("                |--------------|    |-------------|")

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

def getLevel(level, current_character):
    if(level == "riverside"):
        a = riverSideLiving()
        enemy_level = "tutorial"
        return a, enemy_level
    elif(level == "default"):
        a = lakeSideLiving()
        enemy_level = "tutorial"
        return a, enemy_level
    elif(level == "lakeside"):
        a = lakeSideLiving()
        enemy_level = "tutorial"
        return a, enemy_level
    elif(level == "ridgecrest"):
        a = ridgeCrestLiving()
        enemy_level = "tutorial"
        return a, enemy_level
    elif(level == "gorgas"):
        a = gorgasLibrary()
        return a
    elif(level == "quad"):
        a = quadLevel()
        return a
    elif(level == "ferg"):
        a = fergLevel()
        return a
    elif(level == "lakesideDining"):
        a = lakesideDining(current_character)
        return a
    elif(level == "engr"):
        a = engrLevel()
        return a
    elif(level == "rec"):
        a = recLevel()
        return a
    elif(level == "presidential"):
        a = presidentialLiving()
        enemy_level = "tutorial"
        return a, enemy_level
    elif(level == "engrLib"):
        a = engrLibrary()
        return a
    elif(level == "mcLureLib"):
        a = mcLureLibrary()
        return a
    elif(level == "brunoLib"):
        a = brunoLibrary()
        return a
    elif(level == "stadium"):
        a = stadiumLevel()
        return a
    elif(level == "admin"):
        a = adminLevel()
        return a
    elif(level == "music"):
        a = musicLevel()
        return a
    elif(level == "basketball"):
        a = basketballLevel()
        return a
    elif(level == "baseball"):
        a = baseballLevel()
        return a

def getPausedState():
    paused = input("\nWould you like to pause? (yes or no)\n")
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

def move():
    direction = input("Which cardinal direction would you like to go? Options are north, south, east or west.")
    cordinal_direction = ["north", "south", "west", "east"]
    if(direction in cordinal_direction):
        return direction
    else:
        print('The answer you gave was not accepted. Please enter one of the choices as they show in the prompt.')
        move()

def handleMove(direction, curr_location):
    if(curr_location == "lakeside"):
        if(direction == "south"):
            location = "ridgecrest"
        elif(direction == "east"):
            location = "presidential"
    elif(curr_location == "ridgecrest"):
        if(direction == "north"):
            location = "lakeside" 
        elif(direction == "south"):
            location = "brunoLib"
        elif(direction == "east"):
            location = "lakesideDining"
    elif(curr_location == "riverside"):
        if(direction == "south"):
            location = "engr"
        elif(direction == "west"):
            location = "presidential"
    elif(curr_location == "presidential"):
        if(direction == "south"):
            location = "lakesideDining"
        elif(direction == "east"):
            location = "riverside"
        elif(direction == "west"):
            location = "lakeside"
    elif(curr_location == "stadium"):
        if(direction == "north"):
            location = "brunoLib"
        elif(direction == "east"):
            location = "admin"
    elif(curr_location == "lakesideDining"):
        if(direction == "north"):
            location = "presidential"
        elif(direction == "south"):
            location = "ferg"
        elif(direction == "east"):
            location = "engr"
        elif(direction == "west"):
            location = "ridgecrest"
    elif(curr_location == "engr"):
        if(direction == "north"):
            location = "riverside"
        elif(direction == "south"):
            location = "quad"
        elif(direction == "east"):
            location = "rec"
        elif(direction == "west"):
            location = "lakesideDining"
    elif(curr_locaiton == "rec"):
        if(direction == "west"):
            location = "engr"
    elif(curr_location == "ferg"):
        if(direction == "north"):
            location = "lakesideDining"
    elif(curr_location == "brunoLib"):
        if(direction == "north"):
            location = "ridgecrest"
        elif(direction == "south"):
            location = "stadium"
        elif(direction == "east"):
            location = "gorgasLib"
    elif(curr_location == "gorgasLib"):
        if(direction == "south"):
            location = "mcLureLib"
        elif(direction == "east"):
            location = "quad"
        elif(direction == "west"):
            location = "brunoLib"
    elif(curr_location == "quad"):
        if(direction == "north"):
            location = "engr"
        elif(direction == "south"):
            location = "music"
        elif(direction == "east"):
            location = "engrLib"
        elif(direction == "west"):
            location = "gorgasLib"
    elif(curr_location == "engrLib"):
        if(direction == "west"):
            location = "quad"
    elif(curr_location == "mcLureLib"):
        if(direction == "north"):
            location = "gorgasLib"
        elif(direction == "south"):
            location = "admin"
    elif(curr_location == "admin"):
        if(direction == "north"):
            location = "mcLureLib"
        elif(direction == "south"):
            location = "baseball"
        elif(direction == "east"):
            location = "music"
        elif(direction == "west"):
            location = "stadium"
    elif(curr_location == "music"):
        if(direction == "north"):
            location = "quad"
        elif(direction == "south"):
            location = "basketball"
        elif(direction == "west"):
            location = "admin"
    elif(curr_location == "baseball"):
        if(direction == "north"):
            location = "admin"
    elif(curr_location == "basketball"):
        if(direction == "north"):
            location = "music"
    
    return location

def handleBoolMove(curr_location):
    move_direction = move()
    isMove = canMove(move_direction, curr_location)
    if(isMove == True):
        return True, move_direction
    else:
        print("You shall not pass!\n")
        handleBoolMove()

def play(character_name, character_stats, starting_location):

    starting_character = checkContinue(starting_location, character_stats)
    
    #level = getLevel(starting_location, character_stats)
    #level2 = getLevel("lakesideDining", character_stats)
    #direction = move(starting_location)
    while(starting_character.get("vitality") > 0):
        levelOneEnemy, enemy_level = getLevel(starting_location, character_stats)
        
        while(levelOneEnemy.get("vitality") > 0):
            action = int(input("Would you like to do a \n(1) basic attack\n(2) a special attack\n(3) take a health potion\n(4) take a strength potion?\n"))
            action_options = [1,2,3,4]
            if(action in action_options):
                if(action == 1 or action == 2):
                    if(action == 1):
                        starting_character, levelOneEnemy = attack(starting_character, levelOneEnemy, 1, enemy_level, 0)
                        starting_character, levelOneEnemy = attack(starting_character, levelOneEnemy, 1, enemy_level, 1)

            print("Your character:\nHealth: {}\nStrength: {}\nSpecial: {}\nHealth Potions: {}\nStrength Potions: {}\n".format(starting_character.get("vitality"), starting_character.get("strength"), starting_character.get("special"), starting_character.get("health_potions"), starting_character.get("strength_potions") ))
            print("The Enemy:\nHealth: {}\nStrength: {}\nSpecial: {}\nHealth Potions: {}\nStrength Potions: {}\n".format(levelOneEnemy.get("vitality"), levelOneEnemy.get("strength"), levelOneEnemy.get("special"), levelOneEnemy.get("health_potions"), levelOneEnemy.get("strength_potions")))
        print("Finished with that character.")
        isMove, move_direction = handleBoolMove(starting_location)
        if(isMove == True):
            nextLevel = handleMove(move_direction, starting_location)
            nextEnemy, enemy_level = getLevel(nextLevel, starting_character)
            if(nextLevel != "stadium"):

                while(nextEnemy.get("vitality") > 0):
                    action = int(input("Would you like to do a \n(1) basic attack\n(2) a special attack\n(3) take a health potion\n(4) take a strength potion?\n"))
                    action_options = [1,2,3,4]
                    if(action in action_options):
                        if(action == 1 or action == 2):
                            if(action == 1):
                                starting_character, nextEnemy = attack(starting_character, nextEnemy, 1, enemy_level, 0)
                                starting_character, nextEnemy = attack(starting_character, nextEnemy, 1, enemy_level, 1)

                    print("Your character:\nHealth: {}\nStrength: {}\nSpecial: {}\nHealth Potions: {}\nStrength Potions: {}\n".format(starting_character.get("vitality"), starting_character.get("strength"), starting_character.get("special"), starting_character.get("health_potions"), starting_character.get("strength_potions") ))
                    print("The Enemy:\nHealth: {}\nStrength: {}\nSpecial: {}\nHealth Potions: {}\nStrength Potions: {}\n".format(nextEnemy.get("vitality"), nextEnemy.get("strength"), nextEnemy.get("special"), nextEnemy.get("health_potions"), nextEnemy.get("strength_potions")))
                print("Finished level.")
            else:
                while(nextEnemy.get("vitality") > 0):
                    action = int(input("Would you like to do a \n(1) basic attack\n(2) a special attack\n(3) take a health potion\n(4) take a strength potion?\n"))
                    action_options = [1,2,3,4]
                    if(action in action_options):
                        if(action == 1 or action == 2):
                            if(action == 1):
                                starting_character, nextEnemy = attack(starting_character, nextEnemy, 1, enemy_level, 0)
                                starting_character, nextEnemy = attack(starting_character, nextEnemy, 1, enemy_level, 1)

                    print("Your character:\nHealth: {}\nStrength: {}\nSpecial: {}\nHealth Potions: {}\nStrength Potions: {}\n".format(starting_character.get("vitality"), starting_character.get("strength"), starting_character.get("special"), starting_character.get("health_potions"), starting_character.get("strength_potions") ))
                    print("The Enemy:\nHealth: {}\nStrength: {}\nSpecial: {}\nHealth Potions: {}\nStrength Potions: {}\n".format(nextEnemy.get("vitality"), nextEnemy.get("strength"), nextEnemy.get("special"), nextEnemy.get("health_potions"), nextEnemy.get("strength_potions")))
                print("Finished game.")
    isPaused = getPausedState()
    
    if(isPaused == "yes"):
        pauseOption = pauseMenu()
        if(pauseOption == 1):
            isPaused = "no"
        elif(pauseOption == 2):
            printMap()
        elif(pauseOption == 3):
            exit()

    print("testing after pause")

def getPlayerName():
    player_name = input("\nWhat will your character's name be?\n")
    return player_name

def getStartingLocation():
    starting_location = input("\nWhich dorm will you start at? Or would you like the default option?\n(example answers: ridgecrest, lakeside, riverside, presidential, default)\n")
    starting_locations = ["lakeside", "ridgecrest", "riverside", "presidential", "default"]
    if(starting_location in starting_locations):
        return starting_location
    else:
        print("should not go here")
        getStartingLocation()

# def getStartingLocation():
#     starting_location = getStartingLocation()
#     return starting_location

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
    continued = input("\nWould you like to swap this character? (yes or no)\nThis will swap your starting location as well\n")
    if(continued == "yes" or continued == "no"):
        if(continued == "yes"):
            starting_location = getStartingLocation()
            starting_character = getStartingCharacter(starting_location)
            checkContinue(starting_location, starting_character)
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