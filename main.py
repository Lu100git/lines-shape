import turtle
pen = turtle.Turtle()
pen.speed(0)

def trngl():
    for i in range(3):
        pen.pendown()
        pen.forward(740)
        pen.right(120)
        pen.penup()

def sqr():
    pen.penup()
    for i in range(4):
        pen.pendown()
        pen.forward(600)
        pen.right(90)
        pen.penup()

# make a black square
pen.penup()
pen.color("black")
pen.goto(-900,600)
pen.begin_fill()
for i in range(4):
    pen.pendown()
    pen.forward(2000)
    pen.right(90)
    pen.penup()
pen.end_fill()

pen.speed(10)

# blue square
pen.penup()
pen.goto(-300, 300)
pen.color("white")
sqr()

# X
pen.color("red")
pen.right(45)
pen.pendown()
pen.forward(848)
pen.right(315)
pen.penup()

# magenta square
pen.goto(0, 400)
pen.right(45)
pen.color("magenta")
sqr()


# green triangle
pen.color("green")
pen.right(15)
trngl()

pen.color("red")
pen.pendown()
pen.right(30)
pen.forward(848)


pen.color("green")
pen.right(150)
trngl()

# +
pen.color("red")
pen.left(15)
pen.forward(602)
pen.pendown()
pen.right(135)
pen.forward(848)

# rombus
pen.color("yellow")
pen.right(153)
pen.forward(473)

pen.right(54)
pen.forward(476)

pen.right(126)
pen.forward(476)

pen.right(54)
pen.forward(476)

pen.right(128)
pen.penup()
pen.goto(250,-20)

pen.pendown()
pen.forward(284)
pen.right(52)
pen.forward(284)
pen.right(130)
pen.forward(284)
pen.right(52)
pen.forward(284)

# X
pen.color("red")


pen.penup()
pen.goto(300, 300)
pen.right(106)
pen.pendown()
pen.forward(848)

input("press enter to continue...")
