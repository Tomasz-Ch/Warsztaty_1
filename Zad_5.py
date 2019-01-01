# Warsztat: Kostka do gry
#
# W grach planszowych i papierowych RPG używa się wielu rodzajów kostek do gry, nie tylko tych dobrze znanych, sześciennych. Jedną z popularniejszych kości jest np. kostka dziesięciościenna, a nawet stuścienna! Jako że w grach kośćmi rzuca się często, pisanie za każdym razem np. "rzuć dwiema kostkami dziesięciościennymi, a do wyniku dodaj 20" byłoby nudne, trudne i marnowałoby ogromne ilości papieru. W takich sytuacjach używa się kodu "rzuć 2D10+20".
#
# Kod takiej kostki wygląda następująco:
#
# xDy+z
#
# gdzie:
#
# y – rodzaj kostek, których należy użyć (np. D6, D10),
# x – liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny,
# z – liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie).

from random import randint


def game(description):
    splitted = description.split("D")
    if splitted[0] == "":
        x = 1
    else:
        x = int(splitted[0])

    y_z = splitted[1]
    # print(y_z) -> "20+10"  "20-100"  "30"
    if "-" in y_z:
        v = y_z.split("-")
        y = int(v[0])
        z = int(v[1]) * (-1)
    elif "+" in y_z:
        v = y_z.split("+")
        y = int(v[0])
        z = int(v[1])
    else:
        y = int(y_z)
        z = 0

    result = 0
    for i in range(0, x):
        throw = randint(1, y)
        result = result + throw
    result = result + z

    return result


print(game("2D20+10"))
print(game("D20+10"))