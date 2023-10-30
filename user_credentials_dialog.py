import tkinter as tk


class UserCredentialsDialog:
    """Create input dialog with username and password fields"""

    def __init__(self) -> None:
        # initialize entry fields
        self.username_entry = None
        self.password_entry = None

        # initialize tk
        self.root = tk.Tk()

        # declare padding for modal elements
        self.padding = {'padx': 50, 'pady': 5}

        # set the window's dimensions and position
        self.window_width, self.window_height = self.calculate_dialog_dimensions()
        self.x, self.y = self.calculate_dialog_pos()
        self.root.geometry(f'{self.window_width}x{self.window_height}+{self.x}+{self.y}')

        # create input fields
        username_label = tk.Label(self.root, text="username:")
        username_entry = tk.Entry(self.root)
        username_entry.focus_set()  # set focus on the firs entry element
        username_label.pack(self.padding)
        username_entry.pack(self.padding)

        password_label = tk.Label(self.root, text="password:")
        password_entry = tk.Entry(self.root, show='*')  # show='*' -> hides characters
        password_label.pack(self.padding)
        password_entry.pack(self.padding)

        def handle_input_values() -> None:
            username = username_entry.get()
            password = password_entry.get()

            # kill dialog
            self.root.destroy()

            print(username, password)
            # save username and password as instance variables
            self.username_entry = username
            self.password_entry = password

        # handle submitting
        submit_button = tk.Button(self.root, text="Submit", command=handle_input_values)
        self.root.bind('<Return>', lambda event=None: submit_button.invoke())  # submit dialog on enter click
        submit_button.pack(self.padding)

        self.root.mainloop()

    def calculate_dialog_dimensions(self) -> (int, int):
        """Calculate the dimensions of the dialog based on your device's screen resolution"""

        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()

        return width // 7, height // 6

    def calculate_dialog_pos(self) -> (int, int):
        """Calculate where to position the dialog on your screen"""

        x = (self.root.winfo_screenwidth() - self.window_width) // 2
        y = (self.root.winfo_screenheight() - self.window_height) // 3

        return x, y

    def get_credentials(self) -> (str, str):
        """Getter for user credentials (username, password)"""
        return self.username_entry, self.password_entry
