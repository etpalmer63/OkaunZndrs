"""
This will be the collection of functions called by the GUI
"""

import random
from copy import deepcopy

# random.randint(0,9) - generates random int between 0,9 - time seeded



def win_flip(single_flip,board):
    string = ""
    str1 = ""
    str2 = ""

    if (single_flip == True):
        if board["zndrs"]:      #Zndrsplt on battlefield
            print("Draw a card")
            str1 = "Draw a card\n"
            print("*FLASHING LIGHTS*") 

        if board["okaun"]:
            board["okaun_pt"][0] = board["okaun_pt"][0] * 2
            board["okaun_pt"][1] = board["okaun_pt"][1] * 2
            print( "Okaun's new power and toughness are " + \
                    str(board["okaun_pt"][0]) + "/" + \
                    str(board["okaun_pt"][1]) + ".");
            str2 =  "Okaun's new power and toughness are " + \
                    str(board["okaun_pt"][0]) + "/" + \
                    str(board["okaun_pt"][1]) + ".";
    string = str1 + str2
    return string




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
            print("LOSE")
            return False
    else: 
        print("Flipping one coin");
        if (random.randint(0,1) == int(hot)):
            print("WIN")
            win_flip(single_flip,board)
            return True
        else:
            print("LOSE")
            return False
        

def flip_coin(single_flip, board, choice):

    if board["karak"]:   #karak's thumb on battlefield
        print("Flipping two coins")
        if (random.randint(0,1) == choice or \
           (random.randint(0,1) == choice)):
            print("WIN")
            #win_flip(single_flip,board)
            return True
        else:
            print("LOSE")
            return False
    else: 
        print("Flipping one coin");
        if (random.randint(0,1) == choice):
            print("WIN")
            #win_flip(single_flip,board)
            return True
        else:
            print("LOSE")
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

    str1 = ""

    if board["okaun"]:
        #print("Okaun is on the battlefield.")
        #str1 += "Okaun is on the battlefield.\n"
        print("Okaun [" + str(board["okaun_pt"][0]) + "/" \
                           + str(board["okaun_pt"][1]) + "]" \
                           + " is on the battlefield.")
        str1 += "Okaun [" + str(board["okaun_pt"][0]) + "/" \
                           + str(board["okaun_pt"][1]) + "]" \
                           + " is on the battlefield."
    else:
        print("Okaun is not on the battlefield.")
        str1 += "Okaun is not on the battlefield."

    str2 = ""        
    if board["zndrs"]:
        print("Zndrsplt is on the battlefield.")
        str2 = "Zndrsplt is on the battlefield."
    else:
        print("Zndrsplt is not on the battlefield.")
        str2 = "Zndrsplt is not on the battlefield."
        
    str3 = ""
    if board["karak"]:
        print("Karak's Thumb is on the battlefield.")
        str3 = "Karak's Thumb is on the battlefield."
    else: 
        print("Karak's Thumb not is on the battlefield.")
        str3 = "Karak's Thumb not is on the battlefield."

    board_txt_msg = str1 + "\n" + str2 + "\n" + str3

    return board_txt_msg

def update_okaun_pt(board):
    print("Enter Okaun's power")
    board["okaun_pt_set"][0] = int(input())
    print("Enter Okaun's toughness")
    board["okaun_pt_set"][1] = int(input())

    # this copies the base p/t to the current p/t
    # using other methods caused updates to current p/t to change base p/t
    board.update({"okaun_pt":deepcopy(board["okaun_pt_set"])})



def toggle_okaun_otb(board):
    if (board["okaun"]==False):
        board["okaun"] = True  #Okaun on the battlefield
        print("Okaun entered the battlefield.")
        print("*FLASHING RED LIGHTS*")
    else:
        board["okaun"] = False  #Okaun not on the battlefield
        print("Okaun exited the battlefield.")




def toggle_zndrs_otb(board):
    if (board["zndrs"]==False):
        board["zndrs"] = True  #Zndrsplt on the battlefield
        print("Zndrslpt entered the battlefield.")
        print("*FLASHING BLUE LIGHTS*")
        flash_blue_lights()
    else:
        board["zndrs"] = False  #Zndrsplt not on the battlefield
        print("Zndrslpt exited the battlefield.")


def toggle_karak_otb(board):
    if (board["karak"]==False):
        board["karak"] = True  #karak's thumb on the battlefield
        print("Karak's Thumb entered the battlefield.")
    else:
        board["karak"] = False  #Karak's Thumb not on the battlefield
        print("Karak's Thumb exited the battlefield.")


def new_turn_reset(board):
    # New turn -- reset okaun power and toughness
    print("New turn, reseting Okaun's power and toughness.")

    # this copies the base p/t to the current p/t
    # using other methods caused updates to current p/t to change base p/t
    board.update({"okaun_pt":deepcopy(board["okaun_pt_set"])})




def menu_select(board):
    menu_sel = int(input())

    if(menu_sel==1):
        update_okaun_pt(board)
        return 1 
    elif(menu_sel==2):
        check_board_status(board)
        return 2
    elif(menu_sel==3):
        toggle_okaun_otb(board)
        return 3
    elif(menu_sel==4):
        toggle_zndrs_otb(board)
        return 4
    elif(menu_sel==5):
        toggle_karak_otb(board)
        return 5
    elif(menu_sel==6):
        flip_coin(True,board)
        return 6
    elif(menu_sel==7):
        precombat_flips(board) 
        return 7
    elif(menu_sel==8):
        new_turn_reset(board)
        return 8
    elif(menu_sel<=0):
        exit()
    else:
        return 0



def flash_blue_lights():
    #enter code to make blue lights flash
    print("The blue lights flashed")


def flash_red_lights():
    #enter code to make red lights flash
    print("The red lights flashed")

