from tkinter import Entry, Button


def google_search(app, frame, width, height, padx, pady):
    search = Entry(frame, width=width * 2 + padx * 2)
    search.grid(row=6, column=0, columnspan=2, padx=padx, pady=pady)

    g_search = Button(frame, text="Google Search", height=height,
                      command=lambda: app.action(text="Google", query=search))
    g_search.grid(row=7, column=0, columnspan=2, sticky="N")
