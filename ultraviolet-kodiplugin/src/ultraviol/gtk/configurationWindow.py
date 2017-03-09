__author__ = 'developer'
#!/usr/bin/python3
__author__ = 'developer'
from gi.repository import Gtk
import os



class ultravioletMainWindow(Gtk.Window):

    BIOSFOLDER="ultraviol/bios/"

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        # fuseCommand = "fuse-sdl"
        # inputPath="/dev/input/js0"
        # model="48"
        # bios="48.zip"
        # download=True



        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.vbox)

        self.label= Gtk.Label()
        self.label.set_text("Fuse command:")
        self.label.set_justify(Gtk.Justification.LEFT)
        self.vbox.pack_start(self.label, True, True, 0)


        self.entry = Gtk.Entry()
        self.entry.set_text("fuse-sdl")
        self.vbox.pack_start(self.entry, True, True, 0)


        # model:
        models =os.listdir("../../"+self.BIOSFOLDER)
        # i=0
        # for model in models:
        #     print("(%d) model %s..." % (i, model))
        #     i +=1

        self.scrolled_window = Gtk.GtkScrolledWindow()
        self.scrolled_window.set_usize(250, 150)
        self.vbox.add(self.scrolled_window)
        self.scrolled_window.show()


        gtklist = Gtk.GtkList()
        self.scrolled_window.add_with_viewport(gtklist)
        gtklist.show()
        gtklist.connect("selection_changed", self.sigh_print_selection)



        self.button = Gtk.Button(label="Save")
        self.button.connect("clicked", self.on_save)

        self.vbox.pack_start(self.button, True, True, 0)
        # self.add(self.vbox)


    def on_save(self):
        print("save")






win = ultravioletMainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()


