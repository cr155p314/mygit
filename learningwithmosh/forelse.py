# names = ["AJohn", "Mary"]
# found = False
# for name in names:
#     if name.startswith("J"):          Komplizierter Weg!
#         print("Found")
#         found = True
#         break
# if not found:
#     print("Not found")

# definiert "names" als Liste mit den Namen John und Mary
names = ["John", "Mary"]
for name in names:  # for schleife in name
    if name.startswith("J"):  # wenn der name mit J beginnt
        print("Found")  # drucke "found"
        break  # beende for schleife

    else:  # trifft obiges nicht zu
        print("Not found")  # drucke "Not found"
