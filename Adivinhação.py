print('***********************')
print('* JOGO DA ADIVINHAÇÃO *')
print('***********************')

numero_secreto = 42
total_de_tentativas = 3


for rodada in range(1, total_de_tentativas +1 ):
 print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
 
 chute = int(input('\nDigite o seu número: \n'))
 print('\nVocê digitou:\n', chute)
 
 acertou = numero_secreto == chute
 maior = chute > numero_secreto
 menor = chute < numero_secreto 
 
 if(acertou):
    print('\nVocê acertou!!!')
    break
 elif(maior):
    print('\nVocê errou! O seu chute foi maior que o número secreto')
 elif(menor):
    print('\nVocê errou! O seu chute foi menor que o número secreto')

print('\nFIM DE JOGO!!!\n')