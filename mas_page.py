# mas_page.py
from selenium.webdriver.common.by import By

class MASBookingPage:
    def __init__(self, driver):
        self.driver = driver
        # Simple, easy-to-explain element locators
        self.domestic_flight_radio = (By.ID, "domestic-flight")
        self.passenger_name_field  = (By.NAME, "firstName")
        self.insurance_checkbox    = (By.ID, "insurance-checkbox")
        self.total_price_label     = (By.CLASS_NAME, "grand-total")
        self.proceed_button        = (By.ID, "btn-proceed")

    def open_website(self):
        self.driver.get("https://www.malaysiaairlines.com/")

    def select_domestic(self):
        self.driver.find_element(*self.domestic_flight_radio).click()

    def enter_passenger_name(self, name):
        self.driver.find_element(*self.passenger_name_field).send_keys(name)

    def toggle_insurance(self):
        self.driver.find_element(*self.insurance_checkbox).click()

    def get_checkout_price(self):
        return self.driver.find_element(*self.total_price_label).text

    def click_next(self):
        self.driver.find_element(*self.proceed_button).click()