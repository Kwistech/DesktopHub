from tkinter import Button


def github(app, frame, width, height, padx, pady):
    gh = Button(frame, text="GitHub", width=width * 2, height=height,
                      command=lambda: app.action(text="GitHub"))
    gh.grid(row=5, column=0, columnspan=2, padx=padx, pady=pady * 2)
