from tkinter import Button


def python_paths(app, frame, width, height, padx, pady):
    path_python = "C:\\Users\John\AppData\Local\Programs\Python\Python35-32"
    site_pkgs = "C:\\Users\John\AppData\Roaming\Python\Python35\site-packages"

    python = Button(frame, text="Python", width=width, height=height,
                    command=lambda: app.action(text="Python"))
    python.grid(row=4, column=0, padx=padx, pady=pady)

    pkgs = Button(frame, text="Pkgs", width=width, height=height,
                  command=lambda: app.action(text="Pkgs"))
    pkgs.grid(row=4, column=1, padx=padx, pady=pady)

    return path_python, site_pkgs
