import pyodbc
server = 'athenahacks.database.windows.net'
database = 'athenahacks'
username = 'azureuser'
password = 'athenahacks!'   
driver= '{ODBC Driver 17 for SQL Server}'


# Server=tcp:athenahacks.database.windows.net,1433;Initial Catalog=athenahacks;Persist Security Info=False;User ID=azureuser;Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+db+';UID='+usern+';PWD='+pwd+'')
with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()