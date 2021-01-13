#Importation des modules
import turtle                                                                                  #LE PROGRAMME AFFICHE SOIT DES CERCLES SOIT DES LIGNES SOIT DES PENTAGRAMMES EN ROND(DANS
import math                                                                                    #LE STYLE DU DRAPEAU EUROPEEN.
#Création de l'objet plus ça mise au centre                                                    #TOUT LES PARAMETRES SONT PLUS BAS
t=turtle.Turtle()
window=turtle.Screen()
window.bgcolor("black")
t.hideturtle()
t.speed("fastest")
t.penup()
t.setx(0)
t.sety(0)
t.pendown()
#Création des différents méthodes possibles(Cercle,ligne,pentagramme)
#Cercle
def cercle(rayon,extension,nombre_rond):
    z=0
    for i in ["magenta","red","orange","yellow","light green","turquoise","blue","black"] :
        t.color(i)
        t.penup()
        t.right(90)
        t.forward(rayon)
        t.left(90)
        t.pendown()
        t.circle(rayon)
        t.penup()
        t.left(90)
        t.forward(rayon)
        t.right(90)
        t.pendown()
        rayon=rayon+extension
        z=z+1
        if z==nombre_rond :
            break
#Ligne
def ligne(longueur,couleur) :
    t.color(couleur)
    t.forward(longueur/2)
    t.backward(longueur)
    t.forward(longueur/2)
    
#pentagramme
def pentagramme(rayon,couleur):
    t.color(couleur)
    t.penup()
    t.right(198)
    t.forward(rayon)
    t.right(162)
    t.pendown()
    t.begin_fill()
    for y in range(5) :
        t.forward(2*rayon*math.cos(math.radians(18)))
        t.right(144)
    t.left(162)
    t.penup()
    t.backward(rayon)
    t.pendown()
    t.left(198)
    t.end_fill()

#Programme
Nombre_objet=50                                            #NOMBRE D OBJET= NOMBRE OBJET EN CERCLE
rayon=200                                                 #RAYON = DISTANCE DE CES OBJETS PAR RAPPORT AU CENTRE
for i in range(Nombre_objet):
    t.penup()
    t.right(360/Nombre_objet)
    t.forward(rayon)
    t.pendown()
    t.setheading(0)
                                                            #DESACTIVER LE HASHTAG(PETIT CARRE) POUR CHOISIR LA FONCTION CERCLE,LIGNE OU PENTAGRAMME
    cercle(10,50,8)                                         #PARAMETRE CERCLE(RAYON 1ER CERCLE,EXTENSION POUR LES AUTRES CERCLES,NOMBRE DE CERCLE                                
    #ligne(20,"red")                                       #PARAMETRE LIGNE(LONGUEUR, COULEUR)
    #pentagramme(20,"magenta")                              #PARAMETRE PENTAGRAMME(RAYON PENTAGRAMME,COULEUR)
    
    t.right(i*360/Nombre_objet)
    t.penup()
    t.backward(rayon)
    t.pendown()                                              #PS : LE CERCLE PREND GENERALEMENT DU TEMP A CHARGER(EN FCT. DES PARAMETRE) MAIS ON EN FAIT GENERALEMENT DES CHOSES TRES JOLI
        
    
turtle.mainloop()
