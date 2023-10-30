import sort_mechanism as sm
import tkinter as tk
from tkinter import messagebox


class SortingApp():
    def __init__(self):
        self.root = tk.Tk()

        window_width = 600
        window_height = 300

        center_window(self.root, window_width, window_height)  # funkcja sprawiająca że okno apki jest na środku ekranu
        self.root.title("Sortowanie")
        self.label = tk.Label(self.root, text="Please type in the list you want to sort:", font=('Arial', 18))
        self.label.pack(padx=10, pady=10) #uruchamia label i ustawiamy marginesy

        self.textbox = tk.Text(self.root, height=1, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.input_button = tk.Button(self.root, text = "input data", command=self.user_input)
        self.input_button.pack(padx=10, pady=10)
        self.your_list = tk.Label(self.root, text=f"Your list:  ")
        self.your_list.pack()
        # welcome_message()

        self.root.mainloop()

    def user_input(self):
        unsorted = []
        user_input = self.textbox.get("1.0", tk.END)  # Get the text from the Entry widget
        user_input_list = user_input.split(" ")       # Split the input into a list
        for i in range(len(user_input_list)):  
            element = int(user_input_list[i])
            unsorted.append(element)
        print("User input list:", unsorted)
        self.your_list.config(text = f"Your list: {unsorted}")


def welcome_message():
    messagebox.showinfo("Welcome", "Hey, welcome to my app!")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")















#test działania importowania
# print(sm.bubblesort([0,5,87,2,45,1]))
# print(sm.quicksort([0,5,87,2,45,1]))
SortingApp()

#tutaj próba zrobienie pliku exe
#pyinstaller --onefile your_app.py
