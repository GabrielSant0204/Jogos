1
import random
def jogar():
    print('================================')
    print("bem vindo ao ogo de adivinhação")
    print('================================')

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000



    print('qual o nível de dificuldade?')
    print('(1)- Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível: '))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2 ):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range (1, total_de_tentativas + 1):
        print("tentativa ", rodada, "de", total_de_tentativas)
        chute_str = input('digite um número entre 1 e 100: ')
        print('você digitou', chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print('você deve digitar um número entre 1 e 100')
            continue

        acertou = chute == numero_secreto
        maior = chute>numero_secreto
        menor = chute<numero_secreto

        if(acertou):
         print('você acertou')
         print('**você fez {} pontos!**'.format(pontos))
         break
        else:
            if(maior):
                print('você errou! o seu chute foi maior que o numero secreto')
            elif(menor):
                print('você errou! o seu chute foi menor que o numero secreto')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print('fim de jogo')
    print('o número sorteado foi', numero_secreto)

    print('jogar novamente?')
    de_novo = int(input('1- sim 0-não   '))
    while (de_novo >= 1):
        jogar()


if(__name__=='__main__'):
    jogar()