import datetime
import os

import requests


class HTTPRequestHandler:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, endpoint, method="GET", data=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, json=data, headers=headers)
        return response

    @staticmethod
    def classify_status_code(status_code):
        status_classes = {
            1: "Informacional",
            2: "Sucesso",
            3: "Redirecionamento",
            4: "Erro do cliente",
            5: "Erro do servidor"
        }

        class_code = status_code // 100
        return status_classes.get(class_code, "Classe desconhecida")

    def handle_response(self, response):
        status_code = response.status_code
        status_class = self.classify_status_code(status_code)
        response_data = response.json() if response.content else None

        result_info = {
            "status_code": status_code,
            "status_class": status_class,
            "response_data": response_data
        }

        if 200 <= status_code < 300:
            print("Resposta da Requisição:", result_info)
            return result_info
        elif status_code == 400:
            raise ValueError("Solicitação inválida - Bad Request")
        elif status_code == 401:
            raise PermissionError("Não autorizado - Unauthorized")
        elif status_code == 403:
            raise PermissionError("Acesso proibido - Forbidden")
        elif status_code == 404:
            raise LookupError("Recurso não encontrado - Not Found")
        elif status_code == 500:
            raise RuntimeError("Erro interno do servidor - Internal Server Error")
        else:
            raise RuntimeError(f"Erro desconhecido com código de status: {status_code}")

    def log_result(self, result):
        log_dir = "../data/result"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        now = datetime.datetime.now()
        file_name = f"request_handler_{now.strftime('%Y%m%d_%H%M%S')}.txt"
        file_path = os.path.join(log_dir, file_name)

        with open(file_path, "w") as f:
            f.write(result)

        print(f"Resultado gravado em '{file_path}'")

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    handler = HTTPRequestHandler(base_url)

    try:
        response = handler.make_request("posts")
        result_info = handler.handle_response(response)
        formatted_result = str(result_info).replace(",", ",\n")  # Quebra a linha a cada vírgula
        print("Informações da Resposta:\n", formatted_result)
        result_text = f"Informações da Resposta:\n{formatted_result}"
        handler.log_result(result_text)
    except (ValueError, PermissionError, LookupError, RuntimeError) as e:
        error_message = f"Ocorreu um erro: {e}"
        print(error_message)
        handler.log_result(error_message)
