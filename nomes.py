nomes = []

for x in range(5):
    nome = input("digite o nome: ").strip().capitalize()
    nomes.append(nome)

for nome in nomes:
    if nome.startswith('F'):
        print(nome)