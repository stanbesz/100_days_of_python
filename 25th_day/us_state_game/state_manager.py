from turtle import Turtle

class State_Manager(Turtle):

    guessed_states_amount = 0
    guessed_states:set = set()

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.guessed_states_amount = 0

    def draw_state(self,name,pos_x,pos_y):
        self.goto(pos_x,pos_y)
        self.write(f"{name}")
        self.increase_count()
        
    def increase_count(self):
        self.guessed_states_amount+=1

    def add_guessed_state(self, state):
        self.guessed_states.add(state)

    
