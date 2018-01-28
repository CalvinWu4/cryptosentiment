import requests

def get_salience():
    result = requests.post('https://language.googleapis.com/v1/documents:analyzeEntitySentiment?key='
                           'AIzaSyAYinBVEi8o8kXMdayxCWqDFVE0R5WekkU',
                           json={
'document': {
 "content": "de",
 "type": "PLAIN_TEXT"
},
"encodingType": "UTF8"
})
    return result.json()

if __name__ == '__main__':
    get_salience()


