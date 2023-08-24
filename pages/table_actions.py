import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TableActions:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_dir = os.path.join(os.getcwd(), "screenshots")

    def acessar_pagina(self, url):
        self.driver.get(url)  # Acessa a página da web

    def encontrar_edit_delete(self):
        wait = WebDriverWait(self.driver, 10)  # Initialize WebDriverWait

        # Wait for the table to be present
        tabela = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".large-10.columns table")))

        linhas = tabela.find_elements(By.TAG_NAME, "tr")  # Encontra todas as linhas da tabela

        for index, linha in enumerate(linhas, start=1):
            celulas = linha.find_elements(By.TAG_NAME, "td")  # Encontra as células (colunas) da linha

            for celula in celulas:
                links = celula.find_elements(By.TAG_NAME, "a")  # Encontra os links dentro da célula

                for link in links:
                    link_text = link.text.lower()  # Convert link text to lowercase
                    if link_text == "edit" or link_text == "delete":
                        print(link_text, ":", link.get_attribute("href"))  # Imprime o texto e o link

                        # Destacar elemento
                        self.driver.execute_script("arguments[0].style.border='2px solid red'", link)

                        # Capturar screenshot
                        screenshot_name = f"linha{index}_{link_text}.png"
                        screenshot_path = os.path.join(self.screenshot_dir, screenshot_name)
                        self.driver.save_screenshot(screenshot_path)

                        # Remover o destaque
                        self.driver.execute_script("arguments[0].style.border=''", link)
