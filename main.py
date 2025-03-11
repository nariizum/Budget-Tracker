import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

root = tk.Tk()
root.title("Budget")
root.geometry("330x500")  

salary_frame = tk.Frame(root)
salary_frame.grid(row=0, column=0, sticky="nsew")

tk.Label(salary_frame, text="Enter your Salary", font=("Arial", 14)).pack(pady=10)

salary_entry_var = tk.StringVar()
salary_entry = tk.Entry(salary_frame, textvariable=salary_entry_var, font=("Arial", 14), justify="center")
salary_entry.pack(pady=5)
salary = 0 

def switch_to_expenses():
    global salary
    salary = float(salary_entry_var.get())  
    print("Salary entered:", salary)
    expenses_frame.tkraise()

add_expenses_button = tk.Button(salary_frame, text="Add Expenses", font=("Arial", 14), command=lambda: switch_to_expenses())
add_expenses_button.pack(pady=10)

expenses_frame = tk.Frame(root)
expenses_frame.grid(row=0, column=0, sticky="nsew")

tk.Label(expenses_frame, text="Enter your expenses", font=("Arial", 14)).grid(row=0, column=1, columnspan=3, pady=10, sticky="w")

expenses_var = tk.StringVar()
expenses_entry = tk.Entry(expenses_frame, textvariable=expenses_var, font=("Arial", 14), justify="center", width=15)
expenses_entry.grid(row=1, column=0, columnspan=3, pady=5, padx=20)

categories = ['Eating out', 'Transport', 'Groceries', 'Utilities', 'Entertainment', 'Other']
category_var = tk.StringVar()
category_var.set(categories[0])

category_menu = tk.OptionMenu(expenses_frame, category_var, *categories)
category_menu.grid(row=1, column=3, padx=10, pady=5)

expenses = {category: 0 for category in categories}

def on_click(button_val):
    selected_cat = category_var.get()
    
    if button_val == '✔':  
        try:
            expenses[selected_cat] += float(expenses_var.get())  
            print(f"{selected_cat} expense updated to: {expenses[selected_cat]}")
            expenses_var.set("")
        except ValueError:
            print("Invalid input, please enter a valid number.")
        
    elif button_val == 'c':  
        expenses_var.set("")  
        expenses[selected_cat] = 0  
    else:  
        expenses_var.set(expenses_var.get() + button_val)

button_frame = tk.Frame(expenses_frame)
button_frame.grid(row=2, column=0, columnspan=4, pady=10)

buttons = [
    ('1', '2', '3'),
    ('4', '5', '6'),
    ('7', '8', '9'),
    ('c', '0', '✔')
]

for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        btn = tk.Button(button_frame, text=text, font=("Arial", 16), width=5, height=2,
                        command=lambda t=text: on_click(t))
        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

for i in range(3):
    button_frame.columnconfigure(i, weight=1)

def show_analysis():
    filtered_expenses = {category: value for category, value in expenses.items() if value > 0}
    y = np.array(list(filtered_expenses.values()))
    categories = list(filtered_expenses.keys())
    
    if len(y) == 0: 
        print("No expenses entered!")
        return
    
    plt.pie(y, labels=categories, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  
    plt.title(f"Expenses Breakdown")
    
    print(f"Salary: ${salary}")
    print(f"Total Expenses: ${sum(y)}")
    print(f"Remaining Salary: ${salary - sum(y)}")
    
    plt.show()

analysis_button = tk.Button(expenses_frame, text="Show Analysis", font=("Arial", 14), command=show_analysis)
analysis_button.grid(row=3, column=0, columnspan=4, pady=10)

salary_frame.tkraise()

root.mainloop()
