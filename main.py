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


def submit_daily_screening():
    sleep(30)

    daily_screening_submit_btn = driver.find_elements_by_xpath(
        '//*[@id="app"]/div/main/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/button'
    )[0]
    daily_screening_submit_btn.click()

    return driver.quit()


def fill_input_element(element, input_text):
    element.clear()
    element.send_keys(input_text)


def fgcu_sign_in_page(email, password):
    sleep(10)

    fgcu_email_input_element = driver.find_element_by_id("branding-username")
    fill_input_element(fgcu_email_input_element, email)

    fgcu_password_input_element = driver.find_element_by_id("branding-password")
    fill_input_element(fgcu_password_input_element, password)

    fgcu_submit_btn = driver.find_element_by_id("branding-sumbit-button")
    fgcu_submit_btn.click()

    return submit_daily_screening()


def veoci_sign_in_page(email):
    veoci_email_input_element = driver.find_element_by_id("j_username")
    fill_input_element(veoci_email_input_element, email)

    veoci_form_submit_btn = driver.find_element_by_xpath(
        '//*[@id="veoci-password-login"]/div/div[1]/input[2]'
    )
    veoci_form_submit_btn.click()

    fgcu_sign_in_email = "SIGN EMAIL"
    fgcu_sign_in_password = "SIGN PASSWORD"

    return fgcu_sign_in_page(fgcu_sign_in_email, fgcu_sign_in_password)


veoci_sign_in_page("ENTER VEOCI SIGN EMAIL")
