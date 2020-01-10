#Eingabe
print("Bitte geben Sie Ihr gehalt ein")
gehalt = float(input())

#Berechnung
if gehalt >= 4000:
    steuerbetrag = gehalt * 0.26
elif gehalt <= 2500:
    steuerbetrag = gehalt * 0.18
else:
    steuerbetrag = gehalt * 0.22

print("Es ergibt sich eine Steuer von:", steuerbetrag, "Euro")
