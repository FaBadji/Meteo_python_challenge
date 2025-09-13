import requests

#nom= input("quel est votre nom ? ")
#age=input("quel est votre age ? ")
#print("Mon nom c'est " + nom  +" ,et j'ai " + age + "ans" )

"""nom= input("quel est votre nom ? ")
prochain=0
while prochain==0:
   age=input("quel est votre age ? ")
   try:
      prochain = int(age)+1
   except: 
      print("erreur de code")
   else:       
      print("Mon nom est " + nom + " j'ai " + age + " ans et l'annee prochaine j'aurais "+ str(prochain) +" ans")
=========================================================    
mdp = ""
while not mdp == "fatou":
   mdp =input("quel est votre mot de passe ? ")
print("mot de passe correct ")  
def demande_nom():
  reponse=""
  while reponse == "":
    reponse= input("quel est votre nom ? ")
    try:
       n=reponse
    except: 
        print("vous avez pas mis le bon nom") 
    else:
        return n      
nom = demande_nom()
print(nom)  

===================================================
def afficher_information(no,ag ):
  while no == "":
    no= input("quel est votre nom ? ")
    
  while ag == 0:
    ag=input("quel est votre age ? ")
    
  print("vous vous appeler " + no + " et vous avez " + ag + " ans")   
  
n = ""
a=0 
afficher_information(n,a)
===================================================
for i in range(0, 4):
  print(i)  
=====================================================  
angle=input("donner un angle en degre: ")
angle = float(angle)
radian= angle *(3.14/180)
print("votre angle est de " + str(radian) +" radian ")
===================================================
angle=input("donner un angle en radian: ")
angle = float(angle)
degre= (angle*180)/3.14
print("votre angle est de " + str(degre) +" degre ")
=======================================
prenom= "fatou"
nom = "Badji"
age = 24 

result = f"je m'appelle {prenom} {nom} et j'ai {age} ans "
print(result)
===================================
nb1=input("entrer un nombre: ")
nb2=input("entrer un autre nombre: ")
nb1= float(nb1)
nb2=float(nb2)
print("Addition ",nb1 + nb2)
print("Soustraction ",nb1 - nb2)
print("Division ",nb1/nb2)
print("Modulo ",nb1 % nb2)
print("Multiplication", nb1*nb2)
======================================

nombre= int(input("donner un nombre: "))

if nombre % 2 == 0:
   print(f"{nombre} est paire ")
else:
   print(f"{nombre} est impaire ")

#un exercice en utiliant les api ,url...Pour cette exercice je vais creer un script python qui permet de telecharger
# une video dans youtube et le mettre dans mon pc




#reccuperer un fait aleatoir sur le chats
url= f"https://catfact.ninja/fact"

reponse= requests.get(url)
print(reponse.json())



#reccuperer un nombre aleatoir
url=f"https://www.randomnumberapi.com/api/v1.0/random"
reponse=requests.get(url)
print(reponse.json())

#deviver un prenom
prenom=input("donner un prenom:")
url=f"https://api.agify.io?name=Fatou"
reponse=requests.get(url)
#print(reponse.json())
resultat=reponse.json()
if resultat["name"]==prenom:
   print("Bravo vous avez devine le nom!!",prenom)
else:
   print("Vous avez pas trouve le bon nom! ")"""
   
   
#reccuperer les informations d'un pays via un code pays comme FR,US,SN
code=input("donner un code d'un pays sous ce format FR,US... :")
url=f"https://restcountries.com/v3.1/alpha/{code}"
resultat =requests.get(url)
#print(resultat.json())
R=resultat.json()
Name=R[0]["name"]["official"]
Capital=R[0]["capital"][0]
Population=R[0]["population"]

print("les informations sur le code de pays ",code)
print("Le nom officiel du pays c'est ",Name)
print("La capital est ",Capital)
print("La population est de ",Population)
   

     




        