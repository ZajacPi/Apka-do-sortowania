import sort_mechanism as sm
import tkinter as tk

class SortingApp():
    def __init__(self):
        self.root = tk.Tk()
        
        self.root.mainloop()

#test działania importowania
print(sm.bubblesort([0,5,87,2,45,1]))

SortingApp()