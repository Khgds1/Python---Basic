print('-Seja Bem-vindo ao PassCenter v1.0-\n\nO que deseja?')
menu = "1-Comprar Passagem\n2-Consultar Passagem\n3-Abrir uma reclamação"
print(menu)
sep = '-'*12
op1 = int(input())
pp = 1
pas = 'a'
if op1 == 1:
    print(sep)
    print('-Comprar Passagem-')
    origem = str(input('Informe a Origem: '))
    destino = str(input('Informe o Destino: '))
    dataP = str(input('Informe a data de partida: '))
    dataR = str(input('Informe a data de retorno: '))
    pp = 0
if op1 == 2:
    if pp == 0:
        print(pas)
    if pp == 1:
        print('Você não possui passagens')
if op1 == 3:
    print(sep)
    print('Infelizmente nossos serviços de atendimento se encontram fora do ar')
