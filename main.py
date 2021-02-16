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

# Complete FGCU sign in form
def fgcu_sign_in_page(email, password):
    fgcu_email_input_element = driver.find_element_by_id("branding-username")
    fgcu_email_input_element.clear()
    fgcu_email_input_element.send_keys(email)

    fgcu_password_input_element = driver.find_element_by_id("branding-password")
    fgcu_password_input_element.clear()
    fgcu_password_input_element.send_keys(password)

    fgcu_submit_btn = driver.find_element_by_id("branding-sumbit-button")
    fgcu_submit_btn.click()


# Complete Veoci sign in form
def veoci_sign_in_page(email):
    veoci_email_input_element = driver.find_element_by_id("j_username")
    veoci_email_input_element.clear()
    veoci_email_input_element.send_keys(email)

    veoci_form_submit_btn = driver.find_element_by_xpath(
        '//*[@id="veoci-password-login"]/div/div[1]/input[2]'
    )
    veoci_form_submit_btn.click()

    fgcu_sign_in_email = "SIGN EMAIL"
    fgcu_sign_in_password = "SIGN PASSWORD"

    # Pause the program to allow the page to finish loading
    sleep(3)

    fgcu_sign_in_page(fgcu_sign_in_email, fgcu_sign_in_password)


veoci_sign_in_page("ENTER VEOCI SIGN EMAIL")
