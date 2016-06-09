import nltk
nltk.data.show_cfg('grammars/book_grammars/sql1.fcfg')


from nltk import load_parser
test = load_parser('grammars/book_grammars/sql1.fcfg')
q=" What cities are in Greece"
t = list(test.parse(q.split()))
ans = t[0].label()['SEM']
ans = [s for s in ans if s]
q = ' '.join(ans)
print(q)
from nltk.sem import chat80
r = chat80.sql_query('corpora/city_database/city.db', q)
for p in r:
    print(p[0], end=" ")
