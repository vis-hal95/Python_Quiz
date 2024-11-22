
import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Python-related questions and answers
questions = [
    {
        "question": "What is the correct syntax to output 'Hello, World!' in Python?",
        "options": ["print('Hello, World!')", "echo 'Hello, World!'", "printf('Hello, World!')", "echo('Hello, World!')"],
        "answer": "print('Hello, World!')"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["tuple", "list", "string", "int"],
        "answer": "list"
    },
    {
        "question": "What is the correct way to declare a function in Python?",
        "options": ["def function_name():", "function_name[]", "function function_name():", "declare function_name()"],
        "answer": "def function_name():"
    },
    {
        "question": "Which method is used to add an element at the end of a list in Python?",
        "options": ["append()", "insert()", "extend()", "add()"],
        "answer": "append()"
    },
    {
        "question": "What is the output of 'print(2 ** 3)' in Python?",
        "options": ["5", "6", "8", "Error"],
        "answer": "8"
    }
]

# Global variables
score = 0
q_index = 0

# Function to display the current question
def display_question(q_index):
    question_label.config(text=questions[q_index]["question"])
    for i, option in enumerate(questions[q_index]["options"]):
        answer_buttons[i].config(text=option, value=option)
    var.set(None)  # Reset the selected answer

# Function to check answer and give feedback
def check_answer():
    global score, q_index
    selected_answer = var.get()
    correct_answer = questions[q_index]["answer"]

    if selected_answer == correct_answer:
        score += 1
        messagebox.showinfo("Correct!", "Well done! Your answer is correct.", icon="info")
    else:
        messagebox.showerror("Incorrect", "Oops! That's not correct.", icon="error")

    q_index += 1
    if q_index < len(questions):
        display_question(q_index)
    else:
        messagebox.showinfo("Quiz Completed", f"Quiz over! You scored {score} out of {len(questions)}.", icon="info")
        root.quit()

# Create main window
root = tk.Tk()
root.title("VISHAL Python Programming= Quiz")
root.geometry("450x350")
root.configure(bg="#f0f8ff")  # Soft light blue background

# Define a custom font for the interface
custom_font = font.Font(family="Helvetica", size=12, weight="bold")

# Question label
question_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=400, bg="#f0f8ff", fg="#333333")
question_label.pack(pady=20)

# Variable to hold the selected answer
var = tk.StringVar()

# Answer buttons (Radio Buttons)
answer_buttons = []
for i in range(4):
    button = tk.Radiobutton(root, text="", font=custom_font, variable=var, value="", width=25, anchor="w", relief="raised", padx=20, pady=10)
    button.pack(pady=5)
    answer_buttons.append(button)

# Submit button
submit_button = tk.Button(root, text="Submit Answer", font=("Helvetica", 12), width=20, command=check_answer, bg="#351c75",  relief="flat", padx=10, pady=5)
submit_button.pack(pady=20)

# Function to style the buttons with colors
def style_buttons():
    colors = ["#007bff", "#ffc107", "#28a745", "#dc3545"]  # Blue, Yellow, Green, Red
    for i, button in enumerate(answer_buttons):
        button.config(bg=colors[i], activebackground=colors[i], relief="raised", font=("Helvetica", 12), width=25)

# Start the quiz
display_question(q_index)
style_buttons()

# Run the main event loop
root.mainloop()

