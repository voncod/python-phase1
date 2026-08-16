# Relatório de Saúde de Servidores

## Objetivo

Este projeto foi desenvolvido para praticar fundamentos de Python através do processamento de dados estruturados de servidores e da geração de um relatório de saúde em formato JSON.

O projeto simula uma tarefa simples de inventário e geração de relatórios de infraestrutura, utilizando Python para analisar o status e os ambientes dos servidores.

## O que o Script faz

- Lê os dados dos servidores a partir do arquivo `servers.json`.
- Conta o número total de servidores.
- Conta os servidores online e offline.
- Agrupa os servidores por ambiente (`prod`, `dev`, etc.).
- Cria uma lista de servidores online contendo nome e ambiente.
- Cria uma lista de servidores que requerem atenção.
- Gera um relatório estruturado de saúde dos servidores.
- Salva o relatório final no arquivo `report.json`.

## Tecnologias Utilizadas

- Python
- JSON
- Manipulação de arquivos
- Listas e dicionários
- Git & GitHub

## Como Usar
1. Clone o repositório:

```
git clone https://github.com/voncod/python-phase1/new/main/python-phase1/01_server_health_report.dir
cd python-phase1
```

2. Execute o script:
```
python server_report.py
```

3. O relatório gerado será salvo como:
```
report.json
```
## Exemplo de Saída
```
{
    "total_servers": 6,
    "online_servers": 4,
    "offline_servers": 2,
    "by_environment": {
        "prod": 4,
        "dev": 2
    },
    "online_servers_list": [
        {
            "name": "web-01",
            "environment": "prod"
        },
        {
            "name": "db-01",
            "environment": "prod"
        }
    ],
    "attention_required_list": [
        {
            "name": "web-02",
            "reason": "offline"
        }
    ]
}
```
## Estrutura do Projeto
```
├── servers.json
├── server_report.py
└── report.json
```

## Objetivos de Aprendizagem

- Praticar fundamentos de Python.
- Trabalhar com listas e dicionários.
- Processar dados estruturados em JSON.
- Ler e escrever arquivos JSON.
- Construir estruturas de dados aninhadas.
- Utilizar loops e condicionais para analisar dados.
- Gerar relatórios estruturados a partir de dados processados.
- Praticar conceitos básicos de automação relacionados a dados de infraestrutura.

## Observações

- Este é um projeto de aprendizado focado nos fundamentos de Python e automação.
- O objetivo era construir uma solução funcional e compreensível, e não uma solução otimizada para produção.
- O projeto representa uma etapa inicial no uso de Python como ferramenta de automação para tarefas de Cloud e Infraestrutura.
