'''
python exercise 099: create a program that has a function called maior(), 
which receives several parameters with integer values. 
your program must analyze all the values and indicate which one is the largest.
'''
from time import sleep

def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()