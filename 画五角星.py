import turtle

turtle.pensize(10)
#turtle.pencolor("yellow")
#turtle.fillcolor("red")

turtle.color("yellow","red")

turtle.begin_fill()
for i in range(5):
    turtle.forward(180)
    turtle.right(144)
    turtle.forward(180)
    turtle.left(72)
turtle.end_fill()

turtle.hideturtle()   #隐藏画笔
turtle.done()         #结束绘制
