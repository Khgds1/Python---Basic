cod = -1
sep = '-'*12
#Contadores
contmaior = 0
maiorES = '-'
contmenor = 100*10000
menorES = '-'
totalpi = 0
totalm = 0

while True:
    print(sep)
    cod1 = int(input('Código do Estado: '))
    if cod1 != cod:
        estado = str(input('Nome do Estado: '))
        contam = int(input('Número de pacientes com Covid-19: '))
        totalpi = totalpi + contam
        if contam < contmenor:
            contmenor = contam
            menorES = estado
        mortes = int(input('Número de óbitos: '))
        totalm = totalm + mortes
        if mortes > contmaior:
            contmaior = mortes
            maiorES = estado
    else:
        print(sep)
        perc1 = totalpi/100
        perc = totalm/perc1
        print('Estado com maior número de óbitos: {}'.format(maiorES))
        print('Estado com menor número de pacientes que testaram positivo: {}'.format(menorES))
        print('Percentual de óbitos em relação ao total de pacientes infectados: {}%'.format(perc))
