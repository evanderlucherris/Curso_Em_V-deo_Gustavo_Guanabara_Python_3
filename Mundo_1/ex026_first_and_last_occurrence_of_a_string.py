'''
Python Exercise 026:
Write a program that reads a phrase from the keyboard and shows how many times the letter “A” appears, 
the position where it appears the first time, and the position where it appears the last time.
'''

frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A') + 1))