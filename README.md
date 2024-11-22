# Python_Quiz
python project Quiz of python Questions  ==>
### Features:
- **Python Programming Questions**: All the questions are based on Python programming concepts.
- **Colorful and Beautiful Interface**: Buttons have vibrant colors, and the layout is clean and engaging.
- **Instant Feedback**: The app provides immediate feedback about whether the user's answer is correct or incorrect.
- **Final Score**: At the end, the app shows the user's total score.
1. **Questions on Python Programming**:
    - The `questions` list contains dictionaries with:
        - `question`: The text of the question.
        - `options`: A list of four possible answers.
        - `answer`: The correct answer to the question.
        
        ![pyhton]( https://github.com/vis-hal95/Python_Quiz/blob/87086ac11657f5f7ad566c557e4d3691af108368/185bd697-126f-40eb-8a02-afe319705c46.jpeg)

2. **Main Window Setup**:
    - The window is set with a soft light blue background (`#f0f8ff`), making it visually appealing.
    - The window's size is set to `450x350`, which is sufficient to display the question and answer options without feeling crowded.
3. **Question Display**:
    - The question is shown in a **`Label`** widget, which is updated dynamically based on the current question in the quiz.
    - The `wraplength=400` ensures that the text wraps neatly within the window width if it's too long.
4. **Answer Buttons**:
    - Four **Radio Buttons** (`tk.Radiobutton`) are used to display the answer options. These buttons are created dynamically based on the options for each question.
    - The button colors are vibrant (blue, yellow, green, red) to make the interface more colorful and interactive.
5. **Feedback Mechanism**:
    - **Correct Answer**: When the user selects the correct answer, an information message box appears (`messagebox.showinfo`) to congratulate them.
       ![python](https://github.com/vis-hal95/Python_Quiz/blob/3d7b61ab9f345042ed80bbfa712b58e1e38899d5/8e79a058-83e0-4121-a15c-85bc88b564ab.jpeg)
    - **Incorrect Answer**: If the selected answer is wrong, an error message box appears (`messagebox.showerror`) to let the user know they chose the wrong answer.
      ![pyhton](https://github.com/vis-hal95/Python_Quiz/blob/66a6848665ea3c6826aa92acfcf820806c092b5e/e557b177-c443-467a-8f60-e920e6aa1932.jpeg)

    - **Final Score**: At the end of the quiz, a final score is displayed in a message box.
      ![pyhton](https://github.com/vis-hal95/Python_Quiz/blob/848083b947de970f62523237d1d57311b3058451/722ad67c-5301-4cd3-8628-95c8ffd396f0.jpeg)
6. **Submit Button**:
    - The **Submit Answer** button has a green background (`#28a745`) with white text. It triggers the `check_answer`function, which verifies if the answer is correct and moves to the next question.
8. **Styling**:
    - The `style_buttons()` function ensures that the answer buttons have distinct colors (blue, yellow, green, red), each representing one of the answer choices.
    - The `submit_button` has a flat style with rounded corners and padding to give it a modern appearance.
9. **Progression of the Quiz**:
    - After each answer submission, the `q_index` is incremented to move to the next question.
    - When all questions have been answered, the user's score is shown in a final popup.

### How the Application Works:

1. When the app starts, it displays the first Python-related question with four options.
2. The user selects an answer and clicks the **Submit Answer** button.
3. The app immediately shows feedback (correct or incorrect).
4. The quiz proceeds to the next question, and this process repeats until all questions are answered.
5. After the final question, the app displays the user's total score in a popup.

### Example of How It Looks:

- **Start Screen**: The first question appears with colorful answer options.
- **After Submitting Answer**: A popup shows whether the answer was **correct** or **incorrect**.
- **Final Score**: After answering all the questions, a message shows the total score.


