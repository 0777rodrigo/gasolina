import os

def principal():
    nomes = ['Marcio','Evelim','Vinicius','Emerson','Mateus','Amanda','Fabio','Gilson']
    
    print('BEM VINDO AO JOGO DA ADVINHACAO DE NOMES')
    print('TENTE ADVINHAR UM NOME')
    
    while True:
        palpite = input('Digite um nome \n').strip().capitalize()
        os.system('cls')      
        
        if verificarnome(palpite, nomes):
            print('Muito bem! Voce acertou o nome')
            break
        else:
            print('Este nome nao confere, tente denovo')
        
def verificarnome(palpite, nomes):

    if palpite in nomes:
        return True
    else:
        return False
        
principal()