# Paraná Banco - Projeto Case Teste

## Descrição
O projeto Paraná Banco consiste em um case técnico que abrange os seguintes aspectos:

- Estruturação e redação de cenários de teste (consulte o arquivo "Cases Tech - Paraná Banco.pdf" na raiz)
- Criação de cenários e validações para as automações propostas
- Utilização de padrões de projeto para a automação
- Organização do projeto
- Implementação de boas práticas de programação

## Funcionalidades Cobertas
O projeto abrange testes nas seguintes áreas:

- Testes de Interface Web
- Testes de Integração de API

## Tecnologias Utilizadas
O projeto foi desenvolvido utilizando as seguintes tecnologias:

- Linguagem de Programação: Python
- Frameworks: Selenium e Unittest

## Instalação
Siga os passos abaixo para configurar e executar o projeto:

1. Clone este repositório:

```
git clone https://github.com/agamenon/paranabanco.git
```

2. Instale as bibliotecas necessárias a partir do arquivo `requirements.txt`:

```
pip install -r requirements.txt
```

## Execução dos Testes

### Testes de Interface Web
Para executar os testes de interface web, rode a classe:

```
.\pages\ExecuteMainPage.py
```

### Testes de Integração de API
Para executar os testes de integração de API, rode as classes correspondentes:

- Validação dos métodos GET/PUT/DELETE: `.\API\tests\API_Test_Runner.py`
- Validação do método POST: `.\API\tests\testes_endpointsPOST.py`
- Validação dos métodos HTTP Code: `.\API\tests\http_request_handler.py`
- Validação do JSON Schema: `.\API\tests\schemaJSON.py` e `.\API\tests\test_JsonCSV.py`

Certifique-se de seguir essas instruções para uma configuração adequada e bem-sucedida do projeto de teste Paraná Banco. Em caso de dúvidas ou problemas, consulte a documentação ou entre em contato com a equipe responsável pelo projeto.
