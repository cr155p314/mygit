message = "a"


def greet():
    global message  # zeigt python, dass wir nicht das erste message printen sondern die funktion mit einbeziehen
    # vermeiden, keine guter Code damit
    message = "b"


greet()
print(message)
