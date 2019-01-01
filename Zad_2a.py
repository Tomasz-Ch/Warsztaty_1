# Warsztat: Symulator LOTTO.
#
# Jak wszystkim wiadomo, LOTTO to gra liczbowa polegająca na losowaniu 6 liczb z zakresu 1–49. Zadaniem gracza jest poprawne wytypowanie losowanych liczb. Nagradzane jest trafienie 3, 4, 5 lub 6 poprawnych liczb.
#
# Napisz program, który:
#
# zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
# czy wprowadzony ciąg znaków jest poprawną liczbą,
# czy użytkownik nie wpisał tej liczby już poprzednio,
# czy liczba należy do zakresu 1-49,
# po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie,
# wylosuje 6 liczb z zakresu i wyświetli je na ekranie,
# poinformuje gracza, czy trafił przynajmniej "trójkę".

import random


def get_winning_list():
    return random.sample(range(50), 6)


def get_user_list():
    usr_numbers = []

    while len(usr_numbers) < 6:
        try:
            give_number = int(input("podaj liczbe: "))
            if give_number < 1 or give_number > 49:
                print("Liczba powinna być z zakresu [1, 49]")
            elif give_number in usr_numbers:
                print("Liczba powtarza")
            else:
                usr_numbers.append(give_number)

        except ValueError:
            print("musisz podac liczby z zakresu [1, 49]")

    usr_numbers.sort()
    return usr_numbers


def check_winning_numbers(winning_list, usr_numbers):
    win_qty = 0

    for i in usr_numbers:
        if i in winning_list:
            win_qty = win_qty + 1
    if win_qty >= 3:
        print("Trafiles " + str(win_qty))


def lotto():
    winning_list = get_winning_list()
    print(winning_list)
    usr_numbers = get_user_list()
    print(usr_numbers)

    check_winning_numbers(winning_list, usr_numbers)


lotto()