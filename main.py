import requests

ville= input("donner le nom de la ville: ")
print("voici la ville que vous avez donner:",ville)
#je cree un compte openweathermap et je reccupere ma cle qui est la suivante:
#cette cle me permet d'acceder a api pour reccuperer les information.
cle="70ea5d4a47abb6f1460d5ed6db7dacb8"
#je construis un url avec ma ville et ma cle 
url=f"https://api.openweathermap.org/data/2.5/weather?q={ville}&appid={cle}&units=metric&lang=fr"
#je reccupere les information et les affiche
resultat= requests.get(url)
#pour reccuperer les informations de la temperature,humidite.....
information= resultat.json()
temperature=information["main"]["temp"]
humidity=information["main"]["humidity"]
description=information["weather"][0]["description"]
ma_ville=information["name"]

print(f"La meteo a {ma_ville} :")
print(f"Temperature : {temperature}^C")
print(f"L'humidite: {humidity}%")
print(f"Les conditions climatiques: {description}")