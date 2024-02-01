#!/usr/bin/python3

def kalkulator(operacja, x, y):
	if operacja == '+':
		return x + y
	elif operacja == '-':
		return x - y
	elif operacja == '*':
		return x * y
	elif operacja == '/':
		if y != 0:
			return x / y
		else:
			return "Dzielenie przez zero niemozliwe!"
	else:
		return "Nieprawidlowa operacja!"

while True:
	wyrazenie = input("Podaj wyrazenie oddzielone spacja (np. 2 + 2.5, 4 * 7), lub wcisnij q aby zakonczyc): ")

	if wyrazenie.lower() == 'q':
		print("Koniec")
		break

	parts = wyrazenie.split()

	if len(parts) == 3:
		try:
			parts = wyrazenie.split()
			x = float(parts[0])
			operacja = parts[1]
			y = float(parts[2])

			wynik = kalkulator(operacja, x, y)
			print("Wynik: ", wynik)

		except (ValueError, IndexError):
			print("Nieprawidlowe wejscie, sprbuj ponownie")
	else:
		print("Nieprawidlowa ilosc parametrow. Mozna wprowadzic tylko dwie liczby")
