salbase=float(input('digite o seu salario: '))
graf=float(input('Qual e o seu graft: '))

salbro=salbase+graf
print(salbro)
if salbro < 1000 :
    ir = salbro*(20/100)
else :
    ir = salbro*(10/100)

salliq=salbro-ir

print(salliq)
