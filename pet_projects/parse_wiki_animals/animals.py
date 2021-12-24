import urllib.request as urllib
from bs4 import BeautifulSoup
import ssl
import sqlite3

conn = sqlite3.connect('animals.sqlite')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Animals;

CREATE TABLE Animals (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
)
''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ANIMALS = dict()
URL = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'

def parse_sql():
    global ANIMALS
    cur.execute('SELECT count(*) FROM Animals')
    number_of_animals = cur.fetchone()[0]
    for id in range(1, number_of_animals + 1):
        cur.execute('SELECT name FROM Animals WHERE id = ? ', (id, ))
        row = cur.fetchone()[0]
        ANIMALS[row[0]] = ANIMALS.get(row[0], 0) + 1



def parse_wiki(url_link):
    fhand = urllib.urlopen(url_link, context = ctx).read()
    soup = BeautifulSoup(fhand, 'html.parser')
    tags = soup('a')
    return tags


def parse():
    while True:
        global URL
        tags = parse_wiki(URL)
        if 'Aaaaba' in str(tags): break
        for tag in tags:
            if 'Следующая страница' in str(tag): URL = 'https://ru.wikipedia.org/' + str(tag.get('href'))
            if tag.get('title', None) == None: continue
            if tag.get('title') == 'Служебная:Категории': break
            if ':' in str(tag.get('title')): continue
            cur.execute('''INSERT OR IGNORE INTO Animals (name) VALUES ( ? )''', ( tag.get('title'), ) )
            conn.commit()
    parse_sql()


parse()
cur.close()
print(ANIMALS.items())