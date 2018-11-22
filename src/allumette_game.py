#---------- Import Package ------------------------------------
from random import randint
#--------------------------------------------------------------
def init_packet_of_cigarettes () :
    """
    initialization of our pack of 13 cigarettes

    :param None
    :returns: [] : 3 lists into list  [[],  [],  []]
    """
    return ([
        ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
        ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
        ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"]
        ])


def displays_content_pack (packCig) :
    """
    Function allowing to print all the cigarettes of the packet

    :param packCig [] : packet of cigarettes
    :returns None
    """
    try :
        if len(packCig[0]) > 0 :
            for element in packCig :
                count = 0
                for j in range(len(element)) :
                    count += 1
                    print(element[j], end='  ')
                    if count == 5 or count == 10 :
                        print("", end='     ')
                    else :
                        pass
                print("\n")
        else :
            pass
    except TypeError as e :
        print("Certainly there is a problem on the type of the value : ", e)
    except ValueError as e :
        print("Certainly there is a problem on the value : ", e)




def withdrawl (packCig, withdrawal_matches = 0) :
    """
    Function that allow to withdrawl cigarette into the packet

    :param packCig [] : packet of cigarettes
    :returns packCig [] : packet of cigarettes - removed cigarettes
    """
    for i in range(withdrawal_matches):
        packCig[0].pop()
        packCig[1].pop()
        packCig[2].pop()
    return packCig

def number_of_cigarette(packCig) :
    """
    Function that allow to count the number of cigarette into the packet

    :param packCig [] : packet of cigarettes
    :returns nb_cig : int : number of cigarette
    """
    nb_cig = (len(packCig[0]), len(packCig[1]), len(packCig[2]))
    if nb_cig[0] == nb_cig[1] and nb_cig[0] == nb_cig[2] :
        return nb_cig[0]
    else :
        raise ValueError(" Erreur de len() au niveau des listes dans les listes")


def game_level(levelGame, nbCig) :
    if levelGame == "n" :
        return naif_level (nbCig)

    elif levelGame == "d" :
        return distrait_level (nbCig)

    elif levelGame == "r" :
        return rapide_level (nbCig)

    elif levelGame == "e" :
        return expert_level (nbCig)

def naif_level (nbCig) :
    """
    Function that allow the computer to play with a naive mode

    :param nbCig : int : cigarettes number
    :returns numberMatchesTaken : int : number of cigarettes removed
    """
    try :
        if nbCig >= 3 :
            return randint(1,3)
        elif nbCig == 2 :
            return randint(1, 2)
        elif nbCig == 1 :
            return 1
        else :
            return 0
    except TypeError as e :
        print("Certainly there is a problem on the type of the value : ", e)
    except ValueError as e :
        print("Certainly there is a problem on the value : ", e)


def distrait_level (nbCig) :
    """
    Function that allow the computer to play with a distract mode

    :param nbCig : int : cigarettes number
    :returns numberMatchesTaken : int : number of cigarettes removed
    """
    try :
        return randint(1,3)
    except TypeError as e :
        print("Certainly there is a problem on the type of the value : ", e)
    except ValueError as e :
        print("Certainly there is a problem on the value : ", e)
    return numberMatchesTaken


def rapide_level (nbCig) :
    """
    Function that allow the computer to play with a rapid mode
    This mode choose randomly the number of matches between 1 and 3, regardless
    of which ones are in the pile

    :param nbCig : int : cigarettes number
    :returns numberMatchesTaken : int : number of cigarettes removed
    """
    try :
        if nbCig >= 3 :
            return 3
        elif nbCig == 2 :
            return 2
        elif nbCig == 1 :
            return 1
    except TypeError as e :
        print("Certainly there is a problem on the type of the value : ", e)
    except ValueError as e :
        print("Certainly there is a problem on the value : ", e)
    return numberMatchesTaken

def expert_level (nbCig) :
    """
    Function that allow the computer to play with a exeper mode
    Tcomputer adopts for a better strategy than choosing a random number of cigarette
        - if the user leaves 1, 2 or 3 cigarettes ==> the computer wins by choosing
            the right number of cigaretttes
        - if the user leaves 4 cigarettes, the computer leave 3
        - if the user leaves 5, 6 or 7 matches, the computer can win if they take
            a number such that 4 cigarettes remain

    :param nbCig : int : cigarettes number
    :returns numberMatchesTaken : int : number of cigarettes removed
    """
    try :
        if nbCig == 2 :
            return 1
        elif nbCig == 3 :
            return 2
        elif nbCig == 4 :
            return 3
        elif (nbCig - 1) % 4 == 0 :
            return 1
        elif (nbCig - 2) % 4 == 0 :
            return 2
        elif (nbCig - 3) % 4 == 0 :
            return 3
        else :
            return 2
    except TypeError as e :
        print("Certainly there is a problem on the type of the value : ", e)
    except ValueError as e :
        print("Certainly there is a problem on the value : ", e)
    return numberMatchesTaken
