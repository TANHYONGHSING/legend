import pymssql 

server = 'MSI' 
database = 'gudang_garam' 
username = 'sa' 
password = '12345678'

connection = pymssql.connect(server=server, database=database, user=username, password=password)
cursor = connection.cursor()
cursor.execute('SELECT * FROM product')

for row in cursor: 
    print(row)
