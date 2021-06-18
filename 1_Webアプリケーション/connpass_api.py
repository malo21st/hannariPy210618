import MeCab
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import requests

URL = 'https://connpass.com/api/v1/event'

def get_words(nickname, count):
    url_query = f'{URL}/?nickname={nickname}&count={count}&order=2'
    response = requests.get(url_query).json()
    if response['results_available'] == 10000:
        return "該当ありません"
    events = response['events']

    text = ""
    for event in events:
        for key, item in event.items():
            if key == "title":
                e_title = item
            try:
                if key == "series":
                    s_title = item['title']
            except:
                s_title = ""
        text += f'{e_title} {s_title} '
    
    mecab = MeCab.Tagger()
    parts = mecab.parse(text)
    nouns = []
    for part in parts.split('\n')[:-2]:
        if '名詞' in part.split('\t')[4]:
            nouns.append(part.split('\t')[0])
            
    return ' '.join(nouns)

if __name__ == '__main__':
    main()