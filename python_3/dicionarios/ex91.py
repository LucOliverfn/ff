from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6),}
ranking = []
print ('valores sorteados: ')
for k,v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking =sorted(jogo.items(),key=itemgetter(1), reverse=True)
for k,v in enumerate(ranking):
    print(f'{k+1} lugar {v[0]} com {v[1]}.')
    sleep(1)
