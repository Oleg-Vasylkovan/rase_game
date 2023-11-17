from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")


color = ["blue", "red", "green", "purple", "yellow", "brown"]
y_position = [-70, - 40, - 10, 20, 50, 80]
all_turtle = []

is_race_on = False
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    new_turtle.color(color[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winnig_color = turtle.pencolor()
            if winnig_color == user_bet:
                print("You WON!!!")
            else:
                print(f"You LOST. Winner color is {winnig_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()