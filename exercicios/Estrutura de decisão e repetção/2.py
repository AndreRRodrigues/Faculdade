th=int(input('quantas horas voce trabalhou? '))
gh=10
eh=20
tx=50
pag=th*gh

if th > tx :
    pagex=(th-tx)*eh
    print('hoje seu salario foi de {} Reais, como voce fez hora extra voce ganhou {} a mais no total ficou {}'.format(pag, pagex, (pag+pagex)))

else :
    print('Poderia ter ganhado um dinheirinho extra mas ta tranquilo, hoje voce ganhou {} Reais, Gaste com sabedoria'.format(pag))