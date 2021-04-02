from bs4 import BeautifulSoup
import re
import codecs

HTML = codecs.open('atest.html', 'r', 'utf-8').read()

def parse_name(name):
    if len(name) > 3 or len(name) < 1: return 'Упс! Кажется, что-то слишком сложное :('
    elif len(name) == 3: return 'Ура! Мы нашли фамилию: ' + name[0] + ', имя: ' + name[1] + ', отчество: ' + name[2] + '!'
    elif len(name) == 2: return 'Ура! Мы нашли фамилию: ' + name[0] + ', имя: ' + name[1] + '!'
    elif len(name) == 1: return 'Ура! Мы нашли имя: ' + name[0] + '!'

def parse_html(html):
    soup = BeautifulSoup(HTML, 'html.parser')
    tags = soup('p')
    for tag in tags:
        if 'class' not in str(tag): continue
        if tag.get('class')[0] != 'full_name': continue
        name = re.findall('[а-яА-Я]+', str(tag))
        print(parse_name(name))

parse_html(HTML)
