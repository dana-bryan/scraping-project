from bs4 import BeautifulSoup
import requests
import time
import csv

# base url/ page 1
url = 'https://www.wuft.org/news/category/environment/'

# open new file for writing
csvfile = open("project2.csv", 'w', newline='', encoding='utf-8')
c = csv.writer(csvfile)
# write the header row in the CSV
c.writerow(['Headings', 'Dates', 'Summaries'])



def get_articles(soup, list):
    boxes = soup.find_all('article', class_='item-list')

    for box in boxes:
        try:
            list = []
            list.append(box.h2.text.strip('\n\r\t'))
            list.append(box.span.text.strip('\n\r\t'))
            list.append(box.find("div", class_="entry").find("p").text.strip('\n\r\t'))
            time.sleep(3)
        except:
            list.append("None")
        c.writerow(list)
    return list

list = ["Headings", "Dates", "Summaries"]

for i in range(1, 40):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    list = get_articles(soup, list)
    # example - https://www.mlssoccer.com/players?page=23
    url = 'https://www.wuft.org/news/category/environment/page/' + str(i + 1)


csvfile.close()
