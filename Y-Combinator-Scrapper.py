from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Set the path to the GeckoDriver executable
gecko_driver_path = '/usr/bin/geckodriver'

# Configure the options for the geckodriver
options = webdriver.FirefoxOptions()
#optionally make it so the GUI of the browser won't appear
#options.add_argument('--headless')

# declaring instance of gecko
driver = webdriver.Firefox(executable_path=gecko_driver_path, options=options)

# opening the website 
url = 'https://news.ycombinator.com/'
driver.get(url)

# get the number of pages to be loaded from the command line
if len(sys.argv) > 2:
    iteration = int(sys.argv[2])
else:
    iteration = 1

post_num = 1
while iteration > 0:
	#open XML file to write everything i find in 
    with open("results.xml", "a") as f:
        f.write("<?xml version=\"1.0\"?> \n")
        f.write("<articles> \n")

        while True:
            # wait for content to load
            WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loading-spinner')))

            # grab the titles, authors, and ages of the posts using their class
            article_titles = driver.find_elements(By.XPATH, "//span[@class='titleline']/a")
            author_names = driver.find_elements(By.XPATH, "//a[@class='hnuser']")
            ages = driver.find_elements(By.XPATH, "//span[@class='age']")
		
	    #writing everything to the XML file 
            for i in range(len(article_titles)):
                f.write("<post" + str(post_num) + "> \n")
                post_title = article_titles[i].text
                f.write("<title>" + post_title + "</title> \n")
                post_age = ages[i].text
                f.write("<age>" + post_age + "</age> \n")
                author = author_names[i].text
                f.write("<author>" + author + "</author> \n")
                f.write("</post" + str(post_num) + "> \n")
                post_num = post_num + 1

	    #looking for the "More" button at the end of the page and "clicking" it, so it loads a new page of 30 articles
            more_link = driver.find_elements(By.CSS_SELECTOR, 'a.morelink')
            if more_link:
                more_link[0].click()
                time.sleep(2)  # Give time for the new content to load
            else:
                break

    iteration -= 1

with open("results.xml", "a") as f:
    f.write("</articles> \n")
# Close the browser
driver.quit()
