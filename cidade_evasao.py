import numpy as np
import statsmodels.api as sm
import pandas as pd
import pymysql

class AnaliseEvasaoCidade:
    def __init__(self, host, user, password, db):
        self.conexao = pymysql.connect(host=host, user=user, password=password, database=db)
        
    def buscar_dados(self):
        query = """
        SELECT a.situacao_matricula, a.cidade
        FROM alunos a
        """
        return pd.read_sql(query, self.conexao)
    
    def analisar_evasao_por_cidade(self):
        dados = self.buscar_dados()

        dados['evadido'] = np.where(dados['situacao_matricula'] == 'Evasão', 1, 0)

        dados_one_hot = pd.get_dummies(dados['cidade'], prefix='cidade')

        dados = pd.concat([dados, dados_one_hot], axis=1)

        y = dados['evadido'].astype(float)
        X = dados_one_hot.astype(float)

        X = sm.add_constant(X)

        model = sm.OLS(y, X).fit()

        print(model.summary())

        evasao_por_cidade = dados.groupby('cidade')['evadido'].mean() * 100
        print("Taxa de evasão por cidade:")
        print(evasao_por_cidade)
        return evasao_por_cidade

# Exemplo de uso
analise = AnaliseEvasaoCidade(host='localhost', user='root', password='root_dev_password', db='regressao')
evasao_por_cidade = analise.analisar_evasao_por_cidade()
