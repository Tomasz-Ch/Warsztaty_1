# Warsztat: Gra w zgadywanie liczb.
#
# Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 – 100. Następnie:
#
# Zadać pytanie: "Zgadnij liczbę" i pobrać liczbę z klawiatury.
# Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "To nie jest liczba", po czym wrócić do pkt. 1
# Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "Za mało!", po czym wrócić do pkt. 1.
# Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat "Za dużo!", po czym wrócić do pkt. 1.
# Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "Zgadłeś!", po czym zakończyć działanie programu.

import random

def guess_number():
    winning_num = random.randint(1, 100)
    victory = False
    while not victory:
        given_num = input("Insert number: ")
        try:
            given_num = int(given_num)


            if given_num > winning_num:
                print("Za dużo!")
            elif given_num < winning_num:
                print("Za mało!")
            else:
                victory = True
                print("Wygrałeś!")
        except ValueError:
            print("To nie jest liczba!")






guess_number()