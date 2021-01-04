import random

#globale Variablen - also solche, die jederzeit von jedem Teil des Programmes benutzt werden können


# definiere den Einstiegspunkt für das Programm
if __name__ == "__main__":
    main()

# definiere die Funktion, die den Ablauf des Programms bestimmt
def main():
  
  ###########
  # Schön wäre eine Aufteilung, wo jede eigene Funktionalität in einer eigenen Funktion steckt, also in etwa so: 
  ###########
  begruessung() # begruesse den Menschen
  name = wieheisstdu() # und erfrage seinen Namen
  if not name:
    quit()
  else:
    rest()
  #wohnort = wowohnstdu() # erfahre, wo der Mensch wohnt
    # ...
  ###########

  ####
  # Versuch doch mal das umgekehrte Zahlenspiel zu implementieren:
  # Der Mensch merkt sich eine Zahl zwischen 1 und 10 und der Computer hat beliebig viele Versuche, die Zahl zu raten.
  # Allerdings sollte er möglichst wenige Versuche brauchen.
  # Wie kannst der Computer die Aufgabe möglichst zielsicher lösen?
  ####

def begruessung():
  print(random.choice(["Hallo", "Guten Morgen", "Schön, dich zu sehen"]))

def wieheisstdu():
  #Begrüßung
  name = input("Wie heißt du?")

  #Überprüfen, ob was eingegeben wurde
  while not name:
    name = input("Schade, das habe ich nicht verstanden. Wenn du mit deinen Namen nicht verraten möchtest, dann tippe \"X\"")

  if name == "X":
    print("Schade, ich glaube, wir unterhalten uns ein anderes mal weiter. Bis bald.")
    return null

  print("Hallo, " + name)

  return name

def rest():
  #Wohnort
  wohnort = input("Wo wohnst du, " + name + "? ")
  print("Oh wie schön!")

  wohlfuehlen = input("Gefällt es dir dort?").lower() #Hier werden alle Buchstaben in Kleinbuchstaben umgewandelt

  if (wohlfuehlen == "ja"):
    print("Super")
  else:
    umzug = input("Schade, überlegst du umzuziehen?")
    if (umzug == "nein" or umzug == "Nein"):
      print("Ok")
    else:
      neuer_wohnort = input("Welchen Ort hast du im Kopf?")
      print(neuer_wohnort)
      print("Oh, dort ist es sicher schön.")

  #Wetter
  #def Wetter():

  #Gefühl
  happy = False

  liste_zustand = ["gut", "super", "toll"]

  zustand = input("Wie geht es dir heute?")
  zustand = zustand.lower()

  for gefuehl in liste_zustand:
    if gefuehl in zustand and not "nicht" in zustand:
      happy = True
  
  if happy == True:
    print("Schön")
  else:
    print("Schade")
    
  #Witz
  witz = input("Magst du einen Witz hören?").lower()
  
  #Gerade wenn man zwei Versionen von Code vergleicht, ist es einfacher, wenn die Zeilen nicht so lang sind
  witze = ["Treffen sich zwei Ballons. Fragt der eine den anderen, wie geht´s denn? Antwortet der andere, ah mir geht es nicht so gut, ich habe Platzangst.", 
		   "Der Lehrer fragt Fritzchen: Wenn du 5€ vor dir liegen hast, und ich dir 2€ davon wegnehme, was gibt das dann?Fritzchen: Prügel!", 
		   "Was ist der gefährliste Tag für ein Uboot ? -Tag der offen Tür."]

  if witz == "ja":
    print(random.choice(witze))
  else:
    print("Ok, hoffentlich geht es dir bald besser.")
  #Ratespiel

  zahlenraten = input("Hast du Lust auf ein Spiel? ")
  zahlenraten = zahlenraten.lower()
  if zahlenraten == "ja":
    print("Ok, dann geht es los.")
    zahlenraten()
  else:
    print("Schade")

def zahlenraten():
  raten = False
  zahl = random.randint(1,10)

  
  #Wie wäre es hier mit mehreren Versuchen :D
  count = 0
  print("Ich habe mir eine Zahl zwischen 1 und 10 ausgedacht. Nun bist du dran. Rate welche Zahl es sein könnte. "+
		"Du hast 3 Versuche.\n")
  while count<3:
      count +=1 

      versuch = int(input(count+". Versuch: \n"))

      if versuch == zahl:
        neues_spiel = input("Super! Du hast es erraten. Willst du nochmal spielen?").lower()
        if neues_spiel != "ja":
          break
        else:
          count = 0
      else:
        continue
      while raten == False:
        answer = int(input("Versuchs noch mal \n"))
        if answer == zahl:
          raten = True
  
    