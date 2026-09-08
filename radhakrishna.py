import turtle

t = turtle.Turtle()
t.speed(0)
t.width(3)

# Face (Krishna)
t.penup()
t.goto(0, -120)
t.pendown()
t.color("black", "#87CEEB")  # light blue face
t.begin_fill()
t.circle(120)
t.end_fill()

# Eyes
for x in [-40, 40]:
    t.penup()
    t.goto(x, 30)
    t.pendown()
    t.color("black", "white")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.penup()
    t.goto(x, 35)
    t.pendown()
    t.color("black")
    t.circle(5)

# Smile
t.penup()
t.goto(-40, -20)
t.setheading(-60)
t.pendown()
t.circle(60, 120)

# Crown
t.penup()
t.goto(-100, 120)
t.pendown()
t.color("gold")
t.begin_fill()
t.goto(0, 200)
t.goto(100, 120)
t.goto(-100, 120)
t.end_fill()

# Peacock feather
t.penup()
t.goto(0, 200)
t.pendown()
t.color("green")
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(0, 210)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(15)
t.end_fill()

# Flute
t.penup()
t.goto(-150, 0)
t.pendown()
t.color("brown")
t.width(5)
t.forward(300)

# Radha (simple side face)
t.penup()
t.goto(150, -80)
t.pendown()
t.color("black", "#FFC0CB")
t.begin_fill()
t.circle(80)
t.end_fill()

turtle.done()