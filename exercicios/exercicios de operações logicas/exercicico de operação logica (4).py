'''
Tendo como dados de entrada a altura e o sexo de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes
fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 (h = altura)
'''
alt = float(input('Digite a altura: '))
sex = str(input('Digite o sexo :\n M para mulher e H para homen: '))

homen = (72.7*alt) - 58
mulher =  (62.1*alt) - 44.7
if sex == 'm' :
    print('o peso ideal é {}'.format(mulher))
elif sex == 'h' :
    print('O peso ideal é {}'.format(homen))
    