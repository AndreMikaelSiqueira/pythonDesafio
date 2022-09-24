larg = float(input('Largura da parede:'))
alt = float(input('Altura Da Parede'))
área = larg * alt
print('Sua parede tem a dimensao de {}x{} e sua area é de {}m2'.format(larg,alt,área))
tinta = área / 2
print('para pintar essa parede voce precisara de {}l de tinta'.format(tinta))