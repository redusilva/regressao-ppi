import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root_dev_password",
    database="regressao"
)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM alunos")
resultado = cursor.fetchall()

print('alunos: ', resultado)

cursor.execute("SELECT * FROM semestres")
resultado = cursor.fetchall()

print('\n\nsemestres: ', resultado)

cursor.close()
conexao.close()