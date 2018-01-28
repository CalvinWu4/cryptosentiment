import requests
from bs4 import BeautifulSoup  #  HTML Parser


def get_single_item_text_data(item_url):
    article_text = ''
    # catches the exception that there is a bad website link
    try:
        source_code = requests.get(item_url, timeout=None)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')

        article = soup.findAll('p')
        for element in article:
            article_text += '\n' + ''.join(element.findAll(text=True))
    except:
        pass
    return article_text