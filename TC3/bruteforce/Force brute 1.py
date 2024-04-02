# Créé par Magnesium, le 23/04/2021 en Python 3.7
#Import des modules nécessaires
import mechanize
import sys

#Accède à la page de connexion
br = mechanize.Browser()
br.set_handle_robots(False)
response = br.open("http://10.20.32.61/")

fd = open(sys.argv[1])
listepass=fd.readlines()


for form in br.forms():
  print(form)


