# mas_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MASBookingPage:
    def __init__(self, driver):
        self.driver = driver
        # Clean, explicit element locators [cite: 138]
        self.domestic_flight_radio = (By.ID, "domestic-flight")
        self.passenger_name_field  = (By.NAME, "firstName")
        self.insurance_checkbox    = (By.ID, "insurance-checkbox")
        self.total_price_label     = (By.CLASS_NAME, "grand-total")
        self.proceed_button        = (By.ID, "btn-proceed")

    def open_website(self):
        self.driver.get("https://www.malaysiaairlines.com/") [cite: 146]

    def select_domestic(self):
        # Principal Correction: Wait explicitly until the element is clickable
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.domestic_flight_radio)).click()

    def enter_passenger_name(self, name):
        # Principal Correction: Wait until field is visible
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_to_be_clickable(self.passenger_name_field))
        element.send_keys(name)

    def toggle_insurance(self):
        # Principal Correction: Scroll element into view before clicking to prevent overlay issues
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.insurance_checkbox))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def get_checkout_price(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_to_be_clickable(self.total_price_label))
        return element.text

    def click_next(self):
        self.driver.find_element(*self.proceed_button).click() [cite: 146]