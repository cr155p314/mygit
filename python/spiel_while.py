#Zufallsgenerator
import random
random.seed()

#Werte und Berechnung
a = random.randint(1, 10)
b = random.randint(1, 10)
c = a + b
print("Die Aufgabe:", a, "+", b)

#Schleife initialisieren
zahl = c + 1
#Ausgabe: Anzahl Initialisieren
versuch = 0

#solange das Ergebnis nicht c ist"
while zahl != c:
    versuch = versuch + 1

#Eingabe samt Umwandlung
print("Bitte eine Zahl eingeben")
z = input()
zahl = int(z)

#Verzweigung mit if-else
if zahl == c:
    print(zahl, "ist richtig")
else:
    print(zahl, "ist falsch")

#Anzahl und Ergebnis ausgeben
print("Ergebnis: ", c)
print("Anzahl Versuche:", versuch)
