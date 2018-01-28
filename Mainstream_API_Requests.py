import json
import urllib2
from scrape_site import get_single_item_text_data




def request(url):
    json_obj = urllib2.urlopen(url)  # open url to get json data
    json_data = json.load(json_obj)  # load json data
    return json_data

def collect_mainstream(type):
    open('mainstream_text.txt', 'w').close()  # clear text file
    text_file = open("mainstream_text.txt", "a")  # open text file
    json_data = request('https://newsapi.org/v2/everything?q='+type+'&language=en&apiKey=fe3d3131b08445808601a5f7971f460b')
    json_data = json_data['articles']
    text = ''
    for element in json_data:
        print element["url"]
        print element["description"]
        print element['title']
        print get_single_item_text_data(element['url']).encode('utf-8')
        text += get_single_item_text_data(element['url']).encode('utf-8')
    text_file.write(text[:45000])
    text_file.close()

if __name__ == '__main__':
    cryptocurrency = 'stellar-crypto'
    collect_mainstream(cryptocurrency)