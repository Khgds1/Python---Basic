intro = "Formulário"
sep = "-"*12
nome = str(input('Nome: '))
idade = int(input('Idade: '))
email = str(input('Email: '))
telefone = int(input('Telefone: '))
nacionalidade = str(input('Nacionalidade: '))
print(sep)
print('Nome: {}\nIdade: {}\nEmail: {}\nTelefone: {}\nNacionalidade: {}'.format(nome, idade, email, telefone, nacionalidade))
check = str(input('\nConfirma os dados acima?(s ou n): '))
if check == "s":
    print(sep)
    print('Seus dados foram gravados com sucesso')
else:
    print(sep)
    print('1-Nome\n2-Idade\n3-Email\n4-Telefone\n5-Nacionalidade')
    nNome = nome
    nIdade = idade
    nEmail = email
    nTelefone = telefone
    nNacionalidade = nacionalidade
    apt = str(input('\nQual dado deseja modificar?: '))
    if apt == "1":
        nNome = str(input('Nome: '))
    if apt == "2":
        nIdade = str(input('Idade: '))
    print(sep)
    print('-Dados Corrigidos-')
    print('\nNome: {}\nIdade: {}\nEmail: {}\nTelefone: {}\nNacionalidade: {}'.format(nNome, nIdade, nEmail, nTelefone, nNacionalidade))
    print('\nSeus dados foram gravados com sucesso')
