# DesktopHub - Johnathon Kwisses (Kwistech)
from subprocess import Popen
from tkinter import *


class App:

    def __init__(self):
        self._frame = Frame()
        self._frame.pack()

        self._width = 5
        self._height = 5
        self._padx = 5
        self._pady = 5

        self._c_drive_path = "C:\\"
        self._d_drive_path = "D:\\"
        self._docs_path = "C:\\Users\John\Documents"
        self._dls_path = "C:\\Users\John\Downloads"

        self._interface()

    def _interface(self):
        header = Label(self._frame, text="DesktopHub")
        header.grid(row=0, column=0, columnspan=2)

        c_drive = Button(self._frame, text="C:", width=self._width,
                         command=lambda: self._action("C:"))
        c_drive.grid(row=1, column=0, padx=self._padx, pady=self._pady)

        d_drive = Button(self._frame, text="D:", width=self._width,
                         command=lambda: self._action("D:"))
        d_drive.grid(row=1, column=1, padx=self._padx, pady=self._pady)

        docs = Button(self._frame, text="Docs", width=self._width,
                      command=lambda: self._action("Docs"))
        docs.grid(row=2, column=0, padx=self._padx, pady=self._pady)

        dls = Button(self._frame, text="DLs", width=self._width,
                     command=lambda: self._action("DLs"))
        dls.grid(row=2, column=1, padx=self._padx, pady=self._pady)

        footer = Label(self._frame, text="© 2016 Kwistech")
        footer.grid(row=3, column=0, columnspan=2, sticky="E")

    def _action(self, text):
        path = "."

        if text == "C:":
            path = self._c_drive_path
        elif text == "D:":
            path = self._d_drive_path
        elif text == "Docs":
            path = self._docs_path
        elif text == "DLs":
            path = self._dls_path

        self._open(path)

    @staticmethod
    def _open(path):
        Popen(r'explorer "{}"'.format(path))


def main():
    root = Tk()
    root.title("DesktopHub")

    App()

    root.mainloop()

if __name__ == "__main__":
    main()
