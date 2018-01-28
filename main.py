# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import os
import template
import requests
import requests_toolbelt.adapters.appengine
from Mainstream_API_Requests import collect_mainstream
from Mainstream_API_Requests import request
import json
from sentiment_analyzer import get_sentiment_analysis
from Specialized_Media_Scraper import collect_specialized

class MainPage(webapp2.RequestHandler):
    def get(self):
        # Use the App Engine Requests adapter. This makes sure that Requests uses
        # URLFetch.
        requests_toolbelt.adapters.appengine.monkeypatch()

        # gets the top 10 cryptocurrencies from the coinmarketcap API
        payload = {'limit': '10'}
        toptencryptos = requests.get('http://api.coinmarketcap.com/v1/ticker/', params=payload).json()

        template_values = {
            'cryptos': toptencryptos
        }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.write(template.render(path, template_values))


class DataHandler(webapp2.RequestHandler):
    def post(self):
        # Use the App Engine Requests adapter. This makes sure that Requests uses
        # URLFetch.
        requests_toolbelt.adapters.appengine.monkeypatch()

        data = json.loads(self.request.body)
        name = data['name']
        print name
        # get data from mainstream sources
        text_mainstream = collect_mainstream(name.replace(' ', '-'))
        sliced_mainstream_text = text_mainstream[:45000]
        mainstream_analysis_result = get_sentiment_analysis(sliced_mainstream_text)

        # get data from specialized sources
        text_specialized = collect_specialized(name.replace(' ', '-'))
        specialized_analysis_result = get_sentiment_analysis(text_specialized)

        response = {
            'mainstream': mainstream_analysis_result,
            'specialized': specialized_analysis_result,
            'social-media': ''
        }

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(response))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/crypto/', DataHandler)
], debug=True)
