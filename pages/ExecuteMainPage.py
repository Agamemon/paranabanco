from selenium import webdriver

from canvas_element import CanvasElement
from left_buttons import LeftButtons
from main_page import MainPage
from table_actions import TableActions


class ExecuteMainPage:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

    def close_driver(self):
        self.driver.quit()

    def main_page_close(self):
        main_page = MainPage(self.driver)
        main_page.close_page()

    def left_buttons (self):
        main_page = MainPage(self.driver)
        left_buttons_tester = LeftButtons(main_page)  # Pass the instance of MainPage here
        left_buttons_tester.test_left_buttons()

    def table_actions(self):
        main_page = MainPage(self.driver)
        table_actions = TableActions(self.driver)
        table_actions.acessar_pagina(main_page.url)  # Use main_page.url
        table_actions.encontrar_edit_delete()

    def run_canvas_highlight(self):
        canvas_element = CanvasElement(self.driver)
        canvas_element.highlight_canvas_element()

if __name__ == "__main__":
    execution_main_page = ExecuteMainPage()
    try:
        execution_main_page.left_buttons()
        execution_main_page.table_actions()
        execution_main_page.run_canvas_highlight()
        execution_main_page.main_page_close()
    finally:
        execution_main_page.close_driver()
