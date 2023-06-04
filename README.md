# web-parsing-scripts
A repository for web scrappers mostly written in Python using the Selenium framework.
I'll add more to this repository as I learn more. 

##[A Basic Web Parser](https://github.com/lukapopovici/web-parsing-scripts/blob/main/basic_webparser.py)
Basic web parser made for static html pages. Gets all the links from a page ,and can also do so recursively, with a recursivity level that can be set.The url of the scrapped page and the recursivity level can be read from the command line when executing the script. Everything captured gets written on a text file.
Since it's only for static webpages, I didn't see the need to use more complicated frameworks. And so, I settled for Beautiful Soup.
