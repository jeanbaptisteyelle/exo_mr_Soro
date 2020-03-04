
# JOYEUX ANNNIVERSAIRE MONSIEUR
#  Que DIEU vous apporte la force,le courage et la sante pour accomplir vos rêves

def gestion_horaire(prix,heure):
     if heure <=39:
          return 0
     elif heure < 45: 
          return (heure - 39)*(prix*1.5)
     elif heure < 50:
          return (5*prix*1.5) + (heure - 44)*(prix*1.75)

     else:
          return (5*prix*1.5) + 5*(prix*1.75) + (heure - 49)*(prix*2)

n = int(input("saisir nombre d'heures:"))
x = float(input("saisir prix d'heurs:"))
print("le montant de votre heure suplementaire est:", gestion_horaire(x,n), "£")



          

