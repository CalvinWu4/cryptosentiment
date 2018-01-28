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

class MainPage(webapp2.RequestHandler):
    def get(self):
        # Use the App Engine Requests adapter. This makes sure that Requests uses
        # URLFetch.
        requests_toolbelt.adapters.appengine.monkeypatch()

        # gets the top 10 cryptocurrencies from the coinmarketcap API
        payload = {'limit': '10'}
        toptencryptos = requests.get('http://api.coinmarketcap.com/v1/ticker/', params=payload).json()

        for element in toptencryptos:
            text = collect_mainstream(element['name'].replace(' ', '-'))
            sliced_text = text[:45000]
            # element['response'] = sliced_text
            analysis_result = get_sentiment_analysis(sliced_text)
            element['response'] = analysis_result
            print element

        template_values = {
            'cryptos': toptencryptos
        }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.write(template.render(path, template_values))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
