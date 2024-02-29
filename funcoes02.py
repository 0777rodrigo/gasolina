valores = [10, 20, 30, 40, 50]

def soma_valores(valores):
    
    total = 0
    for valor in valores:
        total += valor
    return total

def calcula_media(valores):

    total = soma_valores(valores)
    media = total / len(valores)
    return media

resultado = soma_valores(valores)
media = calcula_media(valores)
print("Soma:", resultado)
print("Média:", media)