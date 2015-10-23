#!/usr/bin/python3
__author__ = 'developer'
# import ultraviol.configuration
# import ultraviol.gtk.selectGameWindow
from gi.repository import Gtk

# import ultraviol.configuration as conf


class ultravioletMainWindow(Gtk.Window):

    title="Ultraviolet"
    conf = None

    def __init__(self):

        # self.conf = ultraviol.configuration.loadConfiguration()
        Gtk.Window.__init__(self, title=self.title)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.vbox)

        self.label= Gtk.Label()
        self.label.set_text("What game do you want to play?")
        self.label.set_justify(Gtk.Justification.LEFT)

        self.vbox.pack_start(self.label, True, True, 0)


        self.entry = Gtk.Entry()
        self.vbox.pack_start(self.entry, True, True, 0)

        # self.entry.set_text("Hello World")

        self.button = Gtk.Button(label="Search")
        self.button.connect("clicked", self.on_button_clicked)

        self.vbox.pack_start(self.button, True, True, 0)
        # self.add(self.vbox)

    def on_button_clicked(self, widget):
        print( "Hello "+self.entry.get_text())
        # self.remove(self.vbox)

        print ("Removing children")
        for child in self.vbox.get_children():
            self.vbox.remove(child)
        # import ultraviol.spectrum.PlatformProviderDbSpectrum as pps
        # provider = pps.PlatformProviderSpectrum()

        # queryString = input("Enter the game name you want to search for:")
        queryString = self.entry.get_text()
        print("Searching for %s..." % queryString)

        # selectedGame= provider.searchRom(queryString)
        selectGameWin = ultraviol.gtk.selectGameWindow.selectGameWindow()
        selectGameWin.queryText=queryString
        selectGameWin.connect("delete-event", Gtk.main_quit)
        selectGameWin.show_all()




win = ultravioletMainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()



