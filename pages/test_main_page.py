from selenium import webdriver

from canvas_element import CanvasElement  # Substitua pelo nome do arquivo onde a classe CanvasElement está definida


class CanvasExecutor:
    def __init__(self, driver):
        self.driver = driver

    def run_canvas_highlight(self):
        canvas_element = CanvasElement(self.driver)

        # Acessa a página da web
        url = "https://the-internet.herokuapp.com/challenging_dom"  # Substitua pela URL real
        self.driver.get(url)

        # Chama o método para destacar o elemento canvas e tirar um screenshot
        canvas_element.highlight_canvas_element()

    def close_driver(self):
        # Fecha o navegador
        self.driver.quit()

if __name__ == "__main__":
    # Configurações do Selenium e do WebDriver (neste caso, Chrome)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Inicia a janela do navegador maximizada
    driver = webdriver.Chrome(options=options)

    # Inicializa a classe CanvasExecutor
    canvas_executor = CanvasExecutor(driver)

    # Executa a ação de destacar o elemento canvas
    canvas_executor.run_canvas_highlight()

    # Fecha o navegador
    canvas_executor.close_driver()
