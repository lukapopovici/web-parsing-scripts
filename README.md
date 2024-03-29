# web-parsing-scripts
<p align="center">
  <img src="https://static.wikia.nocookie.net/minecraft_gamepedia/images/e/ec/Diamond_Shovel_JE3_BE3.png/revision/latest?cb=20200226194003" alt="Shoverl"/>
</p><br />
A repository for web scrapers mostly written in Python using the Selenium framework.
I'll add more to this repository as I learn more. 

# Why does this exist?
I've been curious for a while about why some websites have the "Prove you are not a robot" prompt before allowing you acces to their content. Then, I found out about data mining and browser automation. I made this repository to document my learning process in this field.

## [Github page scraper](https://github.com/lukapopovici/web-parsing-scripts/blob/main/Github_scraper.py)
This scraper retrieves the links of trending projects from a topic page specified as a parameter. <br />
The script utilizes Selenium to dynamically load new articles based on the value of the other parameter. Each increment of the parameter loads 40 more entries from the page.To begin the scraping process, the script first loads the initial page. Then, it continuously clicks on the "Load more" button as specified by the second parameter. This allows for the retrieval of additional content. Once all the desired content has been loaded, it will be extracted and stored in an XML file.<br />
This is the first dinamically loaded page I have "scraped" that justifies the use of an automation framework.

## [Y-Combinator forum scraper](https://github.com/lukapopovici/web-parsing-scripts/blob/main/Y-Combinator-Scrapper.py)
A web scraper made with the purpose of getting data about popular posts on the Y-Combinator forum.Despite Hacker News being a static website that I could have accesed via requests (ex: I could have accesed all the pages after the frontpage by simply requesting them by adding /?p=$nextpagenumber in front of the url), I opted to use the automation framework Selenium instead.
<br />I use Selenium to "click" on the "More" button at the bottom of the page, so that it loads the next page of the forum to be analyzed. And it will keep on going until the number of pages loaded reaches the value read as a parameter at the script's execution.

## [A Basic Web Parser](https://github.com/lukapopovici/web-parsing-scripts/blob/main/basic_webparser.py)
Basic web parser made for static html pages. Gets all the links from a page ,and can also do so recursively, with a recursivity level that can be set.The url of the scraped page and the recursivity level can be read from the command line when executing the script. Everything captured gets written on a text file.<br />
Since it's only for static webpages, I didn't see the need to use more complicated frameworks. And so, I settled for the Beautiful Soup module, as to not overcomplicate myself.




## Resources
[Installing Firefox without Snap](https://www.omgubuntu.co.uk/2022/04/how-to-install-firefox-deb-apt-ubuntu-22-04) In order to avoid the issue of it not being found when using the gecko driver engine on Ubuntu,where it's installed from snap by default.<br />
[Gecko Webdriver Installer](https://github.com/lukapopovici/dotfiles-and-scripts/blob/main/install_gecko.sh)
Distro-agnostic script that downloads and installs the "freshest" release of the Gecko Webdriver and moves it to /usr/bin.
