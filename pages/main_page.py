from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/challenging_dom"
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self):
        self.driver.get(self.url)

    def find_element_by_xpath_with_wait(self, xpath):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def highlight_element(self, element):
        self.driver.execute_script("arguments[0].style.border = '3px solid red'", element)

    def remove_highlight(self, element):
        self.driver.execute_script("arguments[0].style.border = ''", element)

    def take_screenshot(self, element_xpath):
        element_name = element_xpath.replace("/", "_").replace("[@", "_").replace("]", "").replace("(", "").replace(")", "")
        screenshot_path = f"screenshots/screenshot_{element_name}.png"
        self.driver.save_screenshot(screenshot_path)

    def close_page(self):
        self.driver.quit()

