import tkinter as tk

# Function to update the display with button clicks
def click(event):
    current_text = display.get()
    new_text = current_text + str(event)
    display.delete(0, tk.END)
    display.insert(tk.END, new_text)

# Function to clear the display
def clear():
    display.delete(0, tk.END)

# Function to calculate the expression in the display
def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Set up main application window
root = tk.Tk()
root.title("Simple Calculator")

# Display for inputs and results
display = tk.Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons configurations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

for (text, row, column) in buttons:
    if text.isdigit():
        action = lambda e=text: click(e)
    elif text == 'C':
        action = clear
    elif text == '=':
        action = calculate
    else:
        action = lambda e=text: click(e)

    tk.Button(root, text=text, width=9, height=3, command=action).grid(row=row, column=column)

# Run the application
root.mainloop()