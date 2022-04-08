'''
Elabore um diagrama de blocos que leia um número. Se positivo
armazene-o em A, se for negativo, em B. No final mostrar o resultado
'''

n=int(input('digite um nomero: '))

if n > 0 :
    print('o numero {} e positivo ele será armazenado em A'.format(n))
else:
    print('O numero {} e negativo ele sera armazenado em B'.format(n))
