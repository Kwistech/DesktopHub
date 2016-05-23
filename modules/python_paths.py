# Python Paths module for DesktopHub
from tkinter import Button


def python_paths(app, frame, width, height, padx, pady):
    """Create Python Paths tkinter Buttons for DesktopHub.

    Note: Change path_python and site_pkgs to the equivalent path on user's
    machine.

    Args:
        app (__main__.App): Class App from main.py.
        frame (tkinter.Frame): tkinter Frame for App.
        width (int): Button width.
        height (int): Button height.
        padx (int): Button padx kwarg.
        pady (int): Button pady kwarg.

    Returns:
        tuple: [0]=path_python (str); [1]=site_pkgs (str).
    """
    # Path variables (change)
    path_python = "C:\\Users\John\AppData\Local\Programs\Python\Python35-32"
    site_pkgs = "C:\\Users\John\AppData\Roaming\Python\Python35\site-packages"

    python = Button(frame, text="Python", width=width, height=height,
                    command=lambda: app.action(text="Python"))
    python.grid(row=4, column=0, padx=padx, pady=pady)

    pkgs = Button(frame, text="Pkgs", width=width, height=height,
                  command=lambda: app.action(text="Pkgs"))
    pkgs.grid(row=4, column=1, padx=padx, pady=pady)

    return path_python, site_pkgs
