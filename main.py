#%%
import pandas as pd
import json

# %%
with open('../json_to_excel/data/running_store.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
# %%
linhas = []
# %%

for marca in data['Loja']['Marcas']:
    id_marca = marca.get('Marca', None)
    categorias = marca.get('Categoria', [])

    for categoria in categorias:
        id_categoria = categoria.get('idSubCategoria', None)
        tamanhos = categoria.get('Tamanhos', [])

        for tamanho in tamanhos:
            linhas.append({
                'Marca': id_marca,
                'SubCategoria': id_categoria,
                'Tamanho': tamanho.get('Tamanho'),
                'Quantidade de Compras': tamanho.get('quantidadeCompras'),
                'Preço da Unidade': tamanho.get('precoUnitario'),
                                     
            })
# %%
relatorio_vendas = pd.DataFrame(linhas)
# %%
relatorio_vendas = relatorio_vendas[['Marca', 'SubCategoria', 'Tamanho', 'Quantidade de Compras', 'Preço da Unidade']]
# %%
relatorio_vendas['Marca'] = relatorio_vendas['Marca'].astype('str')
relatorio_vendas['SubCategoria'] = relatorio_vendas['SubCategoria'].astype('str')
relatorio_vendas['Tamanho'] = relatorio_vendas['Tamanho'].astype('str')
relatorio_vendas['Quantidade de Compras'] = relatorio_vendas['Quantidade de Compras'].astype('Int64')
relatorio_vendas['Preço da Unidade'] = relatorio_vendas['Preço da Unidade'].astype('float')

#%%
relatorio_vendas = relatorio_vendas.sort_values(by='Marca', ascending=True)

# %%
relatorio_vendas.to_excel('../json_to_excel/exportados/relatorio_vendas.xlsx', index=False)

