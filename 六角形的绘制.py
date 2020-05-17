import turtle

def draw(len):
    turtle.left(30)
    turtle.fd(len)

    for i in range(5):
        turtle.right(60)
        turtle.fd(len)

    turtle.fd(len)
    turtle.right(120)
    turtle.fd(len)

    for i in range(5):
        turtle.left(60)
        turtle.fd(len)
        turtle.right(120)
        turtle.fd(len)

draw(120)
