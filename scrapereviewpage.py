import requests
import lxml.html
from lxml import etree
import time
import csv
import numpy as np
import pandas as pd

#import links for webpage reviews
linkpath = '/Users/scottgleave/Downloads/DataMiningCourse/finalprojectdata/links3.csv'
df = pd.read_csv(linkpath, sep = ',', header = None)
df.columns = ['link', 'rating', 'platform', 'genre', 'date']
hreflist = df['link'].tolist()

count = 0
#function to scrape text
def get_text(url, delay = None):
    global count
    base_url = url
    user_agent = {'User-agent': 'Mozilla/5.0'}
    #in case doesn't work
    try: 
        response = requests.get(base_url, headers=user_agent)

        html_tree = etree.HTML(response.text)

        ptext = []
        for post_id in html_tree.xpath('//p/text()'):
            ptext.append(post_id)
        
        if delay != None:
            time.sleep(delay)

        if count%10 == 0:
            print(count)

        count += 1
        return ptext
    except:
        print(url, "didn't work")
        return "null"


#scrape review texts for all links and store in list
texts = [get_text(x,1) for x in hreflist]

#write to CSV

csvfile = "/Users/scottgleave/Downloads/DataMiningCourse/finalprojectdata/reviewtext2.csv"

print('writing to CSV')
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for text in texts:
        writer.writerow([text]) 

 