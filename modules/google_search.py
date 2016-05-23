# Google Search module for DesktopHub
from tkinter import Entry, Button


def google_search(app, frame, width, height, padx, pady):
    """Create Google Search tkinter Entry and Button for DesktopHub.

    Args:
        app (__main__.App): Class App from main.py.
        frame (tkinter.Frame): tkinter Frame for App.
        width (int): Button width.
        height (int): Button height.
        padx (int): Button padx kwarg.
        pady (int): Button pady kwarg.
    """
    search = Entry(frame, width=width * 2 + padx * 2)
    search.grid(row=6, column=0, columnspan=2, padx=padx, pady=pady)

    g_search = Button(frame, text="Google Search", height=height,
                      command=lambda: app.action(text="Google", query=search))
    g_search.grid(row=7, column=0, columnspan=2, sticky="N")
