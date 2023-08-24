import unittest

from testes_endpointsDELETE import APITestDelete
from testes_endpointsGET import APITestGet
from testes_endpointsPUT import APITestPut


class APITestRunner:
    def __init__(self, base_url):
        self.base_url = base_url

    def execute_get(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(APITestGet)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def execute_put(self):
        api_test = APITestPut(self.base_url)
        api_test.run_tests()

    def execute_delete(self):
        tester = APITestDelete(self.base_url)
        tester.run_tests()

if __name__ == "__main__":
    executor = APITestRunner("https://jsonplaceholder.typicode.com/users")

    executor.execute_get()
    executor.execute_put()
    executor.execute_delete()
