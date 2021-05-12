def strip_punctuation(str): #deleting punctuation chars in string
    for punc in punctuation_chars:
        if punc in str:
            str = str.replace(punc, '')
    return str


def get_pos(str): #get count of all positive words
    str = strip_punctuation(str).lower().split()
    positive_count = 0
    for word in str:
        if word in positive_words: positive_count += 1
    return positive_count


def get_neg(str): #get count of all negative words
    str = strip_punctuation(str).lower().split()
    negative_count = 0
    for word in str:
        if word in negative_words: negative_count += 1
    return negative_count


def twparse():
    with open('project_twitter_data.csv') as csv_tw:
        i = None
        for line in csv_tw:
            if i == None: 
                i = 'pass'
                continue
            line = line.strip().split(',')
            net_score = get_pos(line[0])-get_neg(line[0])
            fhand.write('{}, {}, {}, {}, {}'.format(line[1], line[2], get_pos(line[0]), get_neg(line[0]), net_score)+'\n') #writing to csv


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@'] #list of symbols
positive_words = [] # list of positive words to use
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = [] # list of negative words to use
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


with open('resulting_data.csv', 'w') as fhand:
    header = 'Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n'
    fhand.write(header)
    twparse()