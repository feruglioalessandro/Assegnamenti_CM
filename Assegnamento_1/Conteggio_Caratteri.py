import argparse
import time
from matplotlib import pyplot as plt

## Funzione - conteggio caratteri
def conteggio_caratteri(testo):
    for carattere in testo:
        if carattere in ('a', 'A'):
            frequenza['a'] += 1
        elif carattere in ('b', 'B'):
            frequenza['b'] += 1
        elif carattere in ('c', 'C'):
            frequenza['c'] += 1
        elif carattere in ('d', 'D'):
            frequenza['d'] += 1
        elif carattere in ('e', 'E'):
            frequenza['e'] += 1
        elif carattere in ('f', 'F'):
            frequenza['f'] += 1
        elif carattere in ('g', 'G'):
            frequenza['g'] += 1
        elif carattere in ('h', 'H'):
            frequenza['h'] += 1
        elif carattere in ('i', 'I'):
            frequenza['i'] += 1
        elif carattere in ('j', 'J'):
            frequenza['j'] += 1
        elif carattere in ('k', 'K'):
            frequenza['k'] += 1
        elif carattere in ('l', 'L'):
            frequenza['l'] += 1
        elif carattere in ('m', 'M'):
            frequenza['m'] += 1
        elif carattere in ('n', 'N'):
            frequenza['n'] += 1
        elif carattere in ('o', 'O'):
            frequenza['o'] += 1
        elif carattere in ('p', 'P'):
            frequenza['p'] += 1
        elif carattere in ('q', 'Q'):
            frequenza['q'] += 1
        elif carattere in ('r', 'R'):
            frequenza['r'] += 1
        elif carattere in ('s', 'S'):
            frequenza['s'] += 1
        elif carattere in ('t', 'T'):
            frequenza['t'] += 1
        elif carattere in ('u', 'U'):
            frequenza['u'] += 1
        elif carattere in ('v', 'V'):
            frequenza['v'] += 1
        elif carattere in ('w', 'W'):
            frequenza['w'] += 1
        elif carattere in ('y', 'Y'):
            frequenza['y'] += 1
        elif carattere in ('z', 'Z'):
            frequenza['z'] += 1
            
    
## Main
start = time.time()

frequenza = {'a':0, 'b':0, 'c':0, 'd':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'y':0, 'z':0}

parser = argparse.ArgumentParser('Il programma conta la frequenza relativa dei caratteri del testo passato come argomento')
parser.add_argument('nomefile', type = str, help = 'Inserire il nome del testo da analizzare nel formato \'nomefile.txtt\'')
parser.add_argument('--isto', action = 'store_true', help = 'Se chiamato produce un istogramma della frequenza relativa delle lettere del testo')
args = parser.parse_args()

titolo = args.nomefile
testo = open(titolo, 'r', encoding="utf8").read()
conteggio_caratteri(testo)

totale_caratteri = 0
for lettera in frequenza:
    totale_caratteri += frequenza[lettera]
    
for lettera in frequenza:
    frequenza[lettera] = (frequenza[lettera]/totale_caratteri)*100
    
for lettera in frequenza:
    print(f'Frequenza del carattere {lettera}: {frequenza[lettera] : .2f}%') 

end = time.time()
tempo_di_esecuzione = end - start
print(f'Tempo di esecuzione del programma: {tempo_di_esecuzione : .2f} secondi')

if args.isto:
    plt.bar(frequenza.keys(), frequenza.values())
    plt.show()
    