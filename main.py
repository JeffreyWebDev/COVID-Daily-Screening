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

# Complete Veoci sign in form
def veoci_sign_in_page(email):
    veoci_email_input_element = driver.find_element_by_id("j_username")
    veoci_email_input_element.clear()
    veoci_email_input_element.send_keys(email)

    veoci_form_submit_btn = driver.find_element_by_xpath(
        '//*[@id="veoci-password-login"]/div/div[1]/input[2]'
    )
    veoci_form_submit_btn.click()

    return sleep(3)


veoci_sign_in_page("ENTER VEOCI SIGN EMAIL")
