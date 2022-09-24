salario = float(input('Qual é o salario do Funcionario? R$'))
salarionovo = salario + (salario * 15 / 100)
print('Um Funcionario que ganhava R${}, com 15% de aumento, passa a receber R${}'.format(salario,salarionovo))