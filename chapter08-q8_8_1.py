
import sqlite3
db = 'test.db'
con = sqlite3.connect(db)
csr = con.cursor()

csr.execute('create table if not exists human (name, nickname);')

csr.execute("insert into human(name) values('Ichiro');")
csr.execute("insert into human(name) values('Jiro');")
csr.execute("insert into human(name) values('Saburo');")

csr.execute("update human set nickname = 'Lazer' where name = 'Ichiro';")

csr.execute("select * from human;")
print(csr.fetchall())

con.commit()
con.close()
