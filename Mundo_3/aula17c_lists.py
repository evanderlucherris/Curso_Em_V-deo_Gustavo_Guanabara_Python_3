a = [2, 3, 4, 7]
b = a[:] #COMANDO QUE CRIA UMA COPIA DA LISTA EM INTERESSE
b[2] = 8 #ESTE COMANDO ALTERA O VALOR DA LISTA
#SE b = a SOMENTE, AO ALTERAR O VALOR, SERIA APLICADO NAS DUAS LISTAS
print(f'Lista A: {a}')
print(f'Lista B: {b}')