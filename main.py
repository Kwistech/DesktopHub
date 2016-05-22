# DesktopHub - Johnathon Kwisses (Kwistech)
from subprocess import Popen
from tkinter import *
from webbrowser import open_new

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

    def __init__(self):
        self._frame = Frame()
        self._frame.pack()

        self._width = 5
        self._height = 1
        self._padx = 5
        self._pady = 5

        self._c_drive_path = "C:\\"
        self._d_drive_path = "D:\\"
        self._docs_path = "C:\\Users\John\Documents"
        self._dls_path = "C:\\Users\John\Downloads"

        self._interface()
        self._load_modules()

    def _interface(self):
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
        try:
            mod1 = python_paths(self, self._frame, self._width, self._height,
                                self._padx, self._pady)
            python_paths(self, self._frame, self._width, self._height,
                         self._padx, self._pady)
        except NameError:
            mod1 = None

        try:
            mod2 = google_search(self, self._frame, self._width, self._height,
                                 self._padx, self._pady)
        except NameError:
            mod2 = None

        try:
            mod3 = github(self, self._frame, self._width, self._height,
                          self._padx, self._pady)
        except NameError:
            mod3 = None

        return mod1, mod2, mod3

    def action(self, text, query=None):
        path = "."

        if text == "C:":
            path = self._c_drive_path
        elif text == "D:":
            path = self._d_drive_path
        elif text == "Docs":
            path = self._docs_path
        elif text == "DLs":
            path = self._dls_path

        elif text == "Python":
            path = self._load_modules()[0][0]
        elif text == "Pkgs":
            path = self._load_modules()[0][1]

        elif text == "GitHub":
            open_new("www.github.com/".format(query))
            return

        elif text == "Google":
            query = query.get()
            open_new("www.google.ca/#q={}".format(query))
            return

        Popen(r'explorer "{}"'.format(path))


def main():
    root = Tk()
    root.title("DesktopHub")
    root.resizable(0, 0)

    App()

    root.mainloop()

if __name__ == "__main__":
    main()
