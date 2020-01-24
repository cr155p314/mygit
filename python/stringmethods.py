course = "Python Programming"
print(course.upper())  # alles groß
print(course.lower())  # alles klein
print(course.title())  # erster Buchstabe jedes Wortes groß

print(course.strip())  # entfernt alle leerzeichen

print(course.find("Pro"))  # bestimmte buchstaben finden
print(course.replace("P", "-"))  # ersetze Buchstaben

print("Programming" in course)  # wort vorhanden ja/nein
print("Programming" not in course)  # wort vorhanden ja/nein
