from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LeftButtons:
    def __init__(self, main_page_instance):
        self.main_page = main_page_instance

    def test_left_buttons(self):
        self.main_page.open_page()

        xpath_list = [
            "//div[@id='content']/div/div/div/div/a",
            "//div[@id='content']/div/div/div/div/a[2]",
            "//div[@id='content']/div/div/div/div/a[3]"
        ]

        wait = WebDriverWait(self.main_page.driver, 10)

        for xpath in xpath_list:
            try:
                element = self.main_page.find_element_by_xpath_with_wait(xpath)
                print(f"Element found using xpath: {xpath}")
                self.main_page.highlight_element(element)  # Highlight the element
                self.main_page.take_screenshot(xpath)  # Take a screenshot
                self.main_page.remove_highlight(element)  # Remove the highlight

                wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

            except NoSuchElementException as e:
                print(f"Element not found using xpath: {xpath}")
                print(f"Error: {e}")


