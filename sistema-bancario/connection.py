import mysql.connector

con = mysql.connector.connect(host='localhost', database='SGB', user='root', password='1234')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySql versão ", db_info)
    cursor = con.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)

# if con.is_connected():
#     cursor.close()
#     con.close()
#     print("Conexão ao MySQl foi encerrada")