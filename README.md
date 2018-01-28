# crypto-sentiment

https://brickhackcryptoapp.appspot.com

Webapp that compares sentiment of the top 10 market cap cryptocurrencies between different types of media sources (mainstream media, cryptocurrency-focused media, and social media).

Our sources for mainstream media come from the Google News API. 

Our sources for cryptocurrency-focused media are coindesk.com & cointelegraph.com, the data for which we extracted using the Beautiful Soup web scraper. 

Our source for social media is Reddit and we use its API to extract the top 50 posts (top two pages) for sentiment analysis.

We used the API from http://text-processing.com/api/sentiment/ to calculate the sentiment analysis for each cryptocurrency. We only calculated the sentiments for sentences that mentioned the selected cryptocurrency. An object that contains the probability for each label. Neg and pos will add up to 1, while neutral is standalone. If neutral is greater than 0.5 then the label will be neutral. Otherwise, the label will be pos or neg, whichever has the greater probability.
 

This app is built using the Python webapp2 framework on the Google Cloud Platform and was created during RIT's BrickHack4 from January 27-28 2018.
This project is a collaboration between Calvin Wu, Diosdavi Lara, and Daniel Ro.
