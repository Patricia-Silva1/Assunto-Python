#
# Tests BD usando SQLite / DBeaver
# 
from sqlite3 import connect

# Replace username with your own A2 Hosting account username:
conexao = connect('/home/eduardo/snap/dbeaver-ce/147/.local/share/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db')
cursor = conexao.cursor()

cursor.execute("select * from Artist a where a.ArtistId < 20;")
for col1, col2 in cursor.fetchall():
    print(col1, col2)

conexao.close()