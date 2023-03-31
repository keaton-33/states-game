from turtle import Turtle


class Text:
    def __init__(self):
        self.__init_writer()

    def __init_writer(self):
        self.__writer = Turtle()
        self.__writer.hideturtle()
        self.__writer.penup()
        self.__writer.speed(0)
        self.__writer.color("black")

    def write_text(self, name, position):
        self.__writer.goto(position)
        self.__writer.write(arg=str(name), align="center", font=("Impact", 12, 'normal'))