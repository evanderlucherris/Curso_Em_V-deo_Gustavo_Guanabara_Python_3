'''
python exercise 086:
create a program that declares a 3×3 matrix and fills it with values entered via the keyboard.
in the end, display the matrix on the screen with proper formatting.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a [{l}, {c}]: '))
print('=-'*30)
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
    print()