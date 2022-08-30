import tkinter as ttk
from tkinter import filedialog as fd

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Label
        self.label = ttk.Label(self, text='Chemin du fichier :')
        self.label.grid(row=1, column=0)

        # Entry
        self.path_var = ttk.StringVar()
        self.path_entry = ttk.Entry(self, textvariable=self.path_var, width=50)
        self.path_entry.grid(row=1, column=1, sticky=ttk.NSEW)

        # Select file Button
        self.upload_button = ttk.Button(self, text='...', command=self.search_file_button_clicked)
        self.upload_button.grid(row=1, column=3, padx=10)

        # Upload Button
        self.upload_button = ttk.Button(self, text='Envoyer', command=self.upload_button_clicked)
        self.upload_button.grid(row=1, column=4, padx=10)

        # Message de confirmation
        self.message_label = ttk.Label(self, text='', foreground='green')
        self.message_label.grid(row=2, column=1, sticky=ttk.W)

        # Controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def search_file_button_clicked(self):
        path = fd.askopenfilename(title='Ouvrir une video')
        self.path_entry.insert(0, path)

    def upload_button_clicked(self):
        if self.controller:
            self.controller.upload(self.path_var.get())

    def show_success(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

    def show_error(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.path_entry['foreground'] = 'red'

    def hide_message(self):
        self.message_label['text'] = ''
