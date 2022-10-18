argument_pierwszy = float(input("Podaj pierwszy argument: "))

argument_drugi = float(input("Podaj drugi argument: "))



operacja = (input("Jaką operację chcesz wykonać? 1) dodawanie 2) odejmowanie 3) mnożenie 4) dzielenie 5) potęgowanie "))

if operacja == "1":
    print("To twój wynik dodawania: ", argument_pierwszy+argument_drugi)
if operacja == "2":
    print("To twój wynik odejmowania: ", argument_pierwszy-argument_drugi)
if operacja == "3":
    print("To twój wynik mnozenia: ", argument_pierwszy*argument_drugi)
if operacja == "4"and argument_drugi== 0:
    exit()
else:
    print("wynik dzielenia: ", argument_pierwszy/argument_drugi)
if operacja == "5":
    print("To twój wynik potęgowania: ", argument_pierwszy**argument_drugi)
