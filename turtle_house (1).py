import turtle 
from random import randint
turtle.speed(1)
turtle.colormode(255)

def draw_house(
        x=0,
        y=0,
        base_w=100,
        base_h=10,
        base_color="grey",
        walls_w=100,
        walls_h=100,
        walls_color="green",
        roof_w=120, 
        roof_h=110, 
        roof_color="yellow"
    ):
    draw_base(x, y, base_w, base_h, base_color)
    walls_y = y + base_h 
    draw_walls(x, walls_y, walls_w, walls_h, walls_color)
    roof_y = walls_y + walls_h
    draw_roof(x, roof_y, roof_w, roof_h, roof_color, walls_w)

def draw_base(x, y, base_w, base_h, base_color):
    print("Рисует фундамент")

    draw_rectangle(x, y, base_w, base_h, base_color)

def draw_walls(x, y, walls_w, walls_h, walls_color):
    draw_rectangle(x, y, walls_w, walls_h, walls_color)


def draw_roof(x, y, roof_w, roof_h, roof_color, walls_w,):
    turtle.fillcolor(roof_color)
    turtle.begin_fill()
    turtle.goto(x,  y)
    turtle.fd(walls_w // 2)
    turtle.fd(roof_w // 2)
    top_x = x + walls_w // 2
    top_y = y + roof_h
    turtle.goto(top_x, top_y)
    left_x = top_x - roof_w // 2
    turtle.goto(left_x, y)
    turtle.goto(x, y)
    turtle.end_fill()

def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.end_fill()


def draw_street(first_house_x=0, first_house_y=0, houses=10):
    counter = 0 
    while counter < houses:
        base_w=randint(50, 100)
        walls_w=randint(base_w - 50, base_w)
        roof_w=randint(walls_w, walls_w + 50),
        draw_house(
            x=first_house_x,
            y=first_house_y,
            base_h=randint(10,20),
            base_w=randint(50,100),
            base_color=(randint(0, 255), randint(0, 255), randint(0, 255)),
            walls_h=randint(10,20),
            walls_w=randint(50,100),
            walls_color=(randint(0, 255), randint(0, 255), randint(0, 255)),
            roof_w=roof_w,
            roof_h=roof_w,
            roof_color=(randint(0, 255), randint(0, 255), randint(0, 255)),
            )
        counter += 1
        first_house_x += roof_w // 2 + base_w

draw_street(-200, 0, 5)

turtle.done()

