import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_website(url, recursion_level):
    # sending request and checking if it got greenlit
    response = requests.get(url)
    if response.status_code == 200:
        # create bfs instance and specify parser
        soup = BeautifulSoup(response.content, 'html.parser')

        # extract all link elements
        links = soup.find_all('a')

        # open the file in append mode
        with open("results.txt", "a") as f:
            # printing and writing the results to the file
            for link in links:
                if 'href' in link.attrs:
                    absolute_url = urljoin(url, link['href'])
                    #printing 
                    print("[*]Recursion level: "+str(recursion_level)+" "+absolute_url)
                    f.write("[*]Recursion level: "+str(recursion_level)+" "+absolute_url)

                    if recursion_level > 0:
                        scrape_website(absolute_url, recursion_level - 1)
    else:
        print('Error accessing the website.')


if len(sys.argv) != 3:
    print("Usage: python script.py website_url recursion_level")
else:
    # get function parameters as arguments from the cmd
    website_url = sys.argv[1]
    recursion_level = int(sys.argv[2])-1

    scrape_website(website_url, recursion_level)
