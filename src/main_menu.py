# coding: utf-8


#------ Import package------------
from allumette_game import *

#******************************************************************************
#******************************* MAIN MENU ************************************
#******************************************************************************

def player_game (packCig, nbCig) :

    print(name, " how many cigarettes do you take ? ")
    choiceWithdrawl = int(input())

    # Verification que le joeur retire entre 1 a 3 allumette sinon il pass sont tour
    if choiceWithdrawl < 1 or choiceWithdrawl > 3 :
        choiceWithdrawl = 0
    else :
        pass

    nbAllumettesRestante = nbCig - choiceWithdrawl
    if nbAllumettesRestante > 0 :
        return withdrawl(packCig, choiceWithdrawl)
    else :
        return [[], [], []]


def computer_game(packCig, nbCig, computerLevel) :

    choiceWithdrawl = game_level(computerLevel, nbCig)
    print("Computer, how many cigarettes do you take? ", choiceWithdrawl)

    # Verification que le joeur retire entre 1 a 3 allumette sinon il pass sont tour
    if choiceWithdrawl < 1 or choiceWithdrawl > 3 :
        choiceWithdrawl = 0
    else :
        pass

    nbAllumettesRestante = nbCig - choiceWithdrawl
    if nbAllumettesRestante > 0 :
        return withdrawl(packCig, choiceWithdrawl)
    else :
        return [[], [], []]


#------------------------------Main principal ------------------------------------
if __name__ == "__main__" :

    # Give the player's name
    name = input("Give me your name : ")

    # Give the computer's level
    computerLevel = input(" Wich level do you want to play - n/Naif - d/Distrait - r/rapid - e/expert").lower()

    # dictionary containing level given in abbreviated form
    abbreviatedLevel = {
        "n" : "Naif",
        "d" : "Distrait",
        "r" : "Rapide",
        "e" : "Expert"
        }
    print("My level is : ", abbreviatedLevel[computerLevel])

    # Who start y-->player start or n--> computer start
    startGame = str(input(" Do you start (y / n) ? ")).lower()

    # condition when it's the player who starts
    if startGame == "y" :
        # We initialize our cigarette pack
        packCigarette = init_packet_of_cigarettes()
        # Count number of cigarettes into the pack
        numberCigarettePack = number_of_cigarette(packCigarette)
        # Display content of the pack
        #displays_content_pack(packCigarette)
        whoPlay = ""
        while numberCigarettePack >= 1 :
            # ------------ Player game turn ----------
            whoPlay = name
            displays_content_pack(packCigarette)
            packCigarette = player_game (packCigarette, numberCigarettePack)
            #displays_content_pack(packCigarette)
            numberCigarettePack = number_of_cigarette(packCigarette)
            print("numberCigarettePack ===>", numberCigarettePack)

            if numberCigarettePack > 0 :

                #------------- Computer game turn ----------
                whoPlay = "Computer"
                displays_content_pack(packCigarette)
                packCigarette = computer_game (packCigarette, numberCigarettePack, computerLevel)
                #displays_content_pack(packCigarette)
                numberCigarettePack = number_of_cigarette(packCigarette)
                print("numberCigarettePack ===>", numberCigarettePack)

            else :
                numberCigarettePack = 0
        print(whoPlay, "Have Lost")

    elif startGame == "n" :
        # We initialize our cigarette pack
        packCigarette = init_packet_of_cigarettes()
        # Count number of cigarettes into the pack
        numberCigarettePack = number_of_cigarette(packCigarette)
        # Display content of the pack
        displays_content_pack(packCigarette)
        whoPlay = ""
        while numberCigarettePack >= 1 :
            #------------- Computer game turn ----------
            whoPlay = "Computer"
            displays_content_pack(packCigarette)
            packCigarette = computer_game (packCigarette, numberCigarettePack, computerLevel)
            #displays_content_pack(packCigarette)
            numberCigarettePack = number_of_cigarette(packCigarette)
            print("numberCigarettePack ===>", numberCigarettePack)

            if numberCigarettePack > 0 :
                # ------------ Player game turn ----------
                whoPlay = name
                displays_content_pack(packCigarette)
                packCigarette = player_game (packCigarette, numberCigarettePack)
                #displays_content_pack(packCigarette)
                numberCigarettePack = number_of_cigarette(packCigarette)
                print("numberCigarettePack ===>", numberCigarettePack)
            else :
                numberCigarettePack = 0
        print(whoPlay, "Have Lost")
