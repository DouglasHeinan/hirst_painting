# import colorgram
import random
from turtle import Turtle, Screen


def main():
    # found necessary colors using colorgram
    # colors = colorgram.extract('hirst_image.jpg', 10000)
    # color_list = []
    # for count in range(len(colors)):
    #     cur_color = colors[count]
    #     rgb = cur_color.rgb
    #     rgb = (rgb[0], rgb[1], rgb[2])
    #     color_list.append(rgb)
    # print(color_list)

    # Draws a hirst-style painting

    usable_colors = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
                     (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
                     (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79),
                     (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159),
                     (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62),
                     (47, 66, 82), (115, 134, 139)]
    ralph = Turtle()
    screen = Screen()
    screen.colormode(255)
    ralph.speed(0)
    getting_started(ralph)
    for n in range(10):
        make_a_row(ralph, usable_colors)
        new_row(ralph)
    ralph.hideturtle()
    screen.exitonclick()


def getting_started(ralph):
    ralph.penup()
    ralph.forward(250)
    ralph.left(90)
    ralph.forward(250)
    ralph.left(180)


def make_a_row(ralph, usable_colors):
    for n in range(10):
        ralph.color(random.choice(usable_colors))
        ralph.begin_fill()
        ralph.circle(10)
        ralph.end_fill()
        ralph.forward(50)


def new_row(ralph):
    ralph.left(180)
    ralph.forward(500)
    ralph.left(90)
    ralph.forward(60)
    ralph.left(90)


if __name__ == "__main__":
    main()
