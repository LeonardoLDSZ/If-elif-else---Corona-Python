#Levantar informações do usuário a fim de verificar se este possui os sintomas do Corona Vírus(COVID-19)
#sintomas: coriza + tosse + dor de garganta + febre + congestão nasal + diarreia + fadiga + cansaço + Dificuldade de respirar
#fonte: https://www.bbc.com/portuguese/brasil-51946693
from time import sleep

nome = input('Digite o seu nome:')
sobrenome = input('Digite o seu sobrenome:')
idade = int(input('Digite sua idade:'))
opcao = 0
while opcao != 11:

    print('''Diagnosticar se o usuário possui os sintomas do Corona Vírus (COVID-19):
    [ 1 ] Sintoma - Coriza
    [ 2 ] Sintoma - Tosse
    [ 3 ] Sintoma - Dor de garganta
    [ 4 ] Sintoma - Febre
    [ 5 ] Sintoma - Congestão Nasal
    [ 6 ] Sintoma - Diarréia
    [ 7 ] Sintoma - Fadiga
    [ 8 ] Sintoma - Cansaço
    [ 9 ] Sintoma - Dificuldade de respirar
    [ 10 ] Sintoma - Todos os sintomas acima
    [ 11 ] Encerrar levantamento''')
    opcao = int(input('Qual seu sintoma?'))
    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5 or opcao == 6 or opcao == 7 or opcao == 8 or opcao == 9:
        print(f'{nome} {sobrenome}, {idade} anos de idade, não possui todos os sintomas do Corona Virús, contudo, deverá se dirigir ao posto de saúde mais próximo como precaução.')
        break
    elif opcao == 10:
        print(f'{nome} {sobrenome}, {idade} anos de idade, possui os sintomas do Corona Vírus e deverá se dirigir IMEDIATAMENTE ao posto de saúde mais próximo!') 
        break
    elif opcao == 11:
        print('Diagnóstico encerrado')
    else: 
        print('Opção inválida. Tente novamente')
    print('=-=' * 2)
    sleep(2)
print('Fim do diagnóstico! Até a próxima!')
                
        



