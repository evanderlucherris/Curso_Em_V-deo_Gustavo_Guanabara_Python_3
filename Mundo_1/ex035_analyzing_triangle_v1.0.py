'''
Python Exercise 035:
Develop a program that reads the length of three line segments and tells the user whether or not they can form a triangle.
'''

print('-=-' * 10)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 10)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')