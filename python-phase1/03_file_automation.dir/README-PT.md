# Automação de Arquivos

## Objetivo

Este projeto foi desenvolvido para praticar automação com Python através da organização de arquivos em um diretório de acordo com suas extensões.

O projeto simula uma tarefa simples de automação do sistema de arquivos, utilizando Python para identificar os tipos de arquivos, criar diretórios por categoria e mover os arquivos automaticamente.

## O que o Script faz

- Percorre o diretório `downloads`.
- Ignora diretórios.
- Identifica as extensões dos arquivos.
- Converte as extensões para letras minúsculas para garantir um processamento consistente.
- Categoriza tipos de arquivos conhecidos utilizando um dicionário.
- Cria os diretórios das categorias quando necessário.
- Move os arquivos para os respectivos diretórios.
- Move tipos de arquivos não cadastrados para o diretório `others`.
- Mantém os nomes originais dos arquivos ao movê-los.

## Tecnologias Utilizadas

- Python
- `pathlib`
- Automação do sistema de arquivos
- Dicionários
- Loops e estruturas condicionais
- Git & GitHub

## Como Usar

1. Clone o repositório:
```
git clone https://github.com/voncod/python-phase1/new/main/python-phase1/01_server_health_report.dir
cd python-phase1
```
2. Acesse o diretório do projeto:
```
cd 03_file_automation.dir
```
3. Coloque os arquivos que deseja organizar dentro do diretório downloads.

4. Execute o script:
```
python file_organizer.py
```
5. O script criará automaticamente os diretórios das categorias necessárias e moverá os arquivos.

## Exemplo de Saída

Antes de executar o script:
```
downloads/
├── foto.jpg
├── documento.pdf
├── script.py
├── dados.json
├── notas.txt
└── musica.mp3
```
Depois de executar o script:
```
downloads/
├── images/
│   └── foto.jpg
├── documents/
│   ├── documento.pdf
│   └── notas.txt
├── python/
│   └── script.py
├── json/
│   └── dados.json
└── others/
    └── musica.mp3
```
## Estrutura do Projeto
```
03_file_automation.dir/
├── file_organizer.py
└── downloads/
    ├── images/
    ├── documents/
    ├── python/
    ├── json/
    └── others/
```
## Objetivos de Aprendizagem

- Praticar automação do sistema de arquivos com Python.
- Utilizar pathlib para trabalhar com arquivos e diretórios.
- Percorrer o conteúdo de diretórios.
- Verificar se um caminho representa um arquivo.
- Extrair e normalizar extensões de arquivos.
- Utilizar dicionários para mapear extensões para categorias.
- Criar diretórios programaticamente.
- Mover arquivos utilizando Python.
- Praticar conceitos de automação relevantes para Cloud e Infraestrutura.

## Observações

- Este é um projeto de aprendizado focado em automação com Python e manipulação do sistema de arquivos.
- O objetivo era construir uma solução funcional e compreensível, e não um sistema de gerenciamento de arquivos pronto para produção.
- O projeto representa uma etapa inicial no uso de Python como ferramenta de automação para tarefas de Cloud e Infraestrutura.
