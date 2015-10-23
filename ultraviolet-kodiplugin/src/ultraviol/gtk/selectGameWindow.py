__author__ = 'developer'

from gi.repository import Gtk

# import ultraviol.spectrum.PlatformProviderDbSpectrum as pps

class selectGameWindow(Gtk.Window):

    title="Ultraviolet - Game selection"
    queryText="Batman"

    # conf = conf.loadConfiguration()

    def __init__(self):
        print ("init selectGameWindow")
        self.performSearch()
        self.drawWindow()



    def performSearch(self):
        print("Searching for %s" % self.queryText)
        ultraviol.spectrum.PlatformProviderDbSpectrum.searchRom(self.queryText)


    def drawWindow(self):

        Gtk.Window.__init__(self, title=self.title)
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text("Select game")
        self.vbox.pack_start(self.entry, True, True, 0)

        # self.entry.set_text("Hello World")

        self.button = Gtk.Button(label="Select")
        self.button.connect("clicked", self.on_button_clicked)

        self.vbox.pack_start(self.button, True, True, 0)
        # self.add(self.vbox)


    def addGameList(self,widget, gameList):
        print ("addGameList")
        # http://python-gtk-3-tutorial.readthedocs.org/en/latest/combobox.html
        store = Gtk.ListStore(str)
        list = {("aaaa"),("bbbb")}

        self.treeview = Gtk.TreeView.new_with_model(store)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Title", renderer, text=0)

        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.scrollable_treelist.add(self.treeview)

        # self.add(self.scrollable_treelist)
        self.vbox.pack_start(self.scrollable_treelist, True, True, 0)
        self.vbox.show_all()

    def addFileList(self,widget):
        print("addRomList")

    def addRomList(self,widget):
        print("addRomList")




win = selectGameWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
