from math import sin,cos,tan,radians
ang = float(input('Digite o ãngulo que voce deseja: '))
seno = sin(radians(ang))
cose = cos(radians(ang))
tan = tan(radians(ang))
print('O ãngulo de {:.2f} tem o SENO de {:.2f}'.format(ang,seno))
print('O ãngulo de {:.2f} tem o COSSENO de {:.2f}'.format(ang,cose))
print('O ãngulo de {:.2f} tem o TANGENTE de {:.2f}'.format(ang,tan))