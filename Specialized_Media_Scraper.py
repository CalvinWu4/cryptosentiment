from bs4 import BeautifulSoup  #  HTML Parser
import requests  #  for requesting information from webpage on the internet
from scrape_site import get_single_item_text_data


def cointelegraph_spyder(type):
    # open('specialized_text.txt', 'w').close()  # clear text file
    # text_file = open("specialized_text.txt", "a")  # open text file
    source_code = requests.get('https://cointelegraph.com/search?query='+type)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    text = ''
    for link in soup.find_all("h2", {"class": "header"}):
        href = link.a.get("href")
        # print (str(href))
        # text_file.write(get_single_item_text_data(href).encode('utf-8')+"\n")
        text += get_single_item_text_data(href).encode('utf-8')
    # text_file.close()
    return text[:22000]

def coindesk_spyder(type):
    # open('specialized_text.txt', 'w').close()  # clear text file
    # text_file = open("specialized_text.txt", "a")  # open text file
    source_code = requests.get('https://www.coindesk.com/?s='+type)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    text = ''
    for link in soup.find_all("div", {"class": "post-info"}):
        href = link.a.get("href")
        # print (str(href))
        # text_file.write(get_single_item_text_data(href).encode('utf-8')+"\n")
        text += get_single_item_text_data(href).encode('utf-8')
    # text_file.close()
    return text[:22000]

def collect_specialized(type):
    text = ''
    text += cointelegraph_spyder(type)
    text += coindesk_spyder(type)
    return text

if __name__ == '__main__':
    collect_specialized('bitcoin')
