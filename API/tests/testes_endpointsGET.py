import json
import os
import unittest
from datetime import datetime

import requests


class APITestGet(unittest.TestCase):
    base_url = "https://jsonplaceholder.typicode.com"
    endpoint = "/users"
    full_url = f"{base_url}{endpoint}"

    def test_get_users(self):
        response = requests.get(self.full_url)

        # Verifica se o código de status da resposta é 200 (OK)
        self.assertEqual(response.status_code, 200, "Código de status não é 200")

        # Verifica se a resposta não está vazia
        self.assertTrue(response.json(), "Resposta está vazia")

        # Corrige a formatação do JSON
        formatted_json = json.dumps(response.json(), indent=4)

        # Imprime o resultado na tela
        print(formatted_json)

        # Salva os dados coletados em um arquivo .txt
        directory = "../data/result"
        if not os.path.exists(directory):
            os.makedirs(directory)

        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"APITestGET_{current_time}.txt"
        file_path = os.path.join(directory, filename)

        with open(file_path, "w") as file:
            file.write(formatted_json)


if __name__ == "__main__":
    unittest.main()
