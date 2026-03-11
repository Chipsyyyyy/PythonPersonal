import tkinter as tk

window = tk.Tk() # Create new instance of the tk object
window.title("Simple App") # Title of the app

# # Labels
# label = tk.Label(window, text="Hello") # Create a label
# label.pack() # Places the label inside the window

# # Buttons
# button = tk.Button(window, text="Stop", width=25, command=window.destroy) # Create a button of width 25 and 'destroy' the window when pressed
# button.pack() # Places the button inside the window

# Input

# tk.Label(window, text="First Name").grid(row=0, column=0)
# tk.Label(window, text="Last Name").grid(row=1, column=0)

# entry1 = tk.Entry(window) # Create single-line text input box
# entry2 = tk.Entry(window)

# entry1.grid(row=0, column=1) # Grid arranges the widgets in rows and columns
# entry2.grid(row=1, column=1)

# Check Box

# var1 = tk.IntVar() # Stores the checkbox state (1 or 0)
# var2 = tk.IntVar()

# tk.Checkbutton(window, text="Male", variable=var1).grid(row=0, sticky=tk.W) # sticky=tk.W : aligns the checkbow to the left
# tk.Checkbutton(window, text="Female", variable=var2).grid(row=1, sticky=tk.W)

# Radio Button - Exactly one option

# v = tk.IntVar() # Stores the selected option value

# tk.Radiobutton(window, text="A", variable=v, value=1).pack(anchor=tk.W) # Creates the radio button | value : assigns value when the radio button is selected
# tk.Radiobutton(window, text="B", variable=v, value=2).pack(anchor=tk.W) # anchor=tk.W : Aligns buttons to the left

# Listbox - List of items which the user can select one or more(?) 

lb = tk.Listbox(window)
lb.insert(1, "Python")
lb.insert(2, "Java")
lb.insert(3, "C++")
lb.insert(4, "Any Other")

lb.pack()
window.mainloop() # Run the app