names = []
for i in range(5):
    name = input("Escreva seu nome: ")
    names.append(name)
    print(names)

for name in names:
    if name.startswith('F'):
        print(name)
