import pandas as pd
import numpy as np
import statsmodels.api as sm
from sqlalchemy import create_engine

class AnaliseMateria:
    def __init__(self, user, password, host, database):
        self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

    def buscar_dados(self):
        query = """
        SELECT 
            s.nome_disciplina, 
            a.situacao_matricula, 
            s.status 
        FROM 
            semestres s 
        JOIN 
            alunos a ON s.aluno_id = a.id;
        """
        df = pd.read_sql(query, self.engine)
        return df

    def analisar_evasao_por_materia(self):
        dados = self.buscar_dados()

        dados['evadido'] = np.where(dados['situacao_matricula'] == 'Evasão', 1, 0)
        dados['reprovado'] = np.where(dados['status'].isin(['Reprovado', 'Rep. Falta']), 1, 0)

        taxa_reprovacao = dados.groupby('nome_disciplina')['reprovado'].mean().reset_index()
        taxa_reprovacao.columns = ['nome_disciplina', 'taxa_reprovacao']

        top20_disciplinas = taxa_reprovacao.nlargest(20, 'taxa_reprovacao')['nome_disciplina'].values
        print("Top 20 matérias com maior taxa de reprovação:", top20_disciplinas)

        top20_dados = dados[dados['nome_disciplina'].isin(top20_disciplinas)].copy()

        for disciplina in top20_disciplinas:
            top20_dados.loc[top20_dados['nome_disciplina'] == disciplina, disciplina] = top20_dados['reprovado']

        y = top20_dados['evadido']
        X = top20_dados[top20_disciplinas].fillna(0)

        X = sm.add_constant(X)

        model = sm.OLS(y, X).fit()

        print(model.summary())

if __name__ == "__main__":
    analise_materia = AnaliseMateria(user='root', password='root_dev_password', host='localhost', database='regressao')
    analise_materia.analisar_evasao_por_materia()
