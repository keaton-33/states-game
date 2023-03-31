import turtle


class Screen:
    def __init__(self, image):
        self.__init_screen(image)

    def text_input(self, title, prompt):
        return self.__screen.textinput(title=title, prompt=prompt)

    def __init_screen(self, image):
        self.__screen = turtle.Screen()
        self.__screen.title("US States Game")
        self.__screen.addshape(image)
        turtle.shape(image)

    def start_screen(self):
        turtle.mainloop()
