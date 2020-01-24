name = " "
if not name.strip():
    print("Name is empty")

age = 22
if 18 <= age < 65:
    print("Eligible")

# 18 <= age <65 #vereinfachte mathematische schreibweise statt z. B. if 18 <= and <65

age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "not Eligible"

message = "Eligible" if age >= 18 else "Not eligbile"  # vereinfachter operator

print(message)
