# DesktopHub - Johnathon Kwisses (Kwistech)
from subprocess import Popen
from tkinter import *
from webbrowser import open_new

# For custom module imports
try:
    from modules.python_paths import python_paths
except ImportError:
    pass
try:
    from modules.google_search import google_search
except ImportError:
    pass
try:
    from modules.github import github
except ImportError:
    pass


class App:
    """Define the tkinter GUI and widget actions."""

    def __init__(self):
        """Load interface and module(s) with default parameters.

        Change the path variables to the equivalent path on user's machine.
        """
        # Frame for tkinter GUI
        self._frame = Frame()
        self._frame.pack()

        # Default parameters for interface
        self._width = 5
        self._height = 1
        self._padx = 5
        self._pady = 5

        # Path variables
        self._c_drive_path = "C:\\"
        self._d_drive_path = "D:\\"
        self._docs_path = "C:\\Users\John\Documents"
        self._dls_path = "C:\\Users\John\Downloads"

        # Loads tkinter GUI and module(s)
        self._interface()
        self._load_modules()

    def _interface(self):
        """Define the main interface for tkinter GUI."""
        header = Label(self._frame, text="DesktopHub")
        header.grid(row=0, column=0, columnspan=2)

        c_drive = Button(self._frame, text="C:", width=self._width,
                         command=lambda: self.action("C:"))
        c_drive.grid(row=1, column=0, padx=self._padx, pady=self._pady)

        d_drive = Button(self._frame, text="D:", width=self._width,
                         command=lambda: self.action("D:"))
        d_drive.grid(row=1, column=1, padx=self._padx, pady=self._pady)

        docs = Button(self._frame, text="Docs", width=self._width,
                      command=lambda: self.action("Docs"))
        docs.grid(row=2, column=0, padx=self._padx, pady=self._pady)

        dls = Button(self._frame, text="DLs", width=self._width,
                     command=lambda: self.action("DLs"))
        dls.grid(row=2, column=1, padx=self._padx, pady=self._pady)

        div = Label(self._frame, text="-" * (self._width * 2 + self._padx * 2))
        div.grid(row=3, column=0, columnspan=2)

        footer = Label(self._frame, text="© 2016 Kwistech")
        footer.grid(row=25, column=0, columnspan=2, sticky="E")

    def _load_modules(self):
        """Try to call module functions to load and display in GUI.

        Returns:
            tuple: Contains module functions; None if exception raised.

        Raises:
            NameError: Raised if function can't be called; sets mod=None.
        """
        # Module 1 - python_paths.py
        try:
            mod1 = python_paths(self, self._frame, self._width, self._height,
                                self._padx, self._pady)
            python_paths(self, self._frame, self._width, self._height,
                         self._padx, self._pady)
        except NameError:
            mod1 = None

        # Module 2 - github.py
        try:
            mod2 = github(self, self._frame, self._width, self._height,
                          self._padx, self._pady)
        except NameError:
            mod2 = None

        # Module 3 - google_search.py
        try:
            mod3 = google_search(self, self._frame, self._width, self._height,
                                 self._padx, self._pady)
        except NameError:
            mod3 = None

        return mod1, mod2, mod3

    def action(self, text, query=None):
        """Initiates button command upon button press.

        Args:
            text (str): Shorthand action to be performed.
            query (tkinter.Entry): Search query for browser searches.
        """
        # Default path (root dir)
        path = "."

        # Main GUI
        if text == "C:":
            path = self._c_drive_path
        elif text == "D:":
            path = self._d_drive_path
        elif text == "Docs":
            path = self._docs_path
        elif text == "DLs":
            path = self._dls_path

        # Module 1
        elif text == "Python":
            path = self._load_modules()[0][0]
        elif text == "Pkgs":
            path = self._load_modules()[0][1]

        # Module 2
        elif text == "GitHub":
            open_new("www.github.com/".format(query))
            return

        # Module 3
        elif text == "Google":
            query = query.get()
            open_new("www.google.ca/#q={}".format(query))
            return

        # Explorer opener
        Popen(r'explorer "{}"'.format(path))


def main():
    """Run main program loop with specified settings."""
    root = Tk()
    root.title("DesktopHub")
    root.resizable(0, 0)

    App()

    root.mainloop()

if __name__ == "__main__":
    main()
