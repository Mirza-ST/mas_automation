# test_insurance.py
import time
from selenium import webdriver
from mas_page import MASBookingPage

def test_insurance_updates_total_price():
    # 1. Start the Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10) # Simple fallback wait to ensure elements load

    # 2. Instantiate our simple Page Object
    booking_page = MASBookingPage(driver)

    # 3. Simple execution steps
    booking_page.open_website()
    booking_page.select_domestic()
    booking_page.enter_passenger_name("John Doe")

    # Record baseline ticket pricing
    original_price = booking_page.get_checkout_price()

    # Opt-in to Allianz Travel Insurance
    booking_page.toggle_insurance()
    time.sleep(2) # Brief explicit wait to let UI recalculate dynamically

    # Record updated checkout pricing
    updated_price = booking_page.get_checkout_price()

    # 4. Assert / Verify the total increased
    assert original_price != updated_price, "Error: Booking summary price did not change after selecting insurance!"
    print("Test Passed: Total price updated successfully upon insurance selection.")

    # 5. Move forward to payment entry point
    booking_page.click_next()

    # Wrap up execution
    driver.quit()

# Run the test
if __name__ == "__main__":
    test_insurance_updates_total_price()