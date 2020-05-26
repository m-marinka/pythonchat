from tkinter import Frame, Label, Entry, Button, Text, messagebox, Tk, Scrollbar, VERTICAL


class GUI:
    def __init__(self, master):
        self.root = master
        self.name_widget = None
        self.join_button = None
        self.enter_text_widget = None
        self.chat_area = None
        self.initialize_gui()  # call method here

    def initialize_gui(self):
        self.root.title('socket chat')  # window title
        self.root.resizable(0, 0)
        self.display_name_section()
        self.chat_box()
        self.chat_entry_box()

    def display_name_section(self):
        frame = Frame()
        Label(frame, text='Enter your name: ', font=("Serif", 12)).pack(side='top', anchor='w')
        self.name_widget = Entry(frame, width=50, borderwidth=2)
        self.name_widget.pack(side='left', anchor='e')
        self.join_button = Button(frame, text='Join', width=10, command=self.on_join).pack(side='left')
        frame.pack(side='top', anchor='w')

    def chat_box(self):
        frame = Frame()
        Label(frame, text='Chat Box:', font=("Serif", 12)).pack(side='top', anchor='w')
        self.chat_area = Text(frame, width=60, height=10, font=("Serif", 12))
        scrollbar = Scrollbar(frame, command=self.chat_area.yview, orient=VERTICAL)
        self.chat_area.bind('<KeyPress>', lambda e: 'break')
        self.chat_area.pack(side='left', padx=10)
        scrollbar.pack(side='right', fill='y')
        frame.pack(side='top')

    def chat_entry_box(self):
        frame = Frame()
        Label(frame, text='Enter message: ', font=("Serif", 12)).pack(side='top', anchor='w')
        self.enter_text_widget = Text(frame, width=60, height=3, font=("Serif", 12)).pack(side='top', anchor='w')
        # self.enter_text_widget.pack(side='left', pady=15)
        # self.enter_text_widget.bind('<Return>', self.on_enter_key_pressed)
        frame.pack(side='top')

    def on_join(self):
        if len(self.name_widget.get()) == 0:
            messagebox.showerror("Enter your name", "Enter your name to send message")
            return
        self.name_widget.config(state='disabled')

    def on_enter_key_pressed(self):
        if len(self.name_widget.get()) == 0:
            messagebox.showerror("Enter your name", "Enter your name to send message")
            return

    def on_close_window(self):
        if messagebox.askokcancel("Quit", "Do you want to exit? "):
            self.root.destroy()
            exit(0)


# run window here

if __name__ == '__main__':
    root = Tk()
    gui = GUI(root)
    root.protocol('WM_DELETE_WINDOW', gui.on_close_window)
    root.mainloop()
