from selenium import webdriver
from time import sleep

# Path to browser webdriver
PATH = "INSERT BROWSER WEBDRIVER PATH"

# Allow browser to automate task without window pop-up
browser_option = webdriver.ChromeOptions()
browser_option.add_argument("headless")

# Launch starting webpage
driver = webdriver.Chrome(PATH, options=browser_option)
driver.get("https://veoci.com/veoci/134376/processes/236235613/invocations")
