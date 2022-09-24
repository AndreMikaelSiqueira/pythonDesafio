dia = float(input('Quantos Dias Alugados?'))
km = float(input('Quantos Km rodados?'))
dinheiro = (dia * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(dinheiro))