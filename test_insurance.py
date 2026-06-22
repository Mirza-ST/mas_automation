# test_insurance.py
import time
from selenium import webdriver
from mas_page import MASBookingPage

def test_insurance_updates_total_price():
    # 1. Start Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # 2. Instantiate our Page Object [cite: 146]
        booking_page = MASBookingPage(driver)

        # 3. Simple execution steps [cite: 146]
        booking_page.open_website() [cite: 146]
        booking_page.select_domestic()
        booking_page.enter_passenger_name("John Doe") [cite: 146]

        # Record baseline ticket pricing [cite: 146]
        original_price = booking_page.get_checkout_price()

        # Opt-in to Allianz Travel Insurance [cite: 146]
        booking_page.toggle_insurance()
        time.sleep(2)  # Give the UI 2 seconds to calculate the new price [cite: 146]

        # Record updated checkout pricing [cite: 146]
        updated_price = booking_page.get_checkout_price()

        # 4. Assert / Verify the total increased [cite: 146]
        assert original_price != updated_price, "Error: Booking summary price did not change after selecting insurance!" [cite: 146]
        print("Test Passed: Total price updated successfully upon insurance selection.") [cite: 146]

        # 5. Move forward to payment entry point [cite: 146]
        booking_page.click_next()

    except Exception as e:
        print(f"Test Failed due to error: {e}")

    finally:
        # 6. Always close the browser safely [cite: 146]
        driver.quit()

if __name__ == "__main__":
    test_insurance_updates_total_price()