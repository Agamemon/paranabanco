import datetime
import json
import os

import requests


class APITestDelete:
    def __init__(self, base_url):
        self.base_url = base_url
        self.initial_data = None
        self.results = []

    def get_initial_data(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            self.initial_data = response.json()

    def run_tests(self):
        self.get_initial_data()
        if self.initial_data is None:
            print("Failed to fetch initial data.")
            return

        for item in self.initial_data:
            user_id = item['id']
            delete_response = self.delete_user(user_id)
            self.record_result(delete_response, user_id)

        self.save_results()

    def delete_user(self, user_id):
        delete_url = f"{self.base_url}/{user_id}"
        response = requests.delete(delete_url)
        return response

    def record_result(self, response, user_id):
        result = {
            "user_id": user_id,
            "status_code": response.status_code,
            "response_text": response.text
        }
        self.results.append(result)

    def save_results(self):
        if not os.path.exists("../data/result"):
            os.makedirs("../data/result")

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"APITestDELETE_{timestamp}.txt"
        file_path = os.path.join("../data/result", file_name)

        with open(file_path, "w") as file:
            file.write("Initial Data:\n")
            file.write(json.dumps(self.initial_data, indent=2))
            file.write("\n\n")

            for result in self.results:
                file.write("User ID: {}\n".format(result["user_id"]))
                file.write("Status Code: {}\n".format(result["status_code"]))
                file.write("Response:\n")
                file.write(result["response_text"])
                file.write("\n")
                file.write("=" * 30)
                file.write("\n\n")


if __name__ == "__main__":
    tester = APITestDelete("https://jsonplaceholder.typicode.com/users")
    tester.run_tests()
