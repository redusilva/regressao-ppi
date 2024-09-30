# Análise de Evasão por Cidade

## Descrição do Projeto

Este projeto visa analisar a taxa de evasão de alunos em diferentes cidades, utilizando um modelo de regressão linear. A análise busca identificar se há uma relação significativa entre a cidade dos alunos e a sua situação de matrícula (evadido ou não evadido).

## Estrutura do Código

O código está organizado na classe `AnaliseEvasaoCidade`, que possui as seguintes funções:

- **`__init__`**: Construtor que estabelece a conexão com o banco de dados.
- **`buscar_dados`**: Realiza uma consulta SQL para buscar os dados de alunos, incluindo a situação da matrícula e a cidade.
- **`analisar_evasao_por_cidade`**: Processa os dados, realiza a análise de regressão e imprime os resultados.

## Análise de Regressão

### Dados

A análise utiliza os seguintes dados:
- `situacao_matricula`: Estado da matrícula do aluno (ex: 'Evasão' ou 'Ativo').
- `cidade`: Nome da cidade onde o aluno reside.

### Transformação dos Dados

- A situação da matrícula é transformada em uma variável binária chamada `evadido`, onde `1` representa que o aluno evadiu e `0` representa que não evadiu.
- A coluna `cidade` é convertida em variáveis binárias usando One-Hot Encoding, criando colunas separadas para cada cidade.

### Resultados do Modelo

O modelo de regressão linear é ajustado utilizando a variável dependente `evadido` e as variáveis independentes correspondentes às cidades. Os resultados do modelo são os seguintes:

- **R² (R-squared)**: O valor obtido foi de **0.174**, indicando que o modelo explica apenas **17,4%** da variância na taxa de evasão. Isso sugere que outros fatores que não estão sendo considerados podem influenciar a evasão.
  
- **P-Valor (Prob (F-statistic))**: Um p-valor de **0.624** indica que o modelo global não é estatisticamente significativo, sugerindo que não há evidências suficientes para concluir que as cidades têm um impacto significativo na evasão.
  
- **Coeficientes**: Os coeficientes das variáveis das cidades são todos insignificantes (p > 0.05), indicando que não há uma relação clara entre a cidade e a evasão.

### Taxa de Evasão por Cidade

As taxas de evasão por cidade foram calculadas e são as seguintes:

| Cidade                          | Taxa de Evasão (%) |
|---------------------------------|---------------------|
| Aparecida de Goiânia - GO      | 100.0               |
| Araú - GO                      | 0.0                 |
| Caturai - GO                   | 50.0                |
| Goianira - GO                  | 75.0                |
| Goiânia - GO                   | 0.0                 |
| Inhumas - GO                   | 50.0                |
| Taquaral de Goiás - GO         | 100.0               |

## Conclusões e Sugestões

1. **Revisão do Modelo**: Considere incluir mais variáveis independentes que possam influenciar a evasão, como desempenho acadêmico, histórico financeiro, apoio familiar, etc.
  
2. **Transformação dos Dados**: Verifique se os dados estão bem balanceados entre as cidades, pois a predominância de algumas cidades pode afetar a robustez do modelo.
  
3. **Alternativas de Modelagem**: Considere experimentar outras técnicas de modelagem, como regressão logística, que pode ser mais apropriada para problemas de classificação binária (evadido/não evadido).
  
4. **Exploração de Dados**: Realize uma análise exploratória de dados (EDA) mais profunda para entender os fatores que podem estar contribuindo para a evasão.
  
5. **Validação do Modelo**: Valide o modelo usando métodos de validação cruzada para garantir que os resultados sejam robustos.

## Como Executar

Para executar a análise, certifique-se de ter as seguintes dependências instaladas:

- `numpy`
- `pandas`
- `statsmodels`
- `pymysql`

### Exemplo de Uso

```python
analise = AnaliseEvasaoCidade(host='localhost', user='root', password='root_dev_password', db='regressao')
evasao_por_cidade = analise.analisar_evasao_por_cidade()
