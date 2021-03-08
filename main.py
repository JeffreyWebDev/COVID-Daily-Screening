from selenium import webdriver
import socket
from time import sleep

driver = None

webdriver_path = input("Please enter your webdriver path: ")

while driver is None:

    try:
        # Path to browser webdriver
        PATH = webdriver_path

        # Allow browser to automate task without window pop-up
        browser_option = webdriver.ChromeOptions()
        # browser_option.add_argument("headless")

        # Launch starting webpage
        driver = webdriver.Chrome(PATH, options=browser_option)
        driver.get("https://veoci.com/veoci/134376/processes/236235613/invocations")
    except Exception as err:
        print(
            "Path not found, visit https://sites.google.com/a/chromium.org/chromedriver/home for more information"
        )
        webdriver_path = input("Please enter your webdriver path: ")
        driver = None


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


def veoci_sign_in_page():
    veoci_email = input("Please input Veoci email: ")

    veoci_email_input_element = driver.find_element_by_id("j_username")
    fill_input_element(veoci_email_input_element, veoci_email)

    veoci_form_submit_btn = driver.find_element_by_xpath(
        '//*[@id="veoci-password-login"]/div/div[1]/input[2]'
    )
    veoci_form_submit_btn.click()

    sleep(2)

    invalid_email = driver.find_element_by_xpath(
        '//*[@id="login-user-summary"]/div[2]/strong'
    )

    while invalid_email:
        veoci_email = input("Please input Veoci email: ")

        veoci_email_input_element = driver.find_element_by_id("j_username")
        fill_input_element(veoci_email_input_element, veoci_email)

        veoci_form_submit_btn = driver.find_element_by_xpath(
            '//*[@id="veoci-password-login"]/div/div[1]/input[2]'
        )
        veoci_form_submit_btn.click()

        sleep(2)

        invalid_email = driver.find_element_by_xpath(
            '//*[@id="login-user-summary"]/div[2]/strong'
        )

    fgcu_sign_in_email = input("FGCU login email: ")
    fgcu_sign_in_password = input("FGCU login password: ")

    return fgcu_sign_in_page(fgcu_sign_in_email, fgcu_sign_in_password)


IPaddress = socket.gethostbyname(socket.gethostname())

if IPaddress == "127.0.0.1":
    print("No Internet connection")
    quit()
else:
    veoci_sign_in_page()

