import tkinter as tk
import tkinter.font as font


def menu_button_font():
    return font.Font(size=30, weight='bold')


class FantasyNotes(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Fantasy Notes')
        width = 640
        height = 720
        self.geometry(f'{width}x{height}')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.container = tk.Frame(self)
        self.container.grid_rowconfigure(1, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        for F in (MainMenu, LoadNotebookMenu, CreateNotebookMenu, OptionsMenu):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=1, column=0, sticky='nsew')
        self.show_frame(MainMenu)
        self.container.grid(row=0, column=0, pady=10, padx=10, sticky='nsew')

    def set_stickiness(self, isTrue):
        self.attributes('-topmost', isTrue)
        self.update()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class MainMenu(tk.Frame):
    def __init__(self, container, controller):
        tk.Frame.__init__(self, container)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        tk.Button(self, text='Load notebook', font=menu_button_font(),
                  command=lambda: controller.show_frame(LoadNotebookMenu)).grid(
            row=0, column=0, sticky='nsew')
        tk.Button(self, text='New notebook', font=menu_button_font(),
                  command=lambda: controller.show_frame(CreateNotebookMenu)).grid(
            row=1, column=0, sticky='nsew')
        tk.Button(self, text='Options', font=menu_button_font(),
                  command=lambda: controller.show_frame(OptionsMenu)
                  ).grid(row=2, column=0, sticky='nsew')


class LoadNotebookMenu(tk.Frame):
    def __init__(self, container, controller):
        tk.Frame.__init__(self, container)
        tk.Button(self, text='Back', font=menu_button_font(),
                  command=lambda: controller.show_frame(MainMenu)).grid(row=0, column=1, sticky='nsew')
        v = tk.IntVar()
        v.set(0)
        notebooks = [('Notebook 1', 1),
                     ('Notebook 2', 2),
                     ('Notebook 3', 3),
                     ('Notebook 4', 4),
                     ('Notebook 5', 5)]
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1, uniform='test')
        self.grid_columnconfigure(1, weight=1, uniform='test')
        self.grid_columnconfigure(2, weight=1, uniform='test')
        self.options_container = tk.Frame(self)
        self.options_container.grid_columnconfigure(0, weight=1)
        for i in range(len(notebooks)):
            self.options_container.grid_rowconfigure(i,  weight=1, uniform='test2')
        for notebook, val in notebooks:
            tk.Radiobutton(self.options_container,
                           text=notebook,
                           indicatoron=0,
                           variable=v,
                           # command=ShowChoice,
                           value=val).grid(sticky='nsew')
        self.options_container.grid(row=1, columnspan=3, sticky='nsew')
        self.grid()


class CreateNotebookMenu(tk.Frame):
    def __init__(self, container, controller):
        tk.Frame.__init__(self, container)
        tk.Button(self, text='Back', font=menu_button_font(),
                  command=lambda: controller.show_frame(MainMenu)).grid(row=0, column=0, sticky='w')


class OptionsMenu(tk.Frame):
    def __init__(self, container, controller):
        tk.Frame.__init__(self, container)
        self.controller = controller
        tk.Button(self, text='Back', font=menu_button_font(),
                  command=lambda: controller.show_frame(MainMenu)).grid(row=0, column=0, sticky='w')
        self.always_on_top = tk.IntVar()
        self.always_on_top.set(1)
        tk.Checkbutton(self, text='Enable sticky mode',
                       variable=self.always_on_top,
                       command=self.always_on_top_is_checked_callback).grid(
                           row=1, column=0, sticky='w', padx=10)

    def always_on_top_is_checked_callback(self):
        self.controller.set_stickiness(self.always_on_top.get())


def load():
    app = FantasyNotes()
    app.set_stickiness(True)
    app.mainloop()


if __name__ == '__main__':
    load()
