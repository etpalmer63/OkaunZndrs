import gi


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk



class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Button1")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)
        #self.add(self.button)

        self.button2 = Gtk.Button(label="Button2")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)
        

    def on_button1_clicked(self, widget):
        print("Button 1 Clicked")

    def on_button2_clicked(self, widget):
        print("Button 2 Clicked")



win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
