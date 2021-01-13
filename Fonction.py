import turtle
import math
t=turtle.Turtle()
t.speed(20000)
t.hideturtle()

def Fonction (a,b,c,d):
    tab=[]
    i=0
    x=a
    while a<=x<=b:
        z=x/5
        y=(((math.sin(z))/z)*50)+d
        tab.append((x,y))
        x+=c
    return tab

def Axe(L,l,couleur):
    t.color(couleur)
    t.forward(L)
    t.backward(2*L)
    t.forward(L)
    t.right(90)
    t.forward(l)
    t.backward(2*l)
    t.forward(l)
    t.left(90)
Axe(800,400,"Blue")

def traceur(a,couleur):
    t.color(couleur)
    for i in range(len(a)-1):
        if i==0 :
            t.penup()
        t.setx(10*(a[i][0]))
        t.sety(10*(a[i][1]))
        if i==0 :
            t.pendown()

traceur(Fonction(-80,80,0.1,-20),"red")
        