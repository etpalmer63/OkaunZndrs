import gi


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


from OZFunctions import *
import random
from copy import deepcopy


class okaun_pt_window (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Okaun PT")

        


        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Power Up")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)
        #self.add(self.button1)

        self.button2 = Gtk.Button(label="Power Down")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)
        #self.add(self.button2)

        self.button3 = Gtk.Button(label="Back")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.box.pack_start(self.button3, True, True, 0)

    def on_button1_clicked(self, widget):
        board["okaun_pt_set"][0] += 1
        print("Okaun power set to " + str(board["okaun_pt_set"][0]))
            
    def on_button2_clicked(self, widget):
        board["okaun_pt_set"][0] -= 1
        print("Okaun power set to " + str(board["okaun_pt_set"][0]))

    def on_button3_clicked(self, widget):
        print("Done")
        Gtk.Widget.destroy(self) 


class okaun_power_dialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, title="Okaun Power Set", transient_for=parent, flags=0)
       
        self.set_decorated(False)

        box = self.get_content_area()    

        button1 = Gtk.Button(label="Power Up")
        button1.connect("clicked", self.on_button1_clicked)
        box.add(button1)

        button2 = Gtk.Button(label="Power Down")
        button2.connect("clicked", self.on_button2_clicked)
        box.add(button2)

        button3 = Gtk.Button(label="Done")
        button3.connect("clicked", self.on_button3_clicked)
        box.add(button3)

        self.show_all()


    def on_button1_clicked(self, widget):
        board["okaun_pt_set"][0] += 1
        board.update({"okaun_pt":deepcopy(board["okaun_pt_set"])})
        print("Okaun power set to " + str(board["okaun_pt_set"][0]))
            
    def on_button2_clicked(self, widget):
        board["okaun_pt_set"][0] -= 1
        board.update({"okaun_pt":deepcopy(board["okaun_pt_set"])})
        print("Okaun power set to " + str(board["okaun_pt_set"][0]))

    def on_button3_clicked(self, widget):
        print("Done")
        Gtk.Widget.destroy(self) 



class okaun_tough_dialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, title="Okaun Toughness Set", transient_for=parent, flags=0)
       
        self.set_decorated(False)

        box = self.get_content_area()    

        button1 = Gtk.Button(label="Toughness Up")
        button1.connect("clicked", self.on_button1_clicked)
        box.add(button1)

        button2 = Gtk.Button(label="Power Down")
        button2.connect("clicked", self.on_button2_clicked)
        box.add(button2)

        button3 = Gtk.Button(label="Done")
        button3.connect("clicked", self.on_button3_clicked)
        box.add(button3)

        self.show_all()


    def on_button1_clicked(self, widget):
        board["okaun_pt_set"][1] += 1
        board.update({"okaun_pt":deepcopy(board["okaun_pt_set"])})
        print("Okaun toughness set to " + str(board["okaun_pt_set"][1]))
            
    def on_button2_clicked(self, widget):
        board["okaun_pt_set"][1] -= 1
        board.update({"okaun_pt":deepcopy(board["okaun_pt_set"])})
        print("Okaun toughness set to " + str(board["okaun_pt_set"][1]))

    def on_button3_clicked(self, widget):
        print("Done")
        Gtk.Widget.destroy(self) 




class menu_window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Okaun Zndrsplt Device Menu")

        #self.box = Gtk.Box(spacing=6)
        #self.add(self.box)
        
        grid = Gtk.Grid()
        self.add(grid)


        """
        button1 = Gtk.Button(label="Button 1")
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Button 4")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="Button 6")
        button7 = Gtk.Button(label="Button 7")
        button8 = Gtk.Button(label="Button 8")
        button9 = Gtk.Button(label="Button 9")
        """
        


        self.button1 = Gtk.Button(label="Enter Okaun's\nBase Power and\nToughness", halign=Gtk.Align.CENTER)
        self.button1.connect("clicked", self.on_button1_clicked)
        #self.box.pack_start(self.button1, True, True, 0)
        #self.add(self.button)

        self.button2 = Gtk.Button(label="Check Board\nStatus")
        self.button2.connect("clicked", self.on_button2_clicked)
        #self.box.pack_start(self.button2, True, True, 0)
        
        self.button3 = Gtk.ToggleButton(label="Toggle Okaun\nOTB")
        self.button3.connect("clicked", self.on_button3_clicked)
        #self.box.pack_start(self.button3, True, True, 0)
        
        self.button4 = Gtk.ToggleButton(label="Toggle Zndrsplt\nOTB")
        self.button4.connect("clicked", self.on_button4_clicked)
        #self.box.pack_start(self.button4, True, True, 0)
        
        self.button5 = Gtk.ToggleButton(label="Toggle Karak's\nThumb OTB")
        self.button5.connect("clicked", self.on_button5_clicked)
        #self.box.pack_start(self.button5, True, True, 0)
        
        self.button6 = Gtk.Button(label="Single\nFlip")
        self.button6.connect("clicked", self.on_button6_clicked)
        #self.box.pack_start(self.button6, True, True, 0)
        
        self.button7 = Gtk.Button(label="Precombat\nFlip Sequence")
        self.button7.connect("clicked", self.on_button7_clicked)
        #self.box.pack_start(self.button7, True, True, 0)
        
        self.button8 = Gtk.Button(label="New Turn\nOkaun Reset")
        self.button8.connect("clicked", self.on_button8_clicked)
        #self.box.pack_start(self.button8, True, True, 0)
        
        self.button9 = Gtk.Button(label="Exit")
        self.button9.connect("clicked", self.on_button9_clicked)
        #self.box.pack_start(self.button9, True, True, 0)

        grid.add(self.button1) 
        grid.attach(self.button2,1,0,1,1)
        grid.attach(self.button3,2,0,1,1)
        grid.attach(self.button4,0,1,1,1)
        grid.attach(self.button5,1,1,1,1)
        grid.attach(self.button6,2,1,1,1)
        grid.attach(self.button7,0,2,1,1)
        grid.attach(self.button8,1,2,1,1)
        grid.attach(self.button9,2,2,1,1)

    def on_button1_clicked(self, widget):
        print("Button 1 Clicked")
        
        dialog1 = okaun_power_dialog(self)
        dialog1.run()
        dialog2 = okaun_tough_dialog(self)
        dialog2.run()

        #okaun_win = okaun_pt_window()
        #okaun_win.show()
        #win2.show_all()
        #update_okaun_pt(board)
        #var1 = menu_window()
        #var1.show()

    def on_button2_clicked(self, widget):
        check_board_status(board)
        print("Button 2 Clicked")

    def on_button3_clicked(self, widget):
        toggle_okaun_otb(board)
        print("Button 3 Clicked")

    def on_button4_clicked(self, widget):
        toggle_zndrs_otb(board)
        print("Button 4 Clicked")

    def on_button5_clicked(self, widget):
        toggle_karak_otb(board)
        print("Button 5 Clicked")

    def on_button6_clicked(self, widget):
        flip_coin(True,board) #single flip
        print("Button 6 Clicked")

    def on_button7_clicked(self, widget):
        precombat_flips(board)
        print("Button 7 Clicked")

    def on_button8_clicked(self, widget):
        new_turn_reset(board)
        print("Button 8 Clicked")

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




win = menu_window()
#win2 = okaun_pt_window()
#win2.show_all()
#win.fullscreen() #will cause the entire screen to fill
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
