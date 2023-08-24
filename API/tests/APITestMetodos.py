import json
import os
from datetime import datetime

import requests


class APITestPost:

    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.result_data = []

    def run_create_tests(self, data_list):
        for data in data_list:
            response = self._send_post_request(data)
            self.result_data.append(response.json())

    def run_get_tests(self):
        response = requests.get(self.endpoint)
        self.result_data.append(response.json())

    def run_update_tests(self, user_id, updated_data):
        update_endpoint = f"{self.endpoint}/{user_id}"
        response = self._send_put_request(update_endpoint, updated_data)
        self.result_data.append(response.json())

    def run_delete_tests(self, user_id):
        delete_endpoint = f"{self.endpoint}/{user_id}"
        response = self._send_delete_request(delete_endpoint)
        self.result_data.append(response.status_code)

    def _send_post_request(self, data):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.endpoint, data=json.dumps(data), headers=headers)
        return response

    def _send_put_request(self, endpoint, data):
        headers = {'Content-Type': 'application/json'}
        response = requests.put(endpoint, data=json.dumps(data), headers=headers)
        return response

    def _send_delete_request(self, endpoint):
        response = requests.delete(endpoint)
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

    # Example JSON data list for create tests
    create_test_data = [
        {"name": "John Doe", "username": "johndoe", "email": "johndoe@example.com"},
        {"name": "Jane Smith", "username": "janesmith", "email": "janesmith@example.com"}
        # Add more test data as needed
    ]

    # Example user ID and data for update tests
    user_id_to_update = 1
    updated_user_data = {"name": "Updated Name"}

    # Example user ID for delete tests
    user_id_to_delete = 1

    api_test.run_create_tests(create_test_data)
    api_test.run_get_tests()
    api_test.run_update_tests(user_id_to_update, updated_user_data)
    api_test.run_delete_tests(user_id_to_delete)

    api_test.print_results()
    api_test.save_results_to_file()
