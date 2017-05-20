

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
from datetime import datetime


engine = create_engine('sqlite:///mytable.db', echo=True)

# https://www.pythonsheets.com/notes/python-sqlalchemy.html

class db_connect(object):
	def create_table(self):
		
		engine.execute('CREATE TABLE "EX1" ('
               'id INTEGER NOT NULL,'
               'name VARCHAR, '
               'PRIMARY KEY (id));')

	
	def input_data(self):

		engine.execute('INSERT INTO "EX1" '
               '(id, name) '
               'VALUES (4,"raw1")')

	def select_data(self):

		result = engine.execute('SELECT * FROM '
                        '"EX1"')
		for _r in result:
			print _r

	def delete_data(self):
		engine.execute('DELETE from "EX1" where id=3;')
		result = engine.execute('SELECT * FROM "EX1"')
		print result.fetchall()





#=========


#db_run = db_connect()
#db_run.create_table()
#db_run.input_data()
#db_run.delete_data()






