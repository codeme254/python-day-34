THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # window
        self.window = Tk()
        self.window.title("Zaph Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # score
        self.score = Label(text=f"Score:")
        self.score.grid(column=1, row=0)
        self.score.config(font=("Verdana", 15, "normal"), bg=THEME_COLOR, fg="white", anchor=W)
        # canvs
        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="some text on the canvas", font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # the correct button
        self.correct_image = PhotoImage(file="./images/true.png")
        self.correct_button = Button(image=self.correct_image, command=self.true_pressed)
        self.correct_button.grid(column=0, row=2)
        # the false button
        self.false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_image, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text("You have reached the end of the quiz"))
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
