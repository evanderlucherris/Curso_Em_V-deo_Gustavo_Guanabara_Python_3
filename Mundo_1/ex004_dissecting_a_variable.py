'''
Python Exercise 004:
Write a program that reads something from the keyboard 
and displays its primitive type and all possible information about it.
'''

n = input('Digite algo: ')

print('O tipo primitivo desse valor é', type(n))
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('É numérico?', n.isnumeric())
print('Está em minúsculas?', n.islower())
print('Está em maiúsculas?', n.isupper())
print('Só tem espaços?', n.isspace())
print('Está capitalizada?', n.istitle())