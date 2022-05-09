import turtle
import pandas

screen = turtle.Screen()
screen.setup(725, 491)
screen.title("U.S.A States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed = []

while len(guessed) < 50:
    answer_state = screen.textinput(title=f"{len(guessed)}/50 States Correct",
                                    prompt="What's another state name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed:
                missing_states.append(state)
        # Create a CSV file of all the states to learn
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # item() get the first data
        t.write(state_data.state.item())


##########################################################
# # How to get the x and y coordinate of the mouse click
# def get_mouse_click_coordination(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordination)
#
# turtle.mainloop()
###########################################################
