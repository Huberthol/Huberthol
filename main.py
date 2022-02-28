import turtle
import pandas

screen = turtle.Screen()
screen.title("Województwa_Quiz")
image = "woj_pl.img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_coor(x, y):missing_woj
#     print(x, y)
# screen = turtle.Screen()
# turtle.onscreenclick(get_coor)
# screen.mainloop()

data = pandas.read_csv("16_woj_pl.csv")
all_woj = data.woj.to_list()
guessed_woj = []

while len(guessed_woj) < 16:
    answer_woj = screen.textinput(title=f"{len(guessed_woj)}/16 Odgadnięte Województwa",
                                  prompt="Jakie jest kolejne województwo?").title()
    if answer_woj == "Exit":
        missing_woj = []
        for woj in all_woj:
            if woj not in guessed_woj:
                missing_woj.append(woj)
        new_data = pandas.DataFrame(missing_woj)
        new_data.to_csv("wojewodztwa_do_nauki.csv")
        break
    if answer_woj in all_woj:
        guessed_woj.append(answer_woj)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        woj_data = data[data.woj == answer_woj]
        t.goto(int(woj_data.x), int(woj_data.y))
        t.write(answer_woj)

screen.exitonclick()