from tkinter import *
from tkinter import messagebox

# Function to calculate the percentile
def calculate_percentile(event=None):
    try:
        total = int(entry_total.get())
        rank = int(entry_rank.get())
        
        if rank < 1 or rank > total:
            raise ValueError("Rank must be between 1 and the total number of participants.")
        
        percentile = round((total - rank) / total * 100, 2)
        
        # Change the result color based on the percentile
        if percentile >= 75:
            result_label.config(fg="green")
        elif 50 <= percentile < 75:
            result_label.config(fg="orange")
        else:
            result_label.config(fg="red")
        
        # Display the result
        result_label.config(text=f"Percentile: {percentile}%")
    
    except ValueError as e:
        result_label.config(fg="red")
        result_label.config(text=str(e))

# Function to reset the fields
def reset_fields():
    entry_rank.delete(0, END)
    entry_total.delete(0, END)
    result_label.config(text="Percentile: --", fg="black")

# Function to show the user guide
def show_guide():
    guide_text = (
        "Welcome to RankWise!\n\n"
        "To calculate the percentile, enter:\n"
        "- Your rank in the list.\n"
        "- The total number of participants.\n\n"
        "The percentile will be calculated automatically."
    )
    messagebox.showinfo("Guide", guide_text)

# Main window setup
app = Tk()
app.title("RankWise: Percentile Analyzer")
app.geometry("500x300")
app.config(bg="lightyellow")

# Application title
title_label = Label(app, text="RankWise: Percentile Analyzer", font=("Arial", 16, "bold"), bg="lightyellow")
title_label.pack(pady=10)

# Input area for rank and total participants
frame_input = Frame(app, bg="lightyellow")
frame_input.pack(pady=10)

label_rank = Label(frame_input, text="Rank:", font=("Arial", 12), bg="lightyellow")
label_rank.grid(row=0, column=0, padx=5, pady=5)

entry_rank = Entry(frame_input, font=("Arial", 12))
entry_rank.grid(row=0, column=1, padx=5, pady=5)
entry_rank.bind("<KeyRelease>", calculate_percentile)  # Automatically calculate when the value changes

label_total = Label(frame_input, text="Total Participants:", font=("Arial", 12), bg="lightyellow")
label_total.grid(row=1, column=0, padx=5, pady=5)

entry_total = Entry(frame_input, font=("Arial", 12))
entry_total.grid(row=1, column=1, padx=5, pady=5)
entry_total.bind("<KeyRelease>", calculate_percentile)  # Automatically calculate when the value changes

# Area to display the result
result_label = Label(app, text="Percentile: --", font=("Arial", 14), bg="lightyellow")
result_label.pack(pady=20)

# Buttons to reset fields and show the guide
frame_buttons = Frame(app, bg="lightyellow")
frame_buttons.pack(pady=10)

reset_button = Button(frame_buttons, text="Reset", font=("Arial", 12), command=reset_fields, bg="lightblue")
reset_button.grid(row=0, column=0, padx=10)

guide_button = Button(frame_buttons, text="Guide", font=("Arial", 12), command=show_guide, bg="lightgreen")
guide_button.grid(row=0, column=1, padx=10)

# Start the main loop
app.mainloop()
