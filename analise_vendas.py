"""
Análise de Vendas - Projeto Python para Análise de Dados
=========================================================
Esse script lê um arquivo CSV de vendas, calcula estatísticas
importantes e gera gráficos para facilitar a tomada de decisão.

Bibliotecas utilizadas:
- pandas: manipulação e análise de dados
- matplotlib: criação de gráficos
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

# ──────────────────────────────────────────
# 1. CARREGAR OS DADOS
# ──────────────────────────────────────────

print("=" * 55)
print("       ANÁLISE DE VENDAS - RELATÓRIO COMPLETO")
print("=" * 55)

df = pd.read_csv("vendas.csv")

# Converter coluna de data para o tipo correto
df["data"] = pd.to_datetime(df["data"])

# Calcular o valor total de cada venda
df["valor_total"] = df["quantidade"] * df["preco_unitario"]

print(f"\n✔  Dados carregados: {len(df)} registros encontrados.")
print(f"   Período: {df['data'].min().strftime('%d/%m/%Y')} a {df['data'].max().strftime('%d/%m/%Y')}")


# ──────────────────────────────────────────
# 2. RESUMO GERAL
# ──────────────────────────────────────────

print("\n" + "─" * 55)
print("  RESUMO GERAL")
print("─" * 55)

receita_total      = df["valor_total"].sum()
total_itens        = df["quantidade"].sum()
ticket_medio       = receita_total / len(df)
produto_mais_caro  = df.loc[df["preco_unitario"].idxmax(), "produto"]

print(f"  Receita total:        R$ {receita_total:,.2f}")
print(f"  Total de itens vendidos: {total_itens}")
print(f"  Ticket médio por venda:  R$ {ticket_medio:,.2f}")
print(f"  Produto mais caro:       {produto_mais_caro}")


# ──────────────────────────────────────────
# 3. ANÁLISE POR CATEGORIA
# ──────────────────────────────────────────

print("\n" + "─" * 55)
print("  RECEITA POR CATEGORIA")
print("─" * 55)

por_categoria = (
    df.groupby("categoria")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

for categoria, valor in por_categoria.items():
    barra = "█" * int(valor / 5000)
    print(f"  {categoria:<18} R$ {valor:>10,.2f}  {barra}")


# ──────────────────────────────────────────
# 4. ANÁLISE POR VENDEDOR
# ──────────────────────────────────────────

print("\n" + "─" * 55)
print("  RANKING DE VENDEDORES")
print("─" * 55)

por_vendedor = (
    df.groupby("vendedor")["valor_total"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

for posicao, row in por_vendedor.iterrows():
    medalha = ["🥇", "🥈", "🥉"][posicao] if posicao < 3 else "  "
    print(f"  {medalha} {posicao + 1}º {row['vendedor']:<15} R$ {row['valor_total']:,.2f}")


# ──────────────────────────────────────────
# 5. EVOLUÇÃO MENSAL
# ──────────────────────────────────────────

print("\n" + "─" * 55)
print("  RECEITA MENSAL")
print("─" * 55)

df["mes"] = df["data"].dt.to_period("M")
por_mes = df.groupby("mes")["valor_total"].sum()

for mes, valor in por_mes.items():
    print(f"  {str(mes):<10}  R$ {valor:,.2f}")


# ──────────────────────────────────────────
# 6. GRÁFICOS
# ──────────────────────────────────────────

print("\n" + "─" * 55)
print("  Gerando gráficos...")
print("─" * 55)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Análise de Vendas 2024", fontsize=16, fontweight="bold", y=1.01)

cores = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2"]

# --- Gráfico 1: Receita por categoria (barras horizontais) ---
ax1 = axes[0, 0]
por_categoria.plot(kind="barh", ax=ax1, color=cores[:len(por_categoria)])
ax1.set_title("Receita por Categoria", fontweight="bold")
ax1.set_xlabel("Receita (R$)")
ax1.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"R$ {x:,.0f}"))
ax1.invert_yaxis()
ax1.grid(axis="x", alpha=0.3)

# --- Gráfico 2: Participação por categoria (pizza) ---
ax2 = axes[0, 1]
por_categoria.plot(kind="pie", ax=ax2, autopct="%1.1f%%", colors=cores, startangle=90)
ax2.set_title("Participação por Categoria", fontweight="bold")
ax2.set_ylabel("")

# --- Gráfico 3: Receita mensal (linha) ---
ax3 = axes[1, 0]
meses_str = [str(m) for m in por_mes.index]
ax3.plot(meses_str, por_mes.values, marker="o", linewidth=2.5,
         color="#4C72B0", markersize=8, markerfacecolor="white", markeredgewidth=2.5)
ax3.fill_between(meses_str, por_mes.values, alpha=0.15, color="#4C72B0")
ax3.set_title("Evolução da Receita Mensal", fontweight="bold")
ax3.set_xlabel("Mês")
ax3.set_ylabel("Receita (R$)")
ax3.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"R$ {x:,.0f}"))
ax3.grid(alpha=0.3)

# --- Gráfico 4: Comparativo de vendedores (barras) ---
ax4 = axes[1, 1]
ax4.bar(por_vendedor["vendedor"], por_vendedor["valor_total"],
        color=cores[:len(por_vendedor)])
ax4.set_title("Receita por Vendedor", fontweight="bold")
ax4.set_xlabel("Vendedor")
ax4.set_ylabel("Receita (R$)")
ax4.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"R$ {x:,.0f}"))
ax4.grid(axis="y", alpha=0.3)

plt.tight_layout()

# Salvar os gráficos em um arquivo PNG
nome_arquivo = "graficos_vendas.png"
plt.savefig(nome_arquivo, dpi=150, bbox_inches="tight")
print(f"\n  ✔  Gráficos salvos em: {nome_arquivo}")

plt.show()

print("\n" + "=" * 55)
print("  Análise concluída com sucesso!")
print("=" * 55 + "\n")
