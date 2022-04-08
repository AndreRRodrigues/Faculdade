'''
Construa um diagrama de blocos para ler uma variável numérica N e
imprimi-la somente se a mesma for maior que 100, caso contrário imprimi-
la com o valor zero
'''
n=int(input('digte um numero: '))

if n > 100 :
    print('{} e maior que 100'.format(n))
else :
    print('{} Não e maior que 100'.format(n))