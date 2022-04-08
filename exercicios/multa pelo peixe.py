qp=float(input('quantos queilos voce pescou hoje? '))
m=4
e=qp-50
if qp > 50 :
    mu= 4 * e
    print('Ouve um excesso de {} será ciobrado uma multa de {}'.format(e, mu))
else:
    #nao tem multa
    print('Fica tranquilo meu bom, sem multa pra você hoje :)')
