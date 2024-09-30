# Análise de Evasão por Semestre

## Resultados da Análise

### Resumo da Regressão Linear

O modelo de regressão linear foi ajustado para analisar a relação entre o tempo (representado pelo semestre) e a taxa de evasão. A seguir, apresentamos um resumo dos resultados da regressão:

| **Estatística**                | **Valor**      |
|---------------------------------|----------------|
| **R-squared**                   | 0.887          |
| **Adj. R-squared**              | 0.871          |
| **F-statistic**                 | 54.78          |
| **Prob (F-statistic)**          | 0.000149       |
| **Log-Likelihood**              | -32.103        |
| **Número de Observações**       | 9              |
| **AIC**                         | 68.21          |
| **BIC**                         | 68.60          |
| **Df Residuals**                | 7              |
| **Df Model**                    | 1              |

### Coeficientes do Modelo

| **Regressor** | **Coeficiente** | **Erro Padrão** | **t**      | **p-valor**  | **Intervalo 95%**       |
|---------------|------------------|------------------|------------|---------------|--------------------------|
| const         | 147.9111         | 5.972            | 24.769     | 0.000         | [133.791, 162.031]      |
| x1            | -9.2833          | 1.254            | -7.401     | 0.000         | [-12.249, -6.317]       |

### Interpretação dos Resultados

- **R-squared**: O valor de 0.887 indica que aproximadamente 88.7% da variação na taxa de evasão é explicada pelo modelo. Este é um alto nível de explicabilidade.
  
- **Coeficientes**:
  - O coeficiente **const** (147.9111) representa a taxa de evasão média quando o semestre é zero (o que não é aplicável na prática, mas é parte do modelo).
  - O coeficiente de **x1** (-9.2833) indica que, para cada aumento de um semestre, a taxa de evasão diminui em média 9.28%. Esse valor é altamente significativo (p-valor < 0.001).

### Análise da Taxa de Evasão por Semestre

A tabela a seguir apresenta a taxa de evasão calculada para cada semestre:

| **Semestre** | **Taxa de Evasão (%)** |
|--------------|--------------------------|
| 1.0          | 15.95                    |
| 8.0          | 14.04                    |
| 4.0          | 11.43                    |
| 2.0          | 11.23                    |
| 3.0          | 11.13                    |
| 7.0          | 10.73                    |
| 6.0          | 9.53                     |
| 5.0          | 9.43                     |
| NaN          | 6.52                     |

### Observações

- A taxa de evasão é mais alta no **primeiro semestre** (15.95%), o que pode sugerir que os alunos enfrentam dificuldades ao iniciar o curso.
- A taxa de evasão diminui gradualmente nos semestres subsequentes, o que pode indicar uma adaptação dos alunos ao ambiente acadêmico.
- A presença de um valor NaN na tabela de semestres indica que há um semestre em que não foram registradas evasões.

## Conclusão

Os resultados sugerem que há uma tendência de diminuição da evasão à medida que os semestres avançam. Isso pode fornecer informações valiosas para a implementação de medidas de suporte para os alunos nos primeiros semestres, onde a taxa de evasão é mais crítica.
