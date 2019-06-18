import os

OUTF_NAME = 'json/fixed_history.json'
INF_NAME = 'json/history.json'
START = '{\"data\":['
END = ']}'

if os.path.isfile('./' + OUTF_NAME):
    os.remove(OUTF_NAME)
outf = open(OUTF_NAME, 'w+')

outf.write(START)

with open(INF_NAME, 'r') as inf:
    for i, line in enumerate(inf):
        if i != 0:
            line = ',' + line
        outf.write(line)

outf.write(END)

outf.close()
inf.close()


