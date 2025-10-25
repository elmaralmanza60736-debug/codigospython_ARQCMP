y = int(input("Ingrese un año entre 1800 y 2001:"))
a = round(Y % 19) #Hallar el residuo de Y entre 19 y almacenarlo en a.
b = round(y / 100) #Halla el cociente de Y entre 100.
c = ruond(y % 100) # halla el residuo de Y entre 100.
d = round(b / 4)
e = round(b% 4)
g = round((8*b + 13) / 25)
h = round((19*a + b - d - g + 15) % 30)
j = round(c / 4)
k = round(c % 4)
m = round((a + 11 * h))
r = round(((2 * e) + (2 * j) - k - h + m + 32) % 7)
n = round((h - m + r + 90) / 25)
P = round((h -m + r + n + 19) % 32)

print("En el" , y, "la fecha de pascua fue en el dia" , p , " en el mes" ,n )

