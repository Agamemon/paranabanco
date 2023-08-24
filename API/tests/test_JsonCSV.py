import csv
import json
import os
import sys
import unittest
from datetime import datetime

from utils.api_client import APIClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = APIClient(base_url="https://jsonplaceholder.typicode.com")
        with open(os.path.join(os.path.dirname(__file__), '../data/test_data.json'), 'r') as json_file:
            cls.sample_json_data = json.load(json_file)

    def check_field(self, data, field_name, expected_type):
        # Verifica se um campo existe no dicionário de dados e se seu valor tem o tipo esperado.
        self.assertIn(field_name, data)
        field_value = data[field_name]
        self.assertIsInstance(field_value, expected_type)
        return f"'{field_name}' field is present and has a {expected_type.__name__} value: {field_value}"

    def check_address(self, address):
        # Verifica os campos do dicionário de endereço e do dicionário geo, se presentes.
        messages = []

        self.assertIsInstance(address, dict)
        messages.append("'address' field is a dictionary")

        messages.append(self.check_field(address, "street", str))
        messages.append(self.check_field(address, "suite", str))
        messages.append(self.check_field(address, "city", str))
        messages.append(self.check_field(address, "zipcode", str))

        geo = address.get("geo", {})
        self.assertIsInstance(geo, dict)
        messages.append("'geo' field is a dictionary")

        messages.append(self.check_field(geo, "lat", str))
        messages.append(self.check_field(geo, "lng", str))

        return messages

    def check_company(self, company):
        # Verifica os campos do dicionário da empresa.
        messages = []

        self.assertIsInstance(company, dict)
        messages.append("'company' field is a dictionary")

        messages.append(self.check_field(company, "name", str))
        messages.append(self.check_field(company, "catchPhrase", str))
        messages.append(self.check_field(company, "bs", str))

        return messages

    def save_to_csv(self, filename, data):
        # Salva os dados em um arquivo CSV usando um nome de arquivo único com a data.
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_filename = f"{filename}_{timestamp}.csv"
        unique_path = os.path.join(os.path.dirname(filename), unique_filename)

        with open(unique_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["CT", "Status", "Identificador", "Validador", "Info"])

            for row in data:
                ct = row[0]
                status = row[1]
                info_list = row[2].split("\n")[1:]
                for idx, info in enumerate(info_list):
                    identifier = info.split("'")[1] if "'" in info else ""
                    validator = info.split(":")[0].strip() if ":" in info else ""
                    info_content = info.split(":", 1)[1].strip() if ":" in info else ""

                    if idx == 0:
                        writer.writerow([ct, status, identifier, validator, info_content])
                    else:
                        writer.writerow(["", "", identifier, validator, info_content])

    def test_json_data(self):
        # Testa os dados JSON e salva os resultados em um arquivo CSV.
        results = []

        for entry in self.sample_json_data:
            entry_id = entry['id']
            validation = "PASSED"
            result_messages = []

            try:
                self.assertIsInstance(entry, dict)
                result_messages.append("Entry is a dictionary")

                result_messages.append(self.check_field(entry, "id", int))
                result_messages.append(self.check_field(entry, "name", str))
                result_messages.append(self.check_field(entry, "username", str))
                result_messages.append(self.check_field(entry, "email", str))
                result_messages.append(self.check_field(entry, "phone", str))
                result_messages.append(self.check_field(entry, "website", str))

                result_messages.extend(self.check_address(entry.get("address", {})))
                result_messages.extend(self.check_company(entry.get("company", {})))
            except AssertionError as e:
                validation = "FAILED"
                result_messages.append(str(e))

            results.append([entry_id, validation, "\n".join(result_messages)])

        result_dir = os.path.join(os.path.dirname(__file__), '../data/result')
        os.makedirs(result_dir, exist_ok=True)
        result_path = os.path.join(result_dir, "test_results.csv")
        self.save_to_csv(result_path, results)


if __name__ == "__main__":
    unittest.main()
