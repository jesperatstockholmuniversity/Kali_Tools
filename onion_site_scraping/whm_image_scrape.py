"""
A simple script to scrape the WHM
onion site using Selenium and the
Tor browser driver
"""

#!/bin/python3
import sys
import os
import time
import datetime
import logging
import random
import urllib.request
from os.path import isfile
import tbselenium.common as cm
from tbselenium.tbdriver import TorBrowserDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s", datefmt="%Y/%m/%d %I:%M:%S %p")
logging.warning('Logging started.')

# Get user input
url = str(sys.argv[1])
username = str(sys.argv[2])
password = str(sys.argv[3])
tor_browser_path = str(sys.argv[4])


def scrape(url):
    # Run with the Tor browser
    with TorBrowserDriver(tor_browser_path) as driver:
        # Save the scraped file with time stamp and .html ending
        file_name = str("onion_site_scraped-" + str(datetime.datetime.now()) + ".html")

        # Download URL entered when starting the program
        f = open(file_name, "w")
        driver.get(url)

        # Tailored for White House Market
        elem = driver.find_element_by_name("username")
        elem.clear()
        elem.send_keys(username)

        # Wait 
        time.sleep((random.random() / 1.5) + (random.randint(0, 1) / 5))

        # Continue filling in the password 
        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys(password)

        # Wait and fill in CAPTCHA manually 
        time.sleep((random.random() / 5) + (random.randint(0, 1) / 5))
        elem.submit()

        # Wait
        time.sleep((random.random() / 1.5) + (random.randint(0, 1) / 5))

        # Print status
        print("Title: \n\n", driver.title, "\n\n", driver.current_url, "\n\nDone.\n")

        # Wait
        time.sleep(4)

        # Save the screenshot file with time stamp and .png ending
        screenshot_name = str("onion_site_screenshot-" + str(datetime.datetime.now()) + ".png")

        # Get screenshot
        driver.get_screenshot_as_file(screenshot_name)

        # Wait
        time.sleep(6)

        # Get all other links
        all_links = driver.find_elements_by_tag_name('a')
        logging.debug("All links: ", all_links)

        # Save images
        images = driver.find_elements_by_tag_name('img')
        time.sleep(10)

        # Write image data to local directory 
        output_dir = str("/tmp/" + url[7:]+ str(datetime.datetime.now()))
        os.makedirs(output_dir, 755)
        image_count=0
        for i in images:
            logging.debug("Image: ", i)
            urllib.request.urlretrieve(i.get_attribute('src'), output_dir + "-" + str(image_count)+'.jpg')
            image_count += 1

        # Write page source HTML to file
        # f.write(driver.page_source)
        f.close()

# Check if URLs are in a list or just a singlet
if(isfile(url)):
    for line in url:
        scrape(line)
else:
    scrape(url)
