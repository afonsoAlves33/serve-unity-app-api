import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import urllib



SERVER = 'hololenstcc.database.windows.net'
DATABASE = 'free-sql-db'
USERNAME = 'sqlroot'
PASSWORD = 'Google.com'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
conn = pyodbc.connect(connectionString) 
cursor = conn.cursor()
cursor.execute("CREATE TABLE some_table (x int, y int))")
# params = urllib.parse.quote_plus \
# (r'Driver={ODBC Driver 18 for SQL Server};Server=tcp:hololenstcc.database.windows.net,1433;Database=free-sql-db;Uid=sqlroot;Pwd=Google.com;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
# conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
# engine_azure = create_engine(conn_str,echo=True)

# print('connection is ok')
# print(engine_azure)

# class User():
#     def __init__(self, nome, email) -> None:
#         self.nome = nome
#         self.email = email


# with engine_azure.connect() as conn:
#     conn.execute("CREATE TABLE some_table (x int, y int)")
#     conn.commit()

# with Session(engine_azure) as session:
#     patrick = User(nome="patrick", email="Patrick Star")
#     session.add_all([patrick])
#     session.commit()


