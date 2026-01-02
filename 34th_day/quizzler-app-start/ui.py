from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        
        self.score = 0
        self.score_label = Label(text=f"Score: {self.quiz.score}",fg="white",bg=THEME_COLOR,highlightthickness=0)
        self.score_label.grid(row=0,column=1)
        
        self.canvas = Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,text=f"Question:Example",font=("Arial",20,"italic"),width=280,fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        
        self.image_correct = PhotoImage(file="34th_day\quizzler-app-start\images\\true.png")
        self.button_correct = Button(command=self.check_correct,image=self.image_correct,padx=20,pady=20,highlightthickness=0)
        self.image_false = PhotoImage(file="34th_day\quizzler-app-start\images\\false.png")
        self.button_false = Button(command=self.check_false,image=self.image_false,padx=20,pady=20,highlightthickness=0)
        self.button_correct.grid(row=2,column=0)
        self.button_false.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()
        pass

    def check_correct(self):
        is_right = self.quiz.check_answer(True)
        self.give_feedback(is_right)
        return True
    
    def check_false(self):
        is_right = self.quiz.check_answer(False)
        self.give_feedback(is_right)
        return False

    def change_bg(self,is_right):
        if is_right:
            self.score+=1
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text,fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text,fill="white")

    def give_feedback(self,is_right):
        self.change_bg(is_right)
    
        self.window.after(1000,self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,fill=THEME_COLOR)
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the questions!")
            self.button_correct.config(state="disabled")
            self.button_false.config(state="disabled")