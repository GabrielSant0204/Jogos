import forcafinalizado
import adivinhacao

def escolhe_jogo():
    print('================================')
    print("escolha o seu jogo!")
    print('================================')

    print('(1) Forca  (2) adivinhação')

    jogo = int(input('qual jogo?>>>  '))

    if(jogo == 1):
        print('Jogando Forca')
        forcafinalizado.jogar()

    elif(jogo == 2):
        print('jogando adivinhação')
        adivinhacao.jogar()


if(__name__=='__main__'):
    escolhe_jogo()