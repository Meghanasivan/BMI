import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # convert cm to meters
        age = int(age_entry.get())
        gender = gender_var.get()

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "#4682B4"  # Blue
        elif 18.5 <= bmi < 25:
            category = "Normal"
            color = "#32CD32"  # Green
        elif 25 <= bmi < 30:
            category = "Overweight"
            color = "#FFA500"  # Orange
        else:
            category = "Obese"
            color = "#FF6347"  # Red

        # Age-specific feedback
        if age < 18:
            age_msg = "Note: BMI categories may differ for children and teens."
        elif age > 60:
            age_msg = "BMI may not reflect true body fat for older adults."
        else:
            age_msg = "Keep track of your BMI for better health."

        result_text = f"Your BMI: {bmi}\nCategory: {category}\n\n{age_msg}"
        result_label.config(text=result_text, fg=color)

        show_bmi_chart(bmi)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight, height, and age.")

def show_bmi_chart(bmi_value):
    for widget in chart_frame.winfo_children():
        widget.destroy()

    fig = Figure(figsize=(7, 1.7), dpi=100)
    ax = fig.add_subplot(111)

    # Define ranges and colors
    bmi_ranges = [18.5, 25, 30, 40]
    categories = ["Underweight", "Normal", "Overweight", "Obese"]
    colors = ["#4682B4", "#32CD32", "#FFA500", "#FF6347"]

    start = 10
    for i in range(len(bmi_ranges)):
        width = bmi_ranges[i] - start
        ax.barh(0, width, left=start, height=0.6, color=colors[i], edgecolor='black')
        ax.text(start + width / 2, 0, categories[i], ha='center', va='center', fontsize=9, color='white', fontweight='bold')
        start = bmi_ranges[i]

    # Marker line for user's BMI
    ax.axvline(bmi_value, color='black', linewidth=2)
    ax.text(bmi_value + 0.5, 0.25, f'⬆️ {bmi_value}', fontsize=9, color='black')

    # Chart formatting
    ax.set_xlim(10, 40)
    ax.set_xticks([10, 15, 20, 25, 30, 35, 40])
    ax.set_yticks([])
    ax.set_xlabel("BMI Scale")
    ax.set_title("BMI Category Chart", fontsize=12, pad=15)
    ax.grid(True, axis='x', linestyle='--', alpha=0.3)
    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=5)

# GUI setup
app = tk.Tk()
app.title("Advanced BMI Calculator")
app.geometry("580x690")
app.configure(bg="#f0faff")

tk.Label(app, text="Advanced BMI Calculator", font=("Helvetica", 18, "bold"), bg="#f0faff").pack(pady=10)

form_frame = tk.Frame(app, bg="#f0faff")
form_frame.pack(pady=5)

# Weight
tk.Label(form_frame, text="Weight (kg):", font=("Helvetica", 12), bg="#f0faff").grid(row=0, column=0, sticky="w", padx=10)
weight_entry = tk.Entry(form_frame, font=("Helvetica", 12))
weight_entry.grid(row=0, column=1, pady=5)

# Height
tk.Label(form_frame, text="Height (cm):", font=("Helvetica", 12), bg="#f0faff").grid(row=1, column=0, sticky="w", padx=10)
height_entry = tk.Entry(form_frame, font=("Helvetica", 12))
height_entry.grid(row=1, column=1, pady=5)

# Age
tk.Label(form_frame, text="Age:", font=("Helvetica", 12), bg="#f0faff").grid(row=2, column=0, sticky="w", padx=10)
age_entry = tk.Entry(form_frame, font=("Helvetica", 12))
age_entry.grid(row=2, column=1, pady=5)

# Gender
tk.Label(form_frame, text="Gender:", font=("Helvetica", 12), bg="#f0faff").grid(row=3, column=0, sticky="w", padx=10)
gender_var = tk.StringVar(value="Female")
tk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male", bg="#f0faff").grid(row=3, column=1, sticky="w")
tk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female", bg="#f0faff").grid(row=4, column=1, sticky="w")

# Calculate button
tk.Button(app, text="Calculate BMI", command=calculate_bmi, font=("Helvetica", 13), bg="#007B8A", fg="white", width=20).pack(pady=20)

# Result
result_label = tk.Label(app, text="", font=("Helvetica", 12, "bold"), bg="#f0faff", justify="left")
result_label.pack()

# Chart Area
chart_frame = tk.Frame(app, bg="#f0faff")
chart_frame.pack(pady=10)

# Footer
tk.Label(app, text="Made by Meghana Sivan", font=("Helvetica", 10, "italic"), bg="#f0faff", fg="gray").pack(side="bottom", pady=10)

app.mainloop()

