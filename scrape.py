from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import time
import json

data = {}

browser = webdriver.Chrome()
url = "https://bodyspace.bodybuilding.com/member-search"
browser.get(url)

html = browser.page_source
soup = BeautifulSoup(html, "html.parser")

# Going through pagination
pages_remaining = True
counter = 1
index = 0

while pages_remaining:

    #DO YOUR THINGS WITHIN THE PAGE
    # FETCH AGE, HEIGHT, WEIGHT, & FITNESS GOAL

    metrics = soup.findAll("div", {"class": "bbcHeadMetrics"})
    print(metrics)

    for x in range(0, len(metrics)):
        metrics_children = metrics[index].findChildren()

        details = soup.findAll("div", {"class": "bbcDetails"})
        individual_details = details[index].findChildren()

        if len(individual_details) > 16:
            print ("index: " + str(counter) + " / Age: " + individual_details[2].text + " / Height: " + individual_details[4].text + " / Weight: " + individual_details[7].text + " / Gender: " + individual_details[12].text + " / Goal: " + individual_details[18].text)
        else:
            print ("index: " + str(counter) + " / Age: " + individual_details[2].text + " / Height: " + individual_details[4].text + " / Weight: " + individual_details[7].text + " / Gender: " + individual_details[12].text + " / Goal: " + individual_details[15].text)

        index = index + 1
        counter = counter + 1

    try:
        #Checks if there are more pages with links
        next_link = browser.find_element_by_xpath('//a[@id = 'unique-id']/@href ')
        next_link.click()
        # time.sleep(30)
    except NoSuchElementException:
        rows_remaining = False
