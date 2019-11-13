import turtle
bob=turtle.Turtle()
bob.speed(0)
turtle.bgcolor("skyblue")

bob.begin_fill()
bob.color("red")
bob.goto(-100,0)
for times in range(5):
        bob.forward(500)
        bob.right(144)
bob.end_fill()
bob.forward(500)

bob.begin_fill()
bob.color("orange")
bob.penup()
bob.goto(-50,-15)
for times in range(5):
        bob.forward(400)
        bob.right(144)
bob.end_fill()
bob.forward(400)
bob.pendown()

bob.begin_fill()
bob.color("yellow")
bob.penup()
bob.goto(-0,-30)
for times in range(5):
        bob.forward(300)
        bob.right(144)
bob.end_fill()
bob.forward(300)
bob.pendown()

bob.begin_fill()
bob.color("green")
bob.penup()
bob.goto(50,-45)
for times in range(5):
        bob.forward(200)
        bob.right(144)
bob.end_fill()
bob.forward(200)
bob.pendown()

bob.begin_fill()
bob.color("blue")
bob.penup()
bob.goto(100,-60)
for times in range(5):
        bob.forward(100)
        bob.right(144)
bob.end_fill()
bob.forward(100)
bob.pendown()

bob.begin_fill()
bob.color("purple")
bob.penup()
bob.goto(125,-70)
for times in range(5):
        bob.forward(50)
        bob.right(144)
bob.end_fill()
bob.forward(50)
bob.penup()
