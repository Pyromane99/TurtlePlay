import turtle

#background
def background():
    window=turtle.Screen()
    window.bgcolor("black")
    
#Grille blanche
def grille():
    grille=turtle.Turtle()
    grille.color("white")
    grille.speed("fastest")
    grille.hideturtle()
    grille.pensize(5)
    x=[-100,100,-300,-300]
    y=[300,300,100,-100]
    b=0
    for a in range(4):
        b=b+1
        grille.penup()
        grille.setx(x[a])
        grille.sety(y[a])
        grille.pendown()
        if b<=2 :
            grille.right(90)
        grille.forward(600)
        grille.setheading(0)

#Faire une croix
def croix(x,y):
    croix=turtle.Turtle()
    croix.color("red")
    croix.speed("fastest")
    croix.hideturtle()
    croix.pensize(5)
    croix.penup()
    croix.setx(x)
    croix.sety(y)
    croix.pendown()
    croix.right(45)
    for a in range(4):
        croix.forward(70)
        croix.backward(70)
        croix.right(90)
    
#Faire un cercle
def cercle(x,y):
    cercle=turtle.Turtle()
    cercle.color("green")
    cercle.speed("fastest")
    cercle.hideturtle()
    cercle.pensize(5)
    cercle.penup()
    cercle.setx(x)
    cercle.sety(y-70)
    cercle.pendown()
    cercle.circle(70)

#Programme principale( Emplacement des symboles et appel de leur fonction, création de la matrice des valeurs)
def game(x,y):
    global a
    global b
    xbis=0
    ybis=0
    a=a+1
    if a%2==0:
        if -300<x and x < -100:
            xbis=-200
            if 100<y and y<300:
                ybis=200
                b[0][0]=1
            if -100<y and y<100:
                ybis=0
                b[1][0]=1
            if -300<y and y< -100:
                ybis=-200
                b[2][0]=1
        if -100<x and x<100:
            xbis=0
            if 100<y and y<300:
                ybis=200
                b[0][1]=1
            if -100<y and y<100:
                ybis=0
                b[1][1]=1
            if -300<y and y< -100:
                ybis=-200
                b[2][1]=1
        if 100<x and x<300:
            xbis=200
            if 100<y and y<300:
                ybis=200
                b[0][2]=1
            if -100<y and y<100:
                ybis=0
                b[1][2]=1
            if -300<y and y< -100:
                ybis=-200
                b[2][2]=1
        croix(xbis,ybis)
    else:
        if -300<x and x < -100:
            xbis=-200
            if 100<y and y<300:
                ybis=200
                b[0][0]=2
            if -100<y and y<100:
                ybis=0
                b[1][0]=2
            if -300<y and y< -100:
                ybis=-200
                b[2][0]=2
        if -100<x and x<100:
            xbis=0
            if 100<y and y<300:
                ybis=200
                b[0][1]=2
            if -100<y and y<100:
                ybis=0
                b[1][1]=2
            if -300<y and y< -100:
                ybis=-200
                b[2][1]=2
        if 100<x and x<300:
            xbis=200
            if 100<y and y<300:
                ybis=200
                b[0][2]=2
            if -100<y and y<100:
                ybis=0
                b[1][2]=2
            if -300<y and y< -100:
                ybis=-200
                b[2][2]=2
        cercle(xbis,ybis)
    if Victoire(b)==1:
        print("Victoire au rouge")
    if Victoire(b)==2:
        print("Victoire au vert")
        
#Fonction qui détermine la victoire
def Victoire(c):
    for a in [1,2]:
        for b1 in [0,1,2]:
            for b2 in [0,1,2]:
                for b3 in [0,1,2]:
                    for b4 in [0,1,2]:
                        for b5 in [0,1,2]:
                            for b6 in [0,1,2]:
                                if c==[[a,b1,b2],[a,b3,b4],[a,b5,b6]] or c==[[b1,a,b2],[b3,a,b4],[b5,a,b6]] or c==[[b1,b2,a],[b3,b4,a],[b5,b6,a]] or c==[[a,a,a],[b1,b2,b3],[b4,b5,b6]] or c==[[b1,b2,b3],[a,a,a],[b4,b5,b6]] or  c==[[b1,b2,b3],[b4,b5,b6],[a,a,a]] or c==[[a,b1,b2],[b3,a,b4],[b5,b6,a]] or c==[[b1,b2,a],[b3,a,b4],[a,b5,b6]]:
                                    return a

#Variable global a (Utile pour l'alternance des symboles) et b (la matrice des résultats)
a=0
b=[[0,0,0],[0,0,0],[0,0,0]]

#Appel des fonctions
background()
grille()

#Appel de la fonction principale à chaque fois que on touche l'écran
turtle.onscreenclick(game)
turtle.mainloop()
