a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #VAI CONCATENAR OS VALORES DAS TUPLAS
d = b + a
print(c)
print(c.count(5)) #MOSTRA QUANTAS VEZES APARECE O VALOR INSERIDO (n5)
print(c.index(2, 4)) #AQUI ELE CONTA O MESMO VALOR NA POSIÇÃO SEGUINTE
#NESSE CASO, ELE VAI BUSCAR A SEGUNDA POSIÇÃO DO VALOR 2 QUE ESTÁ NA POSIÇÃO 6 (0-6)

print(d)
print(d.index(8))