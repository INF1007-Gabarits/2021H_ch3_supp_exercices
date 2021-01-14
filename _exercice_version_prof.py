#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return voltage**2 * resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	dot_product = v1[0] * v2[0] + v1[1] * v2[1]
	return dot_product == 0

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	sum = 0
	num_values = 0
	for v in values:
		if v >= 0:
			sum += v
			num_values += 1
	return sum / num_values

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties = tens = fives = ones = 0
	while value != 0:
		if value >= 20:
			twenties += value // 20
			value = value % 20
		elif value >= 10:
			tens += value // 10
			value = value % 10
		elif value >= 5:
			fives += value // 5
			value = value % 5
		elif value >= 1:
			ones += value
			value = 0

	return (twenties, tens, fives, ones);

if __name__ == "__main__":
	#print(dissipated_power(69, 420))
	#print(dissipated_power(42, 9000))
	#print(average([1, 4, -1, 10]))
	#print(average([1, 4, -1, 10, 0]))
	#print(average([-12, -42, 1]))
	#print(average([0xDEAD, 0xBEEF, 420, 69]))
	print(bills(0))
	print(bills(1))
	print(bills(5))
	print(bills(10))
	print(bills(20))
	print(bills(420))
	print(bills(69))
	print(bills(137))
	print(bills(0xBABE))
