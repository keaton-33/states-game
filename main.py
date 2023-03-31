import turtle
import pandas
from text import Text

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# def write_state(correct_answer):

text = Text()

data = pandas.read_csv('50_states.csv')

game_on = True
while game_on:
    answer = screen.textinput(title=f"{50 - len(data)}/50 States Correct", prompt="What's another state's name?")
    answer = answer.title()
    if answer == 'Exit':
        game_on = False
        break
    for state in data['state']:
        if state == answer:
            x = int(data.loc[data['state'] == answer]['x'])
            y = int(data.loc[data['state'] == answer]['y'])
            data = data.loc[data['state'] != answer]
            text.write_text(answer, (x, y))
            if len(data) == 0:
                game_on = False

if len(data) > 0:
    print(data)
    data.to_csv('missed_states.csv')

# turtle.mainloop()
