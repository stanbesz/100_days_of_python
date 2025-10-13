import another_module
import turtle
# from turtle import Timmy
print(f"another_module.another_variable: {another_module.another_variable}")

# turtle_draw = turtle.Turtle()
# turtle_draw.shape("turtle")
# turtle_draw.color("green")
# turtle_draw.forward(100)

# print(turtle_draw)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.align = "l"
table.field_names = ["Pokemon Name","Type"]
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmander","Fire"])

print(table.align)
print(table)