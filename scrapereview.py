from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import requests
import lxml.html
import time
import csv

option = webdriver.ChromeOptions()
option.add_argument(' — incognito')

browser = webdriver.Chrome(executable_path='/Users/scottgleave/Documents/chromedriver', chrome_options=option)

browser.get('https://www.ign.com/reviews/games')

# Wait 20 seconds for page to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='item-boxArt']")))
    print('loaded, gathering info now')
except TimeoutException:
    print('Timed out waiting for page to load')
    browser.quit()






#navigate to next page
count = 0
while True:
    if count == 250:
        print('done')
        break
    count +=1 
    try:
        next = browser.find_element_by_css_selector("a[id='is-more-reviews']")
        next.click()
    except:
        print('out of pages')
        count = 250
    if count%10 == 0:
        print(count)
    time.sleep(5)

titles_element = browser.find_elements_by_xpath("//h3/a")
platform = browser.find_elements_by_xpath("//h3/span")
score = []

scores = browser.find_elements_by_xpath("//span[@class='scoreBox-score']")
genre = browser.find_elements_by_xpath("//span[@class='item-genre']")
date = browser.find_elements_by_xpath("//div[@class='grid_3']/div")

platforms = []
links = []
genres = []
dates = []
count2 = 0
print('savings links')
for elem in titles_element:
    count2 += 1
    links.append(elem.get_attribute("href"))

print('saving scores')
for elem in scores:
    score.append(elem.text)

print('saving platforms')
for elem in platform:
    platforms.append(elem.text)

print('saving genre')
for elem in genre:
    genres.append(elem.text)

print('saving dates')
for elem in date:
    dates.append(elem.text)
#write to CSV

csvfile = "/Users/scottgleave/Downloads/DataMiningCourse/finalprojectdata/links3.csv"

print('writing to CSV')
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val, s,p, g,d in zip(links,score, platforms,genres,dates):
        writer.writerow([val, s,p, g,d]) 

browser.close()