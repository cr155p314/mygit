print("Tag des Datums eingeben:")
tag = int(input())
print("Monat des Datums eingeben:")
monat = int(input())
print("Jahr des Datums eingeben:")
jahr = int(input())

#Berechnung
if tag < 1 or tag > 31:
    print("Falsches Datum")
elif monat < 1 or monat > 12:
    print("Falsches Datum")
elif monat == 4 or monat == 6 or monat == 9 or monat == 11:
    print ("letzter Tag: 30")
    if tag < 1 or tag > 31:
        print("falsches Datum")
    else:
        print("richtiges Datum")
elif monat == 2:
    if jahr%4 == 0 and jahr%100 != 0 or jahr%400 == 0:
        print("letzter Tag: 29")
        if tag < 1 or tag > 29:
            print("falsches Datum")
        else:
            print("Richtiges Datum")
    else:
        print("letzter Tag: 28")
        if tag < 1 or tag > 28:
            print("falsches Datum")
        else:
            print("richtiges Datum")
else:
    print("letzter Tag: 31")
    if tag < 1 or tag > 31:
        print("falsches Datum")
    else:
        print("richtiges Datum")
