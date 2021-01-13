import turtle

t=turtle.Turtle()
t.color("blue")
t.speed("slowest")
t.shape("turtle")
ts=t.getscreen()
t.begin_fill()
def right():
    t.right(20)
def left():
    t.left(20)
while True:
    t.forward(1)
    ts.onkeypress(right,"d")
    ts.onkeypress(left,"q")
    ts.listen()
    t.end_fill()

