import json
import os
from datetime import datetime

import requests


class APITestPut:

    def __init__(self, base_url):
        self.base_url = base_url
        self.results = []

    def run_tests(self):
        # Carregar o arquivo JSON com os dados para atualização
        data_file_path = os.path.join('..', 'data', 'dados.json')
        with open(data_file_path) as json_file:
            data = json.load(json_file)

        for item in data:
            user_id = item.get('id')
            url = f'{self.base_url}/{user_id}'

            response = self._send_put_request(url, item)
            self.results.append(response)

        self._print_results()
        self._save_to_file()

    def _send_put_request(self, url, data):
        response = requests.put(url, json=data)
        return {
            'url': url,
            'status_code': response.status_code,
            'response_data': response.json()
        }

    def _print_results(self):
        for result in self.results:
            print(f"URL: {result['url']}")
            print(f"Status Code: {result['status_code']}")
            print(f"Response Data: {result['response_data']}")
            print("=" * 50)

    def _save_to_file(self):
        result_dir = '../data/result'
        os.makedirs(result_dir, exist_ok=True)

        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"APITestPUT_{now}.txt"
        file_path = os.path.join(result_dir, filename)

        with open(file_path, 'w') as file:
            for result in self.results:
                file.write(f"URL: {result['url']}\n")
                file.write(f"Status Code: {result['status_code']}\n")
                file.write(f"Response Data: {result['response_data']}\n")
                file.write("=" * 50 + "\n")


if __name__ == "__main__":
    api_test = APITestPut('https://jsonplaceholder.typicode.com/users')
    api_test.run_tests()
