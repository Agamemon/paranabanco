# Paraná Banco - Projeto Case Teste

## Descrição

O projeto Paraná Banco é um case técnico que consiste nos seguintes pontos:

 - Estruturação e escrita dos cenários de teste (Verificar arquivo na raiz "Cases Tech - Paraná Banco.pdf")
 - Cenários e validações das automações propostas.
 - Utilização de padrões de projeto para as automações
 - Estruturação do projeto
 - Boas práticas de programaçãoa 

## Funcionalidades cobertas

- Teste de Interface Web
- Testes de API Integração

## Tecnologias Utilizadas

- Linguagem de Programação: Python
- Framework: Selenium e Unittest


## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/agamenon/paranabanco.git

2. Mapeamento de bibliotecas
  Seguir arquivo de requirements.txt

3. Execução dos testes:

  Testes de Interface web - executar classe ".\pages\ExecuteMainPage.py"

4. Testes de API Integração - executar as classe:
 #Validação dos métodos GET/PUT/DELETE ".\API\tests\API_Test_Runner.py"
 #Validação do método POST ".\API\tests\testes_endpointsPOST.py"
 #Validação dos métodos HTTP Code ".\API\tests\http_request_handler.py"
 #Validação do JSON Schema ".\API\tests\schemaJSON.py" e ".\API\tests\test_JsonCSV.py"
