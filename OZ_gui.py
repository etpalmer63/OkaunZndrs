import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


from OZFunctions import *
import random
from copy import deepcopy
import time #for sleep timers 

from pygame import mixer #for sound


def gif_select_win():
    
    win_image = [
            "dchapelle_win.gif",
            "jeancluade_win.gif",
            "miketyson_win.gif",
            "man_win.gif",
            "rocky_win.gif",
            "oldman_win.gif",
            "ufc_win.gif"]

    sel = random.randint(0,len(win_image)-1)
    return win_image[sel]


def gif_select_lose():
    
    lose_image = [
            "gladiator_loser.gif",
            "tswift_loser.gif",
            "missedkick_loser.gif",
            "hulahoop_loser.gif",
            "skateboard_loser.gif"]

    sel = random.randint(0,len(lose_image)-1)
    return lose_image[sel]



class okaun_power_dialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, title="Okaun Power Set", transient_for=parent, flags=0)
       
        self.set_decorated(False)

        box = self.get_content_area()    

        #button1 = Gtk.Button(label="Power Up")
        #button1.connect("clicked", self.on_button1_clicked)
        #box.add(button1)

        #button2 = Gtk.Button(label="Power Down")
        #button2.connect("clicked", self.on_button2_clicked)
        #box.add(button2)

        global board

        label1 = Gtk.Label(label="Power")
        box.add(label1)

        adjustment1 = Gtk.Adjustment(upper=999, step_increment=1, page_increment=10)
        self.spin_button_1 = Gtk.SpinButton()
        self.spin_button_1.set_adjustment(adjustment1)
        self.spin_button_1.set_value(board["okaun_pt_set"][0])
        self.spin_button_1.connect("value-changed", self.on_value_changed_1)
        box.add(self.spin_button_1)

        label2 = Gtk.Label(label="Toughness")
        box.add(label2)

        adjustment2 = Gtk.Adjustment(upper=999, step_increment=1, page_increment=10)
        self.spin_button_2 = Gtk.SpinButton()
        self.spin_button_2.set_adjustment(adjustment2)
        self.spin_button_2.set_value(board["okaun_pt_set"][1])
        self.spin_button_2.connect("value-changed", self.on_value_changed_2)
        box.add(self.spin_button_2)

        button3 = Gtk.Button(label="Done")
        button3.connect("clicked", self.on_button3_clicked)
        box.add(button3)

        self.show_all()


    def on_button1_clicked(self, widget):
        global board
        board["okaun_pt_set"][0] += 1
        board.update({"okaun_pt":deepcopy(board["okaun_pt_set"])})
        print("Okaun power set to " + str(board["okaun_pt_set"][0]))
            
    def on_button2_clicked(self, widget):
        global board
        board["okaun_pt_set"][0] -= 1
        board.update({"okaun_pt":deepcopy(board["okaun_pt_set"])})
        print("Okaun power set to " + str(board["okaun_pt_set"][0]))

    def on_button3_clicked(self, widget):
        print("Done")
        Gtk.Widget.destroy(self) 

    def on_value_changed_1(self, scroll):
        global board
        board["okaun_pt_set"][0]=self.spin_button_1.get_value_as_int()
        board.update({"okaun_pt":deepcopy(board["okaun_pt_set"])})
        print(self.spin_button_1.get_value_as_int())

    def on_value_changed_2(self, scroll):
        global board
        board["okaun_pt_set"][1]=self.spin_button_2.get_value_as_int()
        board.update({"okaun_pt":deepcopy(board["okaun_pt_set"])})
        print(self.spin_button_2.get_value_as_int())


class okaun_tough_dialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, title="Okaun Toughness Set", transient_for=parent, flags=0)
       
        self.set_decorated(False)

        box = self.get_content_area()    

        button1 = Gtk.Button(label="Toughness Up")
        button1.connect("clicked", self.on_button1_clicked)
        box.add(button1)

        button2 = Gtk.Button(label="Toughness Down")
        button2.connect("clicked", self.on_button2_clicked)
        box.add(button2)

        button3 = Gtk.Button(label="Done")
        button3.connect("clicked", self.on_button3_clicked)
        box.add(button3)

        self.show_all()


    def on_button1_clicked(self, widget):
        global board
        board["okaun_pt_set"][1] += 1
        board.update({"okaun_pt":deepcopy(board["okaun_pt_set"])})
        print("Okaun toughness set to " + str(board["okaun_pt_set"][1]))
            
    def on_button2_clicked(self, widget):
        global board
        board["okaun_pt_set"][1] -= 1
        board.update({"okaun_pt":deepcopy(board["okaun_pt_set"])})
        print("Okaun toughness set to " + str(board["okaun_pt_set"][1]))

    def on_button3_clicked(self, widget):
        print("Done")
        Gtk.Widget.destroy(self) 


class single_flip_window(Gtk.Dialog):

    def __init__(self,parent):
        Gtk.Dialog.__init__(self, title="Single Flip", transient_for=parent, flags=0)

        self.set_decorated(False)

        box = self.get_content_area()    
       
        global board
       
        if board["karak"]:
            label_str = "Flipping Two Coins:\n"
        else:
            label_str = "Flipping One Coin:\n"

        label_str += "Heads or Tails?"

        #label = Gtk.Label(label="Coin Flip: Heads or Tails?")
        label = Gtk.Label(label=label_str)
        box.add(label)

        button1 = Gtk.Button(label="Heads")
        button1.connect("clicked", self.on_button1_clicked)
        box.add(button1)

        button2 = Gtk.Button(label="Tails")
        button2.connect("clicked", self.on_button2_clicked)
        box.add(button2)

        self.show_all()

    def on_button1_clicked(self, widget):
        global last_result
        if flip_coin(True,board,0):
            print("WINNER")
            last_result = True
        else:
            print("LOSER")
            last_result = False
        Gtk.Widget.destroy(self) 

    def on_button2_clicked(self, widget):
        global last_result
        if flip_coin(True,board,1):
            last_result = True
            print("WINNER")
        else:
            last_result = False
            print("LOSER")
        Gtk.Widget.destroy(self) 



class single_flip_result_window(Gtk.Dialog):
    def __init__(self,parent):
        Gtk.Dialog.__init__(self, title="Flip Result", transient_for=parent, flags=0)

        self.set_decorated(False)

        box = self.get_content_area()    
      

        img_coin_flip = Gtk.Image()


        global last_result, board

        label = Gtk.Label()

        if last_result:
            #label = Gtk.Label(label=win_flip(True,board))
            label.set_text(win_flip(True, board))
            img_coin_flip.set_from_file(gif_select_win())
        else:
            img_coin_flip.set_from_file(gif_select_lose())
            label.set_text("LOSE!")
            #label = Gtk.Label(label="LOSE!")

        label.set_justify(Gtk.Justification.CENTER)
        box.add(img_coin_flip)
        box.add(label)

        

        #self.add_events(Gtk.Gdk.BUTTON_PRESS_MASK)
        #self.connect("button-press-event", print("a click!"))

        self.show_all()

        def destroy_me():
            Gtk.Widget.destroy(self)

       
        GLib.timeout_add(2000, destroy_me)



class menu_window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Okaun Zndrsplt Device Menu")


       
        #self.set_decorated(False) #later enable this with full screen in main loop

        grid = Gtk.Grid()
        grid.set_row_homogeneous(True)
        grid.set_column_homogeneous(True)
        self.add(grid)


        label = Gtk.Label()
        label.set_text("Enter Okaun's\nBase Power and\nToughness")
        label.set_justify(Gtk.Justification.CENTER)
        #self.button1 = Gtk.Button(label="Enter Okaun's\nBase Power and\nToughness")
        self.button1 = Gtk.Button()
        self.button1.add(label)
        label.set_mnemonic_widget(self.button1)
        self.button1.connect("clicked", self.on_button1_clicked)

        label2 = Gtk.Label()
        label2.set_text("Check Board\nStatus")
        label2.set_justify(Gtk.Justification.CENTER)
        self.button2 = Gtk.Button()
        self.button2.add(label2)
        label2.set_mnemonic_widget(self.button2)
        #self.button2 = Gtk.Button(label="Check Board\nStatus")
        self.button2.connect("clicked", self.on_button2_clicked)
        
        self.button3 = Gtk.ToggleButton(label="Okaun")
        self.button3.connect("clicked", self.on_button3_clicked)
        
        self.button4 = Gtk.ToggleButton(label="Zndrsplt")
        self.button4.connect("clicked", self.on_button4_clicked)
        
        self.button5 = Gtk.ToggleButton(label="Karak's Thumb")
        self.button5.connect("clicked", self.on_button5_clicked)
        
        label6 = Gtk.Label()
        label6.set_text("Single\nFlip")
        label6.set_justify(Gtk.Justification.CENTER)
        self.button6 = Gtk.Button()
        self.button6.add(label6)
        label6.set_mnemonic_widget(self.button6)
        #self.button6 = Gtk.Button(label="Single\nFlip")
        self.button6.connect("clicked", self.on_button6_clicked)
        
        label7 = Gtk.Label()
        label7.set_text("Precombat\nFlip Sequence")
        label7.set_justify(Gtk.Justification.CENTER)
        self.button7 = Gtk.Button()
        self.button7.add(label7)
        label7.set_mnemonic_widget(self.button7)
        #self.button7 = Gtk.Button(label="Precombat\nFlip Sequence")
        self.button7.connect("clicked", self.on_button7_clicked)
        
        label8 = Gtk.Label()
        label8.set_text("New Turn\nOkaun Reset")
        label8.set_justify(Gtk.Justification.CENTER)
        self.button8 = Gtk.Button()
        self.button8.add(label8)
        label8.set_mnemonic_widget(self.button8)
        #self.button8 = Gtk.Button(label="New Turn\nOkaun Reset")
        self.button8.connect("clicked", self.on_button8_clicked)
        
        self.button9 = Gtk.Button(label="Exit")
        self.button9.connect("clicked", self.on_button9_clicked)



        grid.add(self.button1) 
        grid.attach(self.button2,1,0,1,1)
        grid.attach(self.button9,2,0,1,1)
        grid.attach(self.button4,0,1,1,1)
        grid.attach(self.button5,1,1,1,1)
        grid.attach(self.button3,2,1,1,1)
        grid.attach(self.button7,0,2,1,1)
        grid.attach(self.button8,1,2,1,1)
        grid.attach(self.button6,2,2,1,1)

    def on_button1_clicked(self, widget):
        
        dialog1 = okaun_power_dialog(self)
        dialog1.run()
        #dialog2 = okaun_tough_dialog(self)
        #dialog2.run()

    def on_button2_clicked(self, widget):

        board_stats = Gtk.MessageDialog(
                transient_for=self,
                flags=0,
                message_type=Gtk.MessageType.OTHER,
                buttons=Gtk.ButtonsType.OK,
                text=check_board_status(board))
                
        board_stats.run()
        board_stats.destroy()



    def on_button3_clicked(self, widget):
        toggle_okaun_otb(board)
        sound = mixer.Sound('needforspeed.wav')
        sound.play()
        

    def on_button4_clicked(self, widget):
        toggle_zndrs_otb(board)

    def on_button5_clicked(self, widget):
        toggle_karak_otb(board)

    def on_button6_clicked(self, widget):
        global board
        global last_result 

        flip_dialog = single_flip_window(self)
        flip_dialog.run()


        result_dialog = single_flip_result_window(self)
        result_dialog.run()
        #glib.timeout_add_seconds(3) 



    #precombat flip sequence
    def on_button7_clicked(self, widget):
        
        global last_result, board, flips_won
        last_result = True
        flips_won = 0

        #two flip sequences for okaun and zndrsplt each
        while (last_result == True) and board["okaun"]:
            print("----")
            flip_dialog = single_flip_window(self)
            flip_dialog.run()

            result_dialog = single_flip_result_window(self)
            result_dialog.run()
        
            if last_result:
                flips_won += 1

        last_result = True
        while (last_result == True) and board["zndrs"]:
            print("----")
            flip_dialog = single_flip_window(self)
            flip_dialog.run()

            result_dialog = single_flip_result_window(self)
            result_dialog.run()
        
            if last_result:
                flips_won += 1


        #create string to describe result of flip sequence
        string = ("Won " + str(flips_won) + " flips.\n")
        if board["zndrs"]: 
            string += "Draw " + str(flips_won) + " cards.\n"
        if board["okaun"]:
            string += "Okaun is [" + str(board["okaun_pt"][0]) + "/" \
                                   + str(board["okaun_pt"][1]) + "]."

        #display result dialog
        quick_test  = Gtk.MessageDialog(
                transient_for=self,
                flags=0,
                message_type=Gtk.MessageType.OTHER,
                buttons=Gtk.ButtonsType.OK,
                text=string)
                
        quick_test.run()
        quick_test.destroy()

        
        #resets
        last_result = False #reset if neither okaun or zndrsplt is on battlefield - unnecessary?
        flips_won = 0





    def on_button8_clicked(self, widget):
        new_turn_reset(board)

    #Quit button
    def on_button9_clicked(self, widget):
        print("Exit")
        Gtk.main_quit()





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

last_result = False
flips_won = 0
choice = 0 #default to heads

mixer.init() #for playing sounds

win = menu_window()
#win.fullscreen() #will cause the entire screen to fill
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
