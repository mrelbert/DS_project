from selenium import webdriver
from bs4 import BeautifulSoup
from random import randint
from height import feet_to_cm, define_goal
from selenium.common.exceptions import NoSuchElementException
import time
import json

features = []
labels = []

browser = webdriver.Chrome()
url = "https://bodyspace.bodybuilding.com/member-search"
browser.get(url)

# html = browser.page_source
# soup = BeautifulSoup(html, "html.parser")

# Going through pagination
pages_remaining = True
page_number = 1
counter = 1
index = 0

while pages_remaining:

    # if counter == 70:
    #     pages_remaining = False

    # update html and soup
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    # FETCH AGE, HEIGHT, WEIGHT, & FITNESS GOAL

    metrics = soup.findAll("div", {"class": "bbcHeadMetrics"})

    for x in range(0, len(metrics)):
        tempDataSet = []
        metrics_children = metrics[index].findChildren()

        details = soup.findAll("div", {"class": "bbcDetails"})
        individual_details = details[index].findChildren()

        if len(individual_details) > 16:
            # print ("index: " + str(counter) + " / Age: " + individual_details[2].text + " / Height: " + individual_details[4].text + " / Weight: " + individual_details[7].text + " / Gender: " + individual_details[12].text + " / Goal: " + individual_details[18].text)

            # AGE
            if individual_details[2].text == "--":
                tempDataSet.append(randint(28, 50))
            elif individual_details[2].text > 110:
                tempDataSet.append(randint(28, 50))
            else:
                tempDataSet.append(int(individual_details[2].text))

            # HEIGHT IN CM
            tempDataSet.append(feet_to_cm(str(individual_details[4].text)))

            # WEIGHT
            weight = str(individual_details[7].text)
            if weight.strip() == "--":
                tempDataSet.append(randint(28, 50))
            else:
                weight_substring = weight[:3]
                tempDataSet.append(int(weight_substring))

            # GENDER
            gender = str(individual_details[12].text)
            if gender == "male":
                tempDataSet.append(1)
            elif gender == "female":
                tempDataSet.append(0)
            else:
                tempDataSet.append(2)

            # GOALS
            labels.append(define_goal(str(individual_details[18].text)))

        else:
            # print ("index: " + str(counter) + " / Age: " + individual_details[2].text + " / Height: " + individual_details[4].text + " / Weight: " + individual_details[7].text + " / Gender: " + individual_details[12].text + " / Goal: " + individual_details[15].text)

            # AGE
            if individual_details[2].text == "--":
                tempDataSet.append(randint(28, 50))
            else:
                tempDataSet.append(int(individual_details[2].text))

            # HEIGHT IN CM
            tempDataSet.append(feet_to_cm(str(individual_details[4].text)))

            # WEIGHT
            weight = str(individual_details[7].text)
            if weight.strip() == "--":
                tempDataSet.append(randint(28, 50))
            else:
                weight_substring = weight[:3]
                tempDataSet.append(int(weight_substring))

            # GENDER
            gender = str(individual_details[12].text)
            if gender == "male":
                tempDataSet.append(1)
            elif gender == "female":
                tempDataSet.append(0)
            else:
                tempDataSet.append(2)

            # GOALS
            labels.append(define_goal(str(individual_details[15].text)))

        features.append(tempDataSet)
        index = index + 1
        counter = counter + 1

    try:
        print(features)
        print("FEATURES SET LENGTH: " + str(len(features)))
        print(labels)
        print("LABELS SET LENGTH: " + str(len(labels)))

        page_number = page_number + 1
        next_link = browser.find_element_by_xpath('//*[@title="Go to page {0}"]'.format(str(page_number)))
        next_link.click()
        index = 0
        time.sleep(30)

    except NoSuchElementException:
        rows_remaining = False

thefile = open('data.txt', 'w')

thefile.write(str(len(features)) + "FEATURES")
for item in features:
  thefile.write("%s\n" % item)

thefile.write(str(len(labels)) + "LABELS")
for item in labels:
  thefile.write("%s\n" % item)
