sinal = 0
sep = '-'*12
#Contadores
totalC = 0
totalM = 0
compac = 0
#Armazenado
menorvalf = 0
vtotal = 0
qtdM = 0
#ClienteMenorValor
vmenor = '-'
val1 = 100*1000000
#Calculos
mediaM = 0
tcg = 0
tca = 0

while sinal == 0:
    venda = str(input('O dia foi encerrado?(S ou N): '))
    back = 0
    if venda == 'N':
        cod = int(input('Código do Cliente: '))
        nome = str(input('Nome do Cliente: '))
        sexo = str(input('Sexo (M ou F): '))
        if sexo == 'M':
            qtdM = qtdM + 1
        while back == 0:
            ins = str(input('Deseja inserir uma venda?(S ou N: )'))
            if ins == 'S':
                tcg = tcg + 1
                valor = float(input('Valor: '))
                qtd = int(input('Quantidade: '))
                preco = valor*qtd
                vtotal = vtotal + preco
                if sexo == "F" and preco < val1:
                    val1 = preco
                    vmenor = nome
                if preco >= 200:
                    tca = tca + 1
            if ins == 'N':
                back = 1
    if venda == 'S':
        print(sep)
        print('Finalizando o dia')
        perc1 = tcg/100
        perc = tca/perc1
        print(sep)
        print('Valor total arrecadado: R${}'.format(vtotal))
        print('Média de clientes do sexo masculino que realizaram compras durante o dia: {}'.format(qtdM))
        print('Nome da Cliente com menor valor de compra: {}'.format(vmenor))
        print('Percetual de clientes com valor de compra acima de R$200,00: {}%'.format(perc))
        sinal = 1
