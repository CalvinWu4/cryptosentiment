# crypto-sentiment

https://brickhackcryptoapp.appspot.com

Webapp that compares sentiment of the top 10 market cap cryptocurrencies between different types of media sources (mainstream media, cryptocurrency-focused media, and social media).

This app was built using the Python webapp2 framework on the Google Cloud Platform during RIT's BrickHack4 from January 27 to 28 2018.

Our sources for mainstream media come from the Google News API. 

Our sources for cryptocurrency-focused media are coindesk.com & cointelegraph.com, the data for which we extracted using the Beautiful Soup web scraper. 

Our source for social media is Reddit and we used its API to extract the top 50 posts (first two pages) for sentiment analysis.

The text commentary on each type of coin was placed into three text files, one for each type of source. 
The text files were sent to the google natural language processing api to determine the salience of the text. Salience is 
a measure of how focused each text was on the coin it was supposed to be discussing. This salience factor was used to weight the different text files from mainstream media, chat forums, and specialized media. The weighted sum was the overall public sentiment towards that cryptocurrency.

This project was a collaboration between Calvin Wu, Diosdavi Lara, and Daniel Ro.
