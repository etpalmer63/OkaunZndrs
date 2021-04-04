

import random
from copy import deepcopy

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

def win_flip(single_flip,board):
    if (single_flip == True):
        if board["zndrs"]:      #Zndrsplt on battlefield
            print("Draw a card")

        if board["okaun"]:
            board["okaun_pt"][0] = board["okaun_pt"][0] * 2
            board["okaun_pt"][1] = board["okaun_pt"][1] * 2
            print( "Okaun's new power and toughness are " + \
                    str(board["okaun_pt"][0]) + "/" + \
                    str(board["okaun_pt"][1]) + ".");

def flip_coin(single_flip, board):
  
    print("Choose heads(0) or tails(1)")
    hot = input(); 

    if board["karak"]:   #karak's thumb on battlefield
        print("Flipping two coins")
        if (random.randint(0,1) == int(hot) or \
           (random.randint(0,1) == int(hot))):
            print("WIN")
            win_flip(single_flip,board)
            return True
        else:
            print("LOOSE")
            return False
    else: 
        print("Flipping one coin");
        if (random.randint(0,1) == int(hot)):
            print("WIN")
            win_flip(single_flip,board)
            return True
        else:
            print("LOOSE")
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


def precombat_flips(board):
    flips_won = 0

    if board["zndrs"]:
        flips_won = flip_sequence(flips_won, board)
    if board["okaun"]:
        flips_won = flip_sequence(flips_won, board)

    print( str(flips_won) + " flips won!")

    if board["zndrs"]:
        print( "Draw " + str(flips_won) + " cards")

    if board["okaun"]:
        board["okaun_pt"][0] = board["okaun_pt"][0] * 2**flips_won
        board["okaun_pt"][1] = board["okaun_pt"][1] * 2**flips_won
        print( "Okaun's new power and toughness are " \
                + str(board["okaun_pt"][0]) + "/" \
                + str(board["okaun_pt"][1]) + ".");

def show_menu():
    print("* ==== MENU ==== ")
    print("* 1. Enter Okaun's Base Power/Toughness ")
    print("* 2. Check Board Status")
    print("* 3. Okaun Enter or Exit the Battlefield")
    print("* 4. Zndrsplt Enter or Exit the Battlefield")
    print("* 5. Karak's Thumb Enter or Exit the Battlefield")
    print("* 6. Single Coin Flip")
    print("* 7. Precombat Flip Sequence")
    print("* 8. New Turn")
    print("* 0. Exit")
    print("* ============== ")

    
def check_board_status(board):

    print(" === CHECKING BOARD STATUS === ")
    if board["okaun"]:
        print("Okaun is on the battlefield.")
        print("Okaun is [" + str(board["okaun_pt"][0]) + "/" \
                           + str(board["okaun_pt"][1]) + "]")
    else:
        print("Okaun is not on the battlefield.")
            
    if board["zndrs"]:
        print("Zndrsplt is on the battlefield.")
    else:
        print("Zndrsplt is not on the battlefield.")

    if board["karak"]:
        print("Karak's Thumb is on the battlefield.")
    else: 
        print("Karak's Thumb not is on the battlefield.")



def menu_select(board):
    menu_sel = int(input())

    if(menu_sel==1):
        print("Enter Okaun's power")
        board["okaun_pt_set"][0] = int(input())
        print("Enter Okaun's toughness")
        board["okaun_pt_set"][1] = int(input())

        # this copies the base p/t to the current p/t
        # using other methods caused updates to current p/t to change base p/t
        board.update({"okaun_pt":deepcopy(board["okaun_pt_set"])})

        return 1 
    elif(menu_sel==2):
        check_board_status(board)
        return 2
    elif(menu_sel==3):
        if (board["okaun"]==False):
            board["okaun"] = True  #Okaun on the battlefield
            print("Okaun entered the battlefield.")
        else:
            board["okaun"] = False  #Okaun not on the battlefield
            print("Okaun exited the battlefield.")
        return 3
    elif(menu_sel==4):
        if (board["zndrs"]==False):
            board["zndrs"] = True  #Zndrsplt on the battlefield
            print("Zndrslpt entered the battlefield.")
        else:
            board["zndrs"] = False  #Zndrsplt not on the battlefield
            print("Zndrslpt exited the battlefield.")
        return 4
    elif(menu_sel==5):
        if (board["karak"]==False):
            board["karak"] = True  #karak's thumb on the battlefield
            print("Karak's Thumb entered the battlefield.")
        else:
            board["karak"] = False  #Karak's Thumb not on the battlefield
            print("Karak's Thumb exited the battlefield.")
        return 5
    elif(menu_sel==6):
        flip_coin(True,board)
        return 6
    elif(menu_sel==7):
        precombat_flips(board) 
        return 7
    elif(menu_sel==8):
        # New turn -- reset okaun power and toughness
        print("New turn, reseting Okaun's power and toughness.")

        # this copies the base p/t to the current p/t
        # using other methods caused updates to current p/t to change base p/t
        board.update({"okaun_pt":deepcopy(board["okaun_pt_set"])})
        return 8
    elif(menu_sel<=0):
        exit()
    else:
        return 0




"""
This board dictionary contains inforamtion about the board state
"""

board = {
    "okaun_pt" : [3,3],     # Okaun's current power and toughness
    "okaun_pt_set": [3,3],  # Okaun's reset to power and toughness  
    "okaun" : False,        # Okaun not on the battlefield to start
    "zndrs" : False,        # Zndrsplt not on the battlefield to start  
    "karak" : False         # Karak's Thumb not on the battlefield to start
}



#loop the runs the menu
while True:
    show_menu()
    # print(board) # uncomment this to show the saved board state each time
    menu_select(board)
    




