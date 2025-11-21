import turtle
import pandas
from state_manager import State_Manager

screen = turtle.Screen()
screen.title("U.S.A. States Game")
image = "25th_day/us_state_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_info = pandas.read_csv("25th_day/us_state_game/50_states.csv")
print(game_info)
state_list = game_info["state"].to_dict()
for key,value in state_list.items():
    value_lower = value.lower()
    state_list[key] = value_lower

invert_list = {value: key for key,value in state_list.items()}
print(state_list)
game_is_on = True

states_manager = State_Manager()
missing_states = []

while len(states_manager.guessed_states)<50:
    answer_state = screen.textinput(title=f"{states_manager.guessed_states_amount}/50 | Guess the state",prompt="State name: ")
    if isinstance(answer_state,str):
        answer_state_lower = answer_state.lower()
    else:
        pass

    country_ind = invert_list.get(answer_state_lower)
    print(country_ind)

    if answer_state == "exit":
        missing_states = [state for state in state_list.values() if state not in states_manager.guessed_states]
        # for state in state_list.values():
        #     state = state.title()
        #     if state not in states_manager.guessed_states:
        #         missing_states.append(state.title())
                

        #     else:
        #         pass
        break

    if country_ind is not None:
        x_pos = game_info.iloc[country_ind]["x"]
        y_pos = game_info.iloc[country_ind]["y"]

        states_manager.draw_state(game_info.iloc[country_ind].state,x_pos,y_pos)
        states_manager.add_guessed_state(game_info.iloc[country_ind].state)
    else:
        pass


states_to_learn_df = pandas.DataFrame(missing_states)
states_to_learn_df.to_csv("25th_day/us_state_game/states_to_learn.csv")


turtle.mainloop()
