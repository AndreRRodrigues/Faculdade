a = int(input('informe o valor de A: '))
b = int(input('informe o valor de B: '))
c = int(input('informe o valor de C: '))

#seguno passo.
d = b**2-4*a*c
print('delta'd)

#Terceiro passo

x1=-b+(d**0.5)
xd1=x1/2*a
print('x1 {:.0f}'.format(xd1))
x2=-b-(d**0.5)
xd2=x2/(2*a)
print('x2 {:.0f}'.format(xd2))