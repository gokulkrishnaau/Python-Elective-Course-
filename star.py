import turtle

def draw_star(turtle, size, starcolor):
    angle = 144
    turtle.fillcolor(starcolor)
    turtle.begin_fill()

    turtle.pencolor(starcolor)

    for _ in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)

    turtle.end_fill()

def draw_n_stars(n, size, starcolor):
    angle = 360 / n
    distance = size * 5
    wn = turtle.Screen()
    wn.bgcolor("white")
    star_turtle = turtle.Turtle()
    star_turtle.speed(0)

    for _ in range(n):
        star_turtle.penup()
        star_turtle.forward(distance)
        star_turtle.pendown()
        draw_star(star_turtle, size, starcolor)
        star_turtle.penup()
        star_turtle.backward(distance)
        star_turtle.right(angle)

    turtle.done()

star_number = int(input("Enter the number of stars: "))
star_size = int(input("Enter the size of the stars: "))
star_color = input("Enter the name or hex code for color of the stars: ")
draw_n_stars(star_number, star_size, star_color)
