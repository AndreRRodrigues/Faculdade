'''
Ler um número e verificar se ele é par ou ímpar. Quando for par
armazenar esse valor em P e quando for ímpar armazená-lo em I. Exibir P e
I no final do processamento.
'''

n=int(input('digite um numero: '))

if n % 2 :
    print('o numero {} é impar logo ele vai ser armazendo em P'.format(n))
else :
    print('O numero {} é par logo ele vai ser armazenado em N'.format(n))