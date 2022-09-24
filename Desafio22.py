nome = str(input('Digite Seu Nome: ')).strip()

print('Seu Nome em Maiuscula é {}'.format(nome.upper()))
print('Seu Nome em Minuscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu Primeiro nome tem {} letras'.format(nome.find(' ')))

