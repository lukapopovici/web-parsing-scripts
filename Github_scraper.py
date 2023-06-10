from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import sys

gecko_driver_path = '/usr/bin/geckodriver'
options = webdriver.FirefoxOptions()
options.add_argument('--headless')

#function to single out and click on the "Load more" button
def click_load_more_button():
    wait = WebDriverWait(driver, 10)  
    more_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-disable-with="Loading more…"]')))
    more_button.click()

#scrolling function for dinamically loaded pages that change height as they load more content
def scroll_to_bottom():
    prev_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(5) 
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == prev_height:
            break
        prev_height = new_height


driver = webdriver.Firefox(executable_path=gecko_driver_path, options=options)

if len(sys.argv) > 2:
    url = sys.argv[1]
    iteration= int(sys.argv[2])
else:
    url = 'https://github.com/topics/3d'
    iteration= 1

driver.get(url)
#waiting until at least one h3 element is present
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3'))) 
scroll_to_bottom()

for _ in range(iteration): 
    print("[*]Loading page :"+ str(iteration)+"...\n")
    click_load_more_button()
    scroll_to_bottom()
    time.sleep(5)  

print("[*]Finished loading content.Writing to XML file... \n")
with open("results.xml", "a") as f:
    f.write("<?xml version=\"1.0\"?> \n")
    f.write("<articles> \n")

    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loading-spinner')))  # Halved waiting time to 5 seconds

    h3_elements = driver.find_elements(By.TAG_NAME, 'h3')

    for post_num, h3_element in enumerate(h3_elements, start=1):
        a_elements = h3_element.find_elements(By.TAG_NAME, 'a')

        if len(a_elements) >= 1:
            a_element = a_elements[-1]
            f.write("<post" + str(post_num) + "> \n")
            content = a_element.get_attribute('href')
            f.write("<content>" + content + "</content> \n")
            f.write("</post" + str(post_num) + "> \n")

    f.write("</articles> \n")

driver.quit()
