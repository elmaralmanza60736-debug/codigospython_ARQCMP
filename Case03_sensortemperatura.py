vs = 20 #voltios
RS = 75 #ohmios
RO = 100 # Ohmios
K = 0.5 #adimensional
done = 1

while done:
	VM = float(input ("Ingrese el voltage mostrado en el multimetro: "))

	if VM >= 12.0 and VM <= 18.0: # si vm esta entre
		T = (RS / K) * (VM/(VS - VM)) - (RO/K)
		print("La temperatura de la camara de gas es:",T)
		done = 0
else:
	print("voltaje incorrecto. Por favor ingrese nuevamente el valor.")
