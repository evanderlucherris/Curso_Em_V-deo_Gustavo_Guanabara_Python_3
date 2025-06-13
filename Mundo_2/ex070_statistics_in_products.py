'''
Python Exercise 070:
Create a program that reads the name and price of several products. 
The program should ask the user whether they want to continue. 
At the end, show:
A) The total amount spent on the purchase.
B) How many products cost more than R$1000.
C) The name of the cheapest product.
'''

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{'FIM DO PROGRAMA':-^40}')
print(f'O total da compra foi R${total:.2f}')
print(f'temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato que foi {barato}, custa R${menor:.2f}')