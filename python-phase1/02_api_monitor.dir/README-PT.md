# Monitor de Saúde de API

## Objetivo

Este projeto foi desenvolvido para praticar automação com Python através do consumo de uma API HTTP, tratamento de erros de requisição, processamento da resposta da API e geração de um relatório de saúde em formato JSON.

O projeto simula uma tarefa simples de monitoramento de API, utilizando Python para verificar se uma API está respondendo corretamente e registrar informações básicas sobre sua resposta.

## O que o Script faz

- Lê as configurações da API a partir do arquivo `config.yaml`.
- Obtém a URL da API e o tempo limite da requisição a partir da configuração.
- Envia uma requisição GET para a API configurada.
- Trata erros de timeout, HTTP e requisições em geral.
- Valida o status da resposta HTTP.
- Processa a resposta JSON retornada pela API.
- Determina se a API está saudável ou não saudável.
- Registra o código de status HTTP.
- Conta a quantidade de itens retornados pela API.
- Gera um relatório estruturado de saúde.
- Salva o relatório no arquivo `health_report.json`.

## Tecnologias Utilizadas

- Python
- Requests
- YAML
- JSON
- HTTP / REST API
- Manipulação de arquivos
- Tratamento de exceções
- Git & GitHub

## Como usar

1. Clone o repositório:
```
git clone https://github.com/voncod/python-phase1/new/main/python-phase1/01_server_health_report.dir
cd python-phase1
```
2. Acesse o diretório do projeto:
```
cd 02-api-health-monitor
```
3. Instale as dependências necessárias:
```
pip install requests pyyaml
```
4. Execute o script:
```
python api_monitor.py
```
5. O relatório de saúde gerado será salvo como:
```
health_report.json
```

## Exemplo de Saída

```
{
    "url": "https://jsonplaceholder.typicode.com/posts",
    "status": "healthy",
    "http_status": 200,
    "items_received": 100
}
```

## Estrutura do Projeto

```
├── config.yaml
├── api_monitor.py
└── health_report.json
```

## Objetivos de Aprendizagem

- Praticar o consumo de APIs HTTP com Python.
- Utilizar a biblioteca requests para realizar requisições GET.
- Configurar informações de uma API utilizando YAML.
- Processar respostas em formato JSON.
- Tratar exceções relacionadas a HTTP e requisições.
- Utilizar timeouts em requisições HTTP.
- Modificar e gerar dicionários estruturados.
- Gerar um relatório simples de saúde a partir de dados de uma API.
- Praticar conceitos de automação relevantes para Cloud e Infraestrutura.

## Observações

- Este é um projeto de aprendizado focado em automação com Python e monitoramento básico de APIs.
- O objetivo era construir uma solução funcional e compreensível, e não um sistema de monitoramento pronto para produção.
- O projeto representa uma etapa inicial no uso de Python para automatizar tarefas relacionadas a Cloud, APIs e Infraestrutura.
