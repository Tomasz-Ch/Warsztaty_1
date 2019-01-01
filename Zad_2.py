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

def lotto():
    winning_list = random.sample(range(50), 6)
    print(winning_list)
    usr_numbers = []

    while len(usr_numbers) < 6:
        try:
            give_number = int(input("Podaj liczbę: "))
            if give_number < 1 or give_number > 49:
                print("Liczba musi być z zakresu 1 do 49.")
            elif give_number in usr_numbers:
                print("Liczba się powtarza.")
            else:
                usr_numbers.append(give_number)
        except ValueError:
            print("Musisz podać liczby")

    usr_numbers.sort()
    print(usr_numbers)

    win_qty = 0
    for i in usr_numbers:
        if i in winning_list:
            win_qty = win_qty + 1
    if win_qty >= 3:
        print("Trafiłeś " + str(win_qty))


lotto()