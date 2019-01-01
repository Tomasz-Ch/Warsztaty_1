from flask import Flask, request

app = Flask(__name__)

min_num = 0         # zmienne globalne używane później wewnątrz funkcji
max_num = 1000
guess = 0


@app.route("/", methods = ["GET", "POST"])

def game():
    global min_num
    global max_num
    global guess

    form = '''
        <form method="POST">
            <input type = "submit" name="user_response" value="za malo">
            <input type = "submit" name="user_response" value="za duzo">
            <input type = "submit" name="user_response" value="wygrales">
        </form>
        '''

    if request.method == "GET":
        guess = int((max_num - min_num) / 2) + min_num

        return str(guess) + "?" + form
    if request.method == "POST":
        result = request.form["user_response"]
        if result == "za duzo":
            max_num = guess
            guess = int((max_num - min_num) / 2) + min_num
            return str(guess) + form
        if result == "za malo":
            max_num = guess
            guess = int((max_num - min_num) / 2) + min_num
            return str(guess) + form
        if result == "wygrales":
            min_num = 0
            max_num = 1000
            return result







# def guess_number():         #log przy podstawie 2 z 1000
#     print("Pomyśl liczbę od 1 do 1000, a ja ją zgadnę:")
#     min_num = 0
#     max_num = 1000
#     guessed = False
#     tricked = False
#     while not guessed:
#         guess = int((max_num - min_num) / 2) + min_num
#         print("Zgaduję: " + str(guess))
#         user_response = input("czy zgadłem?")
#         if user_response == "za mało":
#             if (min_num == max_num):
#                 print("Oszukałeś, kończę gre!")
#                 tricked = True
#             min_num = guess
#         elif user_response == "za dużo":
#             if (min_num == max_num):
#                 print("Oszukałeś, kończę gre!")
#                 tricked = True
#             max_num = guess
#         elif user_response == "zgadłeś":
#             guessed = True
#             print("Wygrałem!")
#         else:
#             print("Nie oszukuj, podaj 'za dużo', 'za mało' lub 'wygrałeś'!")

app.run(debug = True)