print("Hello world!")


import random


# random.randint(0,9) - generates random int between 0,9 - time seeded



# is Okaun on the board, what is the current base power and toughness
def get_okaun_status(okaun):
    #print("okaun status and power toughness")
    return okaun 


# is Zndrsplt on the board? 
def get_zndrs_status(zndrs):
    #print("Zndrsplt is on/off the battlefield.")
    return zndrs

def get_karak_status(karak):
    #print("Krark's thumb on the battlefield.")
    return karak

def win_flip(single_flip,okaun_pt):
    if (single_flip == True):
        if get_zndrs_status:
            print("Draw a card")

        if get_okaun_status:
            okaun_pt[0] = okaun_pt[0] * 2
            okaun_pt[1] = okaun_pt[1] * 2
            print( "Okaun's new power and toughness are " + str(okaun_pt[0]) + "/" + str(okaun_pt[1]) + ".");

def flip_coin(single_flip, okaun_pt):
  
    print("Choose heads(0) or tails(1)")
    hot = input(); 

    if (get_karak_status() == True):
        print("flipping two coins")
        if (random.randint(0,1) == int(hot) or (random.randint(0,1) == int(hot))):
            print("win")
            win_flip(single_flip,okaun_pt)
            return True
        else:
            print("loose")
            return False
    else: 
        print("flipping one coin");
        if (random.randint(0,1) == int(hot)):
            print("win")
            win_flip(single_flip,okaun_pt)
            return True
        else:
            print("loose")
            return False
        




"""
    choose a side, flip a coin. Continue until you loose. 
    for each won flip, Okaun's power and toughness * 2^(won flips)
    for each won flip, draw a card
"""
def flip_sequence(flips_won, okaun_pt):
    
    single_flip = False

    while flip_coin(single_flip, okaun_pt):
        print("You won a flip!")
        flips_won += 1
    return flips_won


def precombat_flips(okaun_pt):
    flips_won = 0

    if (get_zndrs_status() == True):
        flips_won = flip_sequence(flips_won, okaun_pt)
    if (get_okaun_status() == True):
        flips_won = flip_sequence(flips_won, okaun_pt)

    print( str(flips_won) + " flips won!")

    if (get_zndrs_status() == True):
        print( "Draw " + str(flips_won) + " cards")

    if (get_okaun_status() == True):
        okaun_pt[0] = okaun_pt[0] * 2**flips_won
        okaun_pt[1] = okaun_pt[1] * 2**flips_won
        print( "Okaun's new power and toughness are " + str(okaun_pt[0]) + "/" + str(okaun_pt[1]) + ".");

def show_menu():
    print("* ==== MENU ==== ")
    print("* 1. Enter Okaun's Power/Toughness ")
    print("* 2. Check Board Status")
    print("* 3. Okaun ETB")
    print("* 4. Zndrsplt ETB")
    print("* 5. Karak's Thumb ETB")
    print("* 6. Single Coin Flip")
    print("* 7. Precombat Flip Sequence")
    print("* 0. Exit")
    print("* ============== ")

    
def check_board_status(board):

    print(" === CHECKING BOARD STATUS === ")
    if get_okaun_status(board[1]):
        print("Okaun is on the battlefield.")
        print("Okaun is [" + str(board[0][0]) + "/" + str(board[0][1]) + "]")
    else:
        print("Okaun is not on the battlefield.")
            
    if get_zndrs_status(board[2]):
        print("Zndrsplt is on the battlefield.")
    else:
        print("Zndrsplt is not on the battlefield.")

    if get_karak_status(board[3]):
        print("Karak's Thumb is on the battlefield.")
    else: 
        print("Karak's Thumb not is on the battlefield.")



# This doesn't work in Python! 
def menu_select(board):
    menu_sel = input()

    switch (menu_sel) {
        case 1:
            print("Enter Okaun's power")
            board[0][0] = int(input())
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return 4
        case 5:
            return 5
        case 6:
            return 6
        case 7:
            return 7
    }




#input base power and toughness
okaun_pt = [3,3]

# initial state
okaun = False
zndrs = False
karak = False

board = [okaun_pt, okaun, zndrs, karak]

#flip_coin()
#flip_sequence(0)

#show_menu()

check_board_status(board)


#flip_coin(True, okaun_pt)
#print("====")
#precombat_flips(okaun_pt)



