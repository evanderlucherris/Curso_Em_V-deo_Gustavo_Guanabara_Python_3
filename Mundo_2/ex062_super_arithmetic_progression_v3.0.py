'''
Python Exercise 062:
Improve CHALLENGE 61 by asking the user if they want to show more terms. 
The program will end when the user says they want to show 0 terms.
'''

print('GERADOR DE PA')
print('=-' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('A prograssão foi finalizada com {} termos.'.format(total))