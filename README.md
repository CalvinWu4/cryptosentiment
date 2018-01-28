# crypto-sentiment
Python webapp that shows the public sentiment on various cryptocurrencies.

Articles on various cryptocurrencies were collected from three types of sources: mainstream media, chat forums, and specialized media.
Mainstream Media source: Google news api
Chat Forum source: Reddit api
Specialized Media sources: www.coindesk.com & cointelegraph.com

In most cases, text on each type of cryptocurrency was acquired by interacting with public api thorugh get/post HTTP requests, 
but in some cases it was required to parse through the HTML code using Beautiful Soup.

The text commentary on each type of coin was placed into three text files, one for each type of source. 
The text files were sent to the google natural language processing api to determine the salience of the text. Salience is 
a measure of how focused each text was on the coin it was supposed to be discussing. This salience factor was used to weight the different
text files from mainstream media, chat forums, and specialized media. The weighted sum was the overall public sentiment towards that cryptocurrency.

This project was a collaboration between Calvin Wu, Diosdavi Lara, and Daniel Ro.
