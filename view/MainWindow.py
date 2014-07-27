import pygtk
pygtk.require("2.0")
import gtk

class MainWindow(object):
  def __init__(self):
    builder = gtk.Builder()
    builder.add_from_file("view/main_window.glade")
    self.window = builder.get_object("main_window")
    self.window.show()
    builder.connect_signals({"gtk_main_quit": gtk.main_quit})