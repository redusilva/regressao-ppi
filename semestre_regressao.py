import numpy as np
import statsmodels.api as sm
import pandas as pd
from sqlalchemy import create_engine

# Constantes
COLUNA_SEMESTRE = 'semestre'
COLUNA_TOTAL_EVASAO = 'total_evasao'

class AnaliseEvasaoSemestre:
    def __init__(self, host, user, password, db):
        self.engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")
        
    def buscar_dados(self):
        """
        Método responsável por buscar os dados de evasão por semestre.
        """
        
        query = f"""
        SELECT 
            s.{COLUNA_SEMESTRE}, 
            COUNT(a.id) AS {COLUNA_TOTAL_EVASAO}
        FROM 
            semestres s
        JOIN 
            alunos a ON s.aluno_id = a.id
        WHERE 
            a.situacao_matricula = 'Evasão'
        GROUP BY 
            s.{COLUNA_SEMESTRE}  
        ORDER BY {COLUNA_TOTAL_EVASAO} DESC
        """
        return pd.read_sql(query, self.engine)
    
    def analisar_evasao_por_semestre(self):
        """
        Método que realiza a análise da evasão por semestre.
        """
        
        dados = self.buscar_dados()

        if dados.empty:
            print("Nenhum dado de evasão encontrado.")
            return pd.Series()

        y = dados[COLUNA_TOTAL_EVASAO].astype(float) 
        X = np.arange(len(dados))

        X = sm.add_constant(X)

        model = sm.OLS(y, X).fit()

        print(model.summary())

        dados['taxa_evasao'] = (dados[COLUNA_TOTAL_EVASAO] / dados[COLUNA_TOTAL_EVASAO].sum()) * 100
        print("Taxa de evasão por semestre:")
        print(dados[[COLUNA_SEMESTRE, 'taxa_evasao']])
        return dados[[COLUNA_SEMESTRE, 'taxa_evasao']]

if __name__ == "__main__":
    analise = AnaliseEvasaoSemestre(host='localhost', user='root', password='root_dev_password', db='regressao')
    evasao_por_semestre = analise.analisar_evasao_por_semestre()
