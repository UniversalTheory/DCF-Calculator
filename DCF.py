# A short script for calculating the future value of a company in a given time period using the DCF model

# Necessary variables include: 
# Cash flow, growth rate, rate of return, and timeframe for prediction 

import tkinter as tk
from tkinter import messagebox

# Function to calculate the future value
def calculate_future_value():
    try:
        cf = float(cf_entry.get())
        g = float(g_entry.get())
        r = float(r_entry.get())
        n = int(n_entry.get())
        
        if r == g:
            raise ValueError("The discount rate (r) cannot be equal to the growth rate (g).")
        
        fv = cf * ((1 + g) ** n) / (r - g)
        result_label.config(text=f"Estimated Future Value: {round(fv, 2)}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
        
def clear_input_fields():
    cf_entry.delete(0, tk.END)
    g_entry.delete(0, tk.END)
    r_entry.delete(0, tk.END)
    n_entry.delete(0, tk.END)
    result_label.config(text="")

# Creating the main window
window = tk.Tk()
window.title("Company Value Estimator")

# Creating labels and entry fields for the variables
tk.Label(window, text="Annual Free Cash Flow (CF):").pack()
cf_entry = tk.Entry(window)
cf_entry.pack()

tk.Label(window, text="Expected Annual Growth Rate (g) (e.g., 0.05 for 5%):").pack()
g_entry = tk.Entry(window)
g_entry.pack()

tk.Label(window, text="Required Rate of Return (r) (e.g., 0.1 for 10%):").pack()
r_entry = tk.Entry(window)
r_entry.pack()

tk.Label(window, text="Number of Years to Predict (n):").pack()
n_entry = tk.Entry(window)
n_entry.pack()

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_future_value)
calculate_button.pack()

# Clear button
clear_button = tk.Button(window, text="Clear", command=clear_input_fields)
clear_button.pack()

# Result label
result_label = tk.Label(window, text="", font=('bold', 14))
result_label.pack()

# Run the application
window.mainloop()