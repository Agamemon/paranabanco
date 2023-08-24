import datetime
import os

from selenium.webdriver.common.by import By


class CanvasElement:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_dir = os.path.join(os.getcwd(), "screenshots")

    def highlight_canvas_element(self):
        canvas = self.driver.find_element(By.ID, "canvas")  # Encontra o elemento canvas

        # Destacar o elemento com uma borda vermelha
        self.driver.execute_script("arguments[0].style.border='2px solid red'", canvas)

        # Capturar screenshot
        screenshot_name = "canvas_highlight.png"
        screenshot_path = os.path.join(self.screenshot_dir, screenshot_name)
        self.driver.save_screenshot(screenshot_path)

        # Imprimir informações sobre o elemento
        print("Informações do Elemento Canvas:")
        print(f"Tag: {canvas.tag_name}")
        print(f"ID: {canvas.get_attribute('id')}")
        print(f"Classe: {canvas.get_attribute('class')}")
        print(f"Estilo: {canvas.get_attribute('style')}")

        # Criar um nome para o arquivo de texto com base na data atual
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        txt_filename = f"canvas_info_{canvas.get_attribute('id')}_{current_date}.txt"
        txt_path = os.path.join(self.screenshot_dir, txt_filename)

        # Gravar informações sobre o elemento no arquivo de texto
        with open(txt_path, "w") as txt_file:
            txt_file.write("Informações do Elemento Canvas:\n")
            txt_file.write(f"Tag: {canvas.tag_name}\n")
            txt_file.write(f"ID: {canvas.get_attribute('id')}\n")
            txt_file.write(f"Classe: {canvas.get_attribute('class')}\n")
            txt_file.write(f"Estilo: {canvas.get_attribute('style')}\n")

        # Remover o destaque
        self.driver.execute_script("arguments[0].style.border=''", canvas)