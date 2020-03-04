def permis(ple, ch, vh, am):
    retr = ple + 3*ch + 5*vh + 10*am
    return (retr*200)/100

#victime
p = int(input("saisir le nombre de poule tué par le chasseur:"))
c = int(input("saisir le nombre de chien tué par le chasseur:"))
v = int(input("saisir le nombre de vache tué par le chasseur:"))
a = int(input("saisir le nombre d'ami tué par le chasseur:"))

d = permis(p,c,v,a)

if d == 0:
    print("vous avez aucun dû")
else:
    print("vous avez un dû de: ", d, "£uro")
