# Python Phase 1

## Objetivo

Este repositório contém os projetos desenvolvidos durante meus estudos da Fase 1 de Python, com foco na construção de habilidades práticas de programação e automação aplicáveis a ambientes de Cloud e Infraestrutura.

O objetivo desta fase não era me tornar um desenvolvedor Python, mas aprender Python como uma ferramenta prática para automação, processamento de dados, interação com APIs e tarefas relacionadas à infraestrutura.

## Projetos

### 01 — Relatório de Saúde de Servidores

Processa dados estruturados de servidores a partir de um arquivo JSON e gera um relatório de saúde contendo o status dos servidores, seus ambientes e os servidores que requerem atenção.

**Principais conceitos praticados:**

* Fundamentos de Python
* Listas e dicionários
* Estruturas de dados aninhadas
* JSON
* Manipulação de arquivos
* Processamento de dados

### 02 — Monitor de Saúde de API

Consome uma API HTTP, trata erros de requisição e HTTP, processa a resposta da API e gera um relatório de saúde.

**Principais conceitos praticados:**

* APIs HTTP / REST
* `requests`
* JSON
* YAML
* Tratamento de exceções
* Timeouts
* Arquivos de configuração

### 03 — Automação de Arquivos

Organiza automaticamente arquivos de acordo com suas extensões utilizando automação do sistema de arquivos com Python.

**Principais conceitos praticados:**

* `pathlib`
* Manipulação de arquivos e diretórios
* Extensões de arquivos
* Dicionários
* Estruturas condicionais
* Automação do sistema de arquivos

## Tecnologias Utilizadas

* Python
* JSON
* YAML
* APIs HTTP / REST
* Requests
* Pathlib
* Automação do sistema de arquivos
* Git & GitHub
* Linux / WSL

## Habilidades Demonstradas

* Fundamentos de Python
* Processamento de dados
* Trabalho com dados estruturados
* Manipulação de arquivos JSON
* Configuração utilizando YAML
* Consumo de APIs HTTP
* Tratamento de exceções
* Automação de arquivos e diretórios
* Funções e lógica reutilizável
* Automação básica voltada para infraestrutura
* Fluxo de trabalho com Git e GitHub

## Estrutura do Repositório

```text
python-phase1/
├── 01-server-health-report/
│   ├── servers.json
│   ├── server_report.py
│   └── report.json
│
├── 02-api-health-monitor/
│   ├── config.yaml
│   ├── api_monitor.py
│   └── health_report.json
│
├── 03_file_automation.dir/
│   ├── file_organizer.py
│   └── downloads/
│
└── README.md
```

## Abordagem de Aprendizagem

Os projetos deste repositório foram desenvolvidos de forma incremental, com cada projeto focado em diferentes capacidades de automação com Python.

Em vez de construir uma única aplicação grande e artificial, os projetos são intencionalmente pequenos e independentes. Isso permite praticar conceitos individualmente e, gradualmente, combiná-los em tarefas práticas de automação.

## Observações

* Este repositório representa a conclusão dos meus estudos iniciais de Python.
* Os projetos possuem foco educacional e não têm como objetivo representar sistemas prontos para produção.
* Python está sendo estudado como uma ferramenta para automação de Cloud e Infraestrutura.
* A próxima etapa do aprendizado será focada em tecnologias e conceitos mais diretamente relacionados a Cloud e Infraestrutura.
