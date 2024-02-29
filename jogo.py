import random
import os

nsorteado = random.randint(1,100)

while True:
    palpite = int(input('digite um numero entre 1 e 100 \n'))
    os.system('cls')

    if palpite == nsorteado:
        print(f'parabens! acertou miseravi quem te ensinou')
        break

    elif palpite < nsorteado:
        print('digite um numero maior')

    else:
    
        print('digite um numero menor')