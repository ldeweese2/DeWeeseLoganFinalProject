"""
Logan DeWeese

10/6/2023

Final Project

Expense Tracker Lite
This Python application is a simple Expense Tracker Lite built using the Tkinter library 
for creating a graphical user interface. It helps users track their expenses by entering 
the expense amount and category
"""

import tkinter as tk
from tkinter import Entry, Button, Label, Toplevel, messagebox

# Define some custom colors
primary_color = "#3498db"  # Blue color
secondary_color = "#e74c3c"  # Red color
window_background_color = "#ecf0f1"  # Gray color for window backgrounds

# Callback functions
def add_expense():
    expense_text = expense_entry.get()
    category_text = category_entry.get()

    if not expense_text or not category_text:
        messagebox.showerror("Error", "Both fields are required.")
        return

    try:
        expense_amount = float(expense_text)
    except ValueError:
        messagebox.showerror("Error", "Expense must be a valid number.")
        return

    # Store the expense data and update the summary
    expenses.append((expense_amount, category_text))
    update_summary()
    expense_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

def view_summary():
    summary_window = Toplevel(root)
    summary_window.title("Expense Summary")
    summary_window.geometry("700x700")  # Set the summary window size

    # Create a frame with a gray background for the summary window
    summary_frame = tk.Frame(summary_window, bg=window_background_color)
    summary_frame.pack(fill=tk.BOTH, expand=True)

    # Display the summary in the frame
    summary_label = Label(summary_frame, text="Expense Summary", font=("Helvetica", 16))
    summary_label.pack()

    for expense, category in expenses:
        expense_label = Label(summary_frame, text=f"{category}: ${expense:.2f}", font=("Helvetica", 12))
        expense_label.pack()

    

def exit_app():
    root.destroy()

def update_summary():
    total_expense = sum(expense for expense, _ in expenses)
    summary_label.config(text=f"Total Expenses: ${total_expense:.2f}", font=("Helvetica", 14))

# Initialize the main window with a larger size
root = tk.Tk()
root.title("Expense Tracker Lite")
root.geometry("700x700")  # Set the initial size to 400x400 pixels

# Create a frame with a gray background for the main window
main_frame = tk.Frame(root, bg=window_background_color)
main_frame.pack(fill=tk.BOTH, expand=True)

# Create and pack labels, entry widgets, and buttons with custom styles, centered in the window
expense_label = Label(main_frame, text="Expense:", font=("Helvetica", 12), bg=window_background_color)
expense_label.pack(pady=10)  # Add padding at the top

expense_entry = Entry(main_frame, font=("Helvetica", 12))
expense_entry.pack(pady=10)  # Add padding between the input boxes

category_label = Label(main_frame, text="Category:", font=("Helvetica", 12), bg=window_background_color)
category_label.pack(pady=10)  # Add padding between the input boxes

category_entry = Entry(main_frame, font=("Helvetica", 12))
category_entry.pack(pady=10)  # Add padding between the input boxes

add_button = Button(main_frame, text="Add Expense", command=add_expense, bg=primary_color, fg="white", font=("Helvetica", 12))
add_button.pack(pady=10)  # Add padding below the button

summary_button = Button(main_frame, text="View Summary", command=view_summary, bg=primary_color, fg="white", font=("Helvetica", 12))
summary_button.pack(pady=10)  # Add padding below the button

exit_button = Button(main_frame, text="Exit", command=exit_app, bg=secondary_color, fg="white", font=("Helvetica", 12))
exit_button.pack(pady=10)  # Add padding below the button

# Initialize expenses list
expenses = []

# Create and pack a label for the summary
summary_label = Label(main_frame, text="", font=("Helvetica", 14))
summary_label.pack()

# Load the first image using tkinter.PhotoImage (adjust the path as needed)
image1 = tk.PhotoImage(file="images\\money.gif")
image1_label = Label(main_frame, image=image1, width=300, height=300)  # Adjust width and height as needed
image1_label.pack(side=tk.LEFT, padx=10)  # Use pack for both images and specify side

# Load the second image using tkinter.PhotoImage (adjust the path as needed)
image2 = tk.PhotoImage(file="images\\money4.gif")  # Change the file path to your second image
image2_label = Label(main_frame, image=image2, width=300, height=300)  # Adjust width and height as needed
image2_label.pack(side=tk.RIGHT, padx=10)  # Use pack for both images and specify side




# Start the Tkinter main loop
root.mainloop()
