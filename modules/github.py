# Github module for DesktopHub
from tkinter import Button


def github(app, frame, width, height, padx, pady):
    """Create GitHub tkinter Button for DesktopHub.

    Args:
        app (__main__.App): Class App from main.py.
        frame (tkinter.Frame): tkinter Frame for App.
        width (int): Button width.
        height (int): Button height.
        padx (int): Button padx kwarg.
        pady (int): Button pady kwarg.
    """
    gh = Button(frame, text="GitHub", width=width * 2, height=height,
                      command=lambda: app.action(text="GitHub"))
    gh.grid(row=5, column=0, columnspan=2, padx=padx, pady=pady * 2)
