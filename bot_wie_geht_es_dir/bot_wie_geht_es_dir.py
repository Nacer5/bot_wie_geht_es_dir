import random

greetings = ["Hallo", "Guten Morgen", "Schön, dich zu sehen"]

print(random.choice(greetings))

#Begrüßung
name = input("Wie heißt du?")
print("Hallo, " + name)

#Wohnort
wohnort = input("Wo wohnst du, " + name + "? ")
print("Oh wie schön!")

wohlfuehlen = input("Gefällt es dir dort?")

if (wohlfuehlen == "ja" or wohlfuehlen == "Ja"):
  print("Super")
else:
  umzug = input("Schade, überlegst du umzuziehen?")
  if (umzug == "nein" or umzug == "Nein"):
    print("Ok")
  else:
    neuer_wohnort = input("Welchen Ort hast du im Kopf?")
    print(neuer_wohnort)
    print ("Oh, dort ist es sicher schön.")
#Wetter
#def Wetter():

#Gefühl
happy = False

liste_zustand = ["gut", "super", "toll"]

zustand = input("Wie geht es dir heute?")
zustand = zustand.lower()

for gefuehl in liste_zustand:
  if gefuehl in zustand:
    happy = True
    if "nicht" in zustand:
      happy = False
  
if happy == True:
  print("Schön")
else:
  print("Schade")
  #Witz
  witz = input("Magst du einen Witz hören?")
witze = ["Treffen sich zwei Ballons. Fragt der eine den anderen, wie geht´s denn? Antwortet der andere, ah mir geht es nicht so gut, ich habe Platzangst.", "Der Lehrer fragt Fritzchen: Wenn du 5€ vor dir liegen hast, und ich dir 2€ davon wegnehme, was gibt das dann?Fritzchen: Prügel!", "Was ist der gefährliste Tag für ein Uboot ? -Tag der offen Tür."]
if witz == "Ja" or witz == "ja":
  print(random.choice(witze))
else:
  print("Ok, hoffentlich geht es dir bald besser.")
#Ratespiel

import random 

raten = False

zahl = random.randint(1,10)
print(zahl)

zahlenraten = input("Hast du Lust auf ein Spiel? ")
zahlenraten = zahlenraten.lower()
if zahlenraten == "ja":
  print("Ok, dann geht es los.")
else:
  print("Schade")

versuch = int(input("Ich habe mir eine Zahl zwischen 1 und 10 ausgedacht. Nun bist du dran. Rate welche Zahl es sein könnte.\n"))

if versuch == zahl:
  print("erraten")
else:
  print("nicht erraten")
while raten == False:
  answer = int(input("Versuchs noch mal \n"))
  if answer == zahl:
    raten = True
    neues_spiel = ("Super! Du hast es erraten. Willst du nochmal spielen?")
    neues_spiel = neues_spiel.lower()
    print(neues_spiel)
    if neues_spiel == "ja":
      print("Bye")
