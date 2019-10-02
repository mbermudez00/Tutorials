from unicodedata import normalize
import pandas as pd

a = open('streets.txt','r')
out = open('out.txt', 'w') 
change = {'Autopista':'carretera',
        'Calle':'avenida',
        }

for s in a:
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    s = normalize('NFKC', normalize('NFKD', s).translate(trans_tab))
    for i in change:
        if i in s:
            print(change[i])
            s = change[i]
    out.write(s.upper())

print("finish!")
