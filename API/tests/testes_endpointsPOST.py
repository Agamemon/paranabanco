import json
import os
from datetime import datetime

import requests


class APITestPost:

    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.result_data = []

    def run_tests(self, data_list):
        for data in data_list:
            response = self._send_post_request(data)
            self.result_data.append(response.json())

    def _send_post_request(self, data):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.endpoint, data=json.dumps(data), headers=headers)
        return response

    def print_results(self):
        for idx, result in enumerate(self.result_data):
            print(f"Test Result {idx + 1}: {result}")

    def save_results_to_file(self):
        result_dir = '../data/result'
        os.makedirs(result_dir, exist_ok=True)

        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"APITestPOST_{now}.txt"
        file_path = os.path.join(result_dir, filename)

        with open(file_path, 'w') as file:
            for result in self.result_data:
                file.write(f"Response Data: {json.dumps(result, indent=2)}\n")
                file.write("=" * 50 + "\n")

        print(f"Results saved to {file_path}")

if __name__ == '__main__':
    api_test = APITestPost('https://jsonplaceholder.typicode.com/users')

    # Example JSON data list for testing
    test_data_list = [
        {"name": "John Doe", "username": "johndoe", "email": "johndoe@example.com"},
        {"name": "Jane Smith", "username": "janesmith", "email": "janesmith@example.com"}
        # Add more test data as needed
    ]

    api_test.run_tests(test_data_list)
    api_test.print_results()
    api_test.save_results_to_file()
