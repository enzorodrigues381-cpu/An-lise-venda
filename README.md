# Análise de Vendas 🐍📊

Projeto Python para análise de dados de vendas, desenvolvido como demonstração de habilidades em ciência de dados.

## O que o projeto faz

- Lê dados de vendas de um arquivo CSV
- Calcula estatísticas: receita total, ticket médio, ranking de vendedores
- Gera 4 gráficos automáticos (barras, pizza, linha, comparativo)
- Salva os gráficos em um arquivo PNG

## Como executar

### 1. Instalar dependências

```bash
pip install pandas matplotlib
```

### 2. Rodar o script

```bash
python analise_vendas.py
```

## Estrutura dos arquivos

```
data-analyzer/
├── analise_vendas.py   # Script principal
├── vendas.csv          # Dados de exemplo (30 registros)
└── README.md           # Este arquivo
```

## Bibliotecas utilizadas

| Biblioteca   | Para que serve                          |
|--------------|-----------------------------------------|
| `pandas`     | Leitura do CSV e análise dos dados      |
| `matplotlib` | Criação dos gráficos                    |

## Exemplo de saída

```
=======================================================
       ANÁLISE DE VENDAS - RELATÓRIO COMPLETO
=======================================================

✔  Dados carregados: 30 registros encontrados.
   Período: 05/01/2024 a 25/03/2024

-------------------------------------------------------
  RESUMO GERAL
-------------------------------------------------------
  Receita total:        R$ 163.983,00
  Total de itens vendidos: 347
  Ticket médio por venda:  R$ 5.466,10
  Produto mais caro:       Notebook
```
