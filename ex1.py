"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati suma numerelor pana la numarul respectiv.
    exemplu:
        Veti primi: 5
        Veti printa: 15
"""
number=input()
suma=0
for i in range(0, int(number)+1):
    suma+=i

print(suma)