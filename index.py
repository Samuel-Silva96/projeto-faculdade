from matplotlib import pyplot as plt
import pandas as pd

# Carregar os dados
dados_csv = pd.read_csv('dataset.csv')


# Gráfico de barras
visitantes = dados_csv['VISITANTE'].value_counts().head(5)

plt.bar(visitantes.index, visitantes.values, color='blue')
plt.title('Top 5 Maiores Visitantes')
plt.xlabel('Times')
plt.ylabel('Quantidade de Jogos')

for i, valor in enumerate(visitantes.values):
    plt.text(i, valor + 0.1, str(valor), ha='center')
plt.show()


# Gráfico de Pizza - Distribuição dos Resultados
resultados = dados_csv['RESULTADO'].value_counts()

labels_pizza = resultados.index.map({'V': 'Vitória', 'E': 'Empate', 'D': 'Derrota'})

plt.pie(resultados.values, labels=labels_pizza, autopct='%1.1f%%', startangle=90, colors=['blue', 'yellow',  'red'])
plt.title('Distribuição dos Resultados')
plt.axis('equal')
plt.show()


# Histograma - Frequência dos gols do Corinthians
plt.hist(dados_csv['GOL COR'], bins=range(0, dados_csv['GOL COR'].max()+2), color='Blue', edgecolor='black')
plt.title('Frequência dos Gols do Corinthians')
plt.xlabel('Quantidade de Gols')
plt.ylabel('Frequência')
plt.grid(axis='y')
plt.show()