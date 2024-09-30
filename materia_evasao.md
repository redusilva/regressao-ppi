# Análise de Evasão por Matéria

## Resultados da Análise

### Top 20 Matérias com Maior Taxa de Reprovação

O script identificou as 20 disciplinas com as maiores taxas de reprovação. Essas disciplinas são:

1. Cálculo Diferencial e Integral I
2. Fundamentos de Cálculo
3. Geometria Analítica
4. Transformações Químicas
5. Leitura e Produção Textual de Gêneros Acadêmicos
6. P.C C. II - Processos Educacionais e Cultura
7. Cálculo Integral e Diferencial I
8. Estrutura e Propriedades da Matéria
9. Língua Portuguesa
10. Física Geral II
11. Introdução às Práticas de Laboratório
12. Laboratório de Química Analítica I
13. P.C C. I - Ciência e Linguagem
14. Políticas da Educação
15. Química Inorgânica II
16. Tecnologias da Informação e Comunicação
17. Filosofia da Educação
18. Instrumentação para o Ensino de Química
19. Química Analítica II
20. Físico Química I

### Resultados da Regressão Linear

A tabela abaixo resume os resultados da regressão linear:

| Regressor                                         | Coeficiente | Erro Padrão | Valor t  | p-valor  |
|---------------------------------------------------|-------------|-------------|----------|----------|
| const                                             | 0.5172      | 0.031       | 16.928   | 0.000    |
| Cálculo Diferencial e Integral I                  | 0.4828      | 0.466       | 1.035    | 0.301    |
| Fundamentos de Cálculo                            | 0.4828      | 0.235       | 2.057    | 0.040    |
| Geometria Analítica                               | 0.3063      | 0.117       | 2.619    | 0.009    |
| Transformações Químicas                           | 0.3249      | 0.111       | 2.925    | 0.004    |
| Leitura e Produção Textual de Gêneros Acadêmicos | 0.1494      | 0.270       | 0.553    | 0.581    |
| P.C C. II - Processos Educacionais e Cultura     | -0.1839     | 0.270       | -0.680   | 0.497    |
| Cálculo Integral e Diferencial I                  | 0.4113      | 0.128       | 3.212    | 0.001    |
| Estrutura e Propriedades da Matéria               | 0.3578      | 0.120       | 2.974    | 0.003    |
| Língua Portuguesa                                 | 0.3918      | 0.144       | 2.729    | 0.007    |
| Física Geral II                                   | 0.4828      | 0.330       | 1.461    | 0.145    |
| Introdução às Práticas de Laboratório            | -0.5172     | 0.330       | -1.565   | 0.119    |
| Laboratório de Química Analítica I               | -0.5172     | 0.330       | -1.565   | 0.119    |
| P.C C. I - Ciência e Linguagem                   | -0.0172     | 0.330       | -0.052   | 0.958    |
| Políticas da Educação                             | -0.0172     | 0.330       | -0.052   | 0.958    |
| Química Inorgânica II                             | -0.0172     | 0.330       | -0.052   | 0.958    |
| Tecnologias da Informação e Comunicação           | -0.5172     | 0.330       | -1.565   | 0.119    |
| Filosofia da Educação                             | 0.3918      | 0.144       | 2.729    | 0.007    |
| Instrumentação para o Ensino de Química          | -0.0172     | 0.330       | -0.052   | 0.958    |
| Química Analítica II                              | -0.0172     | 0.330       | -0.052   | 0.958    |
| Físico Química I                                  | 0.4828      | 0.466       | 1.035    | 0.301    |

### Interpretação dos Resultados

- **Coeficiente**: Representa a mudança esperada na variável dependente (`evadido`) para cada unidade de mudança na variável independente (disciplinas). Um coeficiente positivo indica que, à medida que a taxa de reprovação aumenta, a probabilidade de evasão também aumenta.
- **Erro Padrão**: Medida da precisão dos coeficientes estimados. Valores menores indicam estimativas mais precisas.
- **Valor t**: Testa a hipótese de que o coeficiente é diferente de zero. Um valor t alto indica que o coeficiente é significativamente diferente de zero.
- **p-valor**: Indica a significância estatística. Um p-valor menor que 0.05 sugere que o coeficiente é estatisticamente significativo.

### Resumo dos Principais Resultados

- As disciplinas **Fundamentos de Cálculo**, **Geometria Analítica** e **Transformações Químicas** apresentaram coeficientes significativos e positivos, indicando uma relação entre alta taxa de reprovação e evasão dos alunos.
- O modelo geral apresentou um **R² de 0.145**, indicando que aproximadamente 14.5% da variação na evasão pode ser explicada pelas disciplinas consideradas.
- O **p-valor global do modelo** é muito baixo (7.99e-05), indicando que pelo menos uma das variáveis independentes é significativamente diferente de zero.

## Conclusão

A análise sugere que certas disciplinas têm um impacto significativo na evasão dos alunos. A identificação dessas matérias pode ajudar na implementação de estratégias de intervenção para reduzir as taxas de evasão, como tutorias ou suporte acadêmico específico.
