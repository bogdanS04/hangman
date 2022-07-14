from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.configure(pady=30, padx=30, bg=THEME_COLOR)
        self.window.title("Quizzler")
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="question text", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def change_score_label(self):
        self.score_label.configure(text=f"Score: {self.score}")

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
        else:
            self.canvas.itemconfigure(self.question_text, text="You've reached the end!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def white_bg(self):
        self.get_next_question()
        self.canvas.configure(bg="white")
        self.change_score_label()
    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.score += 1
            self.canvas.configure(bg='green')
            self.window.after(1000, self.white_bg)
        else:
            self.canvas.configure(bg='red')
            self.window.after(1000, self.white_bg)
