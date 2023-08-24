import os
from datetime import datetime

import requests
from jsonschema import validate, exceptions


class UserEndpointValidator:
    def __init__(self, url):
        self.url = url

    def get_users(self):
        response = requests.get(self.url)
        response_data = response.json()
        return response_data

    def print_validation_error(self, file, index, entry, validation_error):
        with open(file, 'a') as f:
            f.write(f"Validation Error in Entry {index}:\n")
            f.write(f"    Entry: {entry}\n")
            f.write("    Path: -> ".join(str(path) for path in validation_error.path) + "\n")
            f.write(f"    Message: {validation_error.message}\n\n")

    def print_validation_success(self, file, success_count, validated_entries):
        with open(file, 'a') as f:
            f.write(f"Validated {success_count} entries successfully.\n")
            f.write("Validated Entries:\n")
            for index, entry in validated_entries:
                f.write(f"Entry {index}: {entry}\n")
            f.write("\n")

    def validate_users(self, data, schema):
        success_count = 0
        validated_entries = []
        errors = []

        for index, entry in enumerate(data):
            try:
                validate(instance=entry, schema=schema)
                success_count += 1
                validated_entries.append((index, entry))
            except exceptions.ValidationError as e:
                errors.append((index, entry, e))

        return success_count, validated_entries, errors

    def validate_endpoint(self, schema):
        users_data = self.get_users()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        result_dir = "../data/result"
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)
        result_file = os.path.join(result_dir, f"{self.__class__.__name__}_{timestamp}.txt")

        success_count, validated_entries, validation_errors = self.validate_users(users_data, schema)

        if success_count > 0:
            self.print_validation_success(result_file, success_count, validated_entries)

        if validation_errors:
            with open(result_file, 'a') as f:
                f.write(f"Failed to validate {len(validation_errors)} entries:\n")
                for index, entry, validation_error in validation_errors:
                    self.print_validation_error(result_file, index, entry, validation_error)

if __name__ == "__main__":
    endpoint_url = "https://jsonplaceholder.typicode.com/users"

    def user_schema():
        return {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "username": {"type": "string"},
                "email": {"type": "string"},
                "address": {"type": "object"},
                "phone": {"type": "string"},
                "website": {"type": "string"},
                "company": {"type": "object"}
            },
            "required": ["id", "name", "username", "email", "address", "phone", "website", "company"]
        }

    validator = UserEndpointValidator(endpoint_url)
    validator.validate_endpoint(user_schema())
