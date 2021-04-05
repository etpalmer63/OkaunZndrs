import gi


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk



class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)
        

        self.button1 = Gtk.Button(label="Enter Okaun P/T")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)
        #self.add(self.button)

        self.button2 = Gtk.Button(label="Button2")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)
        
        self.button3 = Gtk.Button(label="Exit")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.box.pack_start(self.button3, True, True, 0)
        
        self.button4 = Gtk.Button(label="Exit")
        self.button4.connect("clicked", self.on_button4_clicked)
        self.box.pack_start(self.button4, True, True, 0)

    def on_button1_clicked(self, widget):
        print("Button 1 Clicked")
        var1 = MyWindow()
        var1.show()

    def on_button2_clicked(self, widget):
        print("Button 2 Clicked")

    #Quit button
    def on_button3_clicked(self, widget):
        print("Button 3 Clicked")
        Gtk.main_quit()

    def on_button4_clicked(self, widget):
        print("Button 4 Clicked")

win = MyWindow()
#win.fullscreen() #will cause the entire screen to fill
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
