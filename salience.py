import requests

def get_salience(content, coin):
    return 1
    result = requests.post('https://language.googleapis.com/v1/documents:analyzeEntitySentiment?key='
                           'AIzaSyAYinBVEi8o8kXMdayxCWqDFVE0R5WekkU',
                           json={
'document': {
 "content": content,
 "type": "PLAIN_TEXT"
},
"encodingType": "UTF8"
}, timeout=None)
    result = result.json()['entities']
    for element in result:
        if coin.lower() == element['name'].lower():
            return element['salience']

if __name__ == '__main__':
    print(get_salience('Bitcoin Cash is a shit coin.', 'Bitcoin Cash'))


