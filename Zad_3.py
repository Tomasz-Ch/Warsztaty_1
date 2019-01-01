def guess_number():         #log przy podstawie 2 z 1000
    print("Pomyśl liczbę od 1 do 1000, a ja ją zgadnę:")
    min_num = 0
    max_num = 1000
    guessed = False
    tricked = False
    while not guessed or not tricked:
        guess = int((max_num - min_num) / 2) + min_num
        print("Zgaduję: " + str(guess))
        user_response = input("czy zgadłem?")
        if user_response == "za mało":
            if (min_num == max_num):
                print("Oszukałeś, kończę gre!")
                tricked = True
            min_num = guess
        elif user_response == "za dużo":
            if (min_num == max_num):
                print("Oszukałeś, kończę gre!")
                tricked = True
            max_num = guess
        elif user_response == "zgadłeś":
            guessed = True
            print("Wygrałem!")
        else:
            print("Nie oszukuj, podaj 'za dużo', 'za mało' lub 'wygrałeś'!")



guess_number()