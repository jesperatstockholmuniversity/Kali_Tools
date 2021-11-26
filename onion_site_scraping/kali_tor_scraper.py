import sys
import tbselenium.common as cm
from os.path import isfile
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem

"""
STEM code
#tbb_dir = "/home/amoros/downloads/tor-browser_en-US/"
#tor_process = launch_tbb_tor_with_stem

#with TorBrowserDriver(tbb_dir, tor_cfg=cm.USE_STEM) as driver:
#    driver.load_url("https://check.torproject.org")

#tor_process.kill()
"""

# Read user input
user_input = str(sys.argv[1])

if(isfile(user_input)):
    print("")
else:
    print("Not a file ", type(user_input))

#url = str(sys.argv[1])

# Run with the Tor browser
with TorBrowserDriver("/home/kali/Downloads/tor-browser_en-US/") as driver:
    # Get URL 
    driver.get(url)
    source = driver.page_source

    # Print title in Terminal
    print("Title: \n\n", driver.title, "\n\n URL: ", driver.current_url, "Page source |\n\n", source)

    # Save screenshot
    driver.get_screenshot_as_file("onion_site_screenshot.png")

    # Write to file
    f = open("scraped_onion_site.html","w")
    f.write("DONE:")
    f.close

    # Quit
    driver.quit()
