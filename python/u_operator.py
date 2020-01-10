#Eingabe
print("Bitte geben Sie ihr Gehalt ein")
gehalt = float(input())
print("bitte geben Sie Ihren Familienstand ein"
    + " (1=ledig, 2=verheiratet):")
familienstand = int(input())

#Berechnung
if gehalt > 4000 and familienstand == 1:
    steuerbetrag = gehalt * 0.26
elif gehalt <= 4000 and familienstand == 2:
    steuerbetrag = gehalt *0.18
else:
    steuerbetrag = gehalt * 0.22

print("Es ergibt sich eine Steuer von:", steuerbetrag, "Euro")
