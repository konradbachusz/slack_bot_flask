# -*- coding: utf-8 -*-


from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps



# ref https://impythonist.wordpress.com/2015/07/12/build-an-api-under-30-lines-of-code-with-python-and-flask/

e = create_engine('sqlite:///movie_metadata.db')

app = Flask(__name__)
api = Api(app)

# Get 
#=======================================


class Director_Meta(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select distinct director_name from movie")
        return {'departments': [i[0] for i in query.cursor.fetchall()]}

class Country_imdb_meta(Resource):
    def get(self, country_name):
        conn = e.connect()
        query = conn.execute("select * from movie where country='%s'"%country_name)

        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result


class Sample_movie_meta(Resource):
    def get(self, limit_count):
        conn = e.connect()
        query = conn.execute("select * from movie limit '%s'"%limit_count)
        print query 

        result = {'meta_data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

# Delete
#=======================================

# http://blog.cloudoki.com/getting-started-with-restful-apis-using-the-flask-microframework-for-python/
# http://www.bradcypert.com/writing-a-restful-api-in-flask-sqlalchemy/


#class delete_movie_data(Resource):
#    def delete(self, movie_name):
#        conn = e.connect()
#        query = conn.execute("delete from movie where movie_title = '%s'"%movie_name)
#        conn.commit()
#        result = conn.execute("select count(*) from movie")
#        return result 


#@app.route('/delete_movie/<string:movie_name>', methods = ['DELETE'])
#def delete(self, movie_name):
#        conn = e.connect()
#        #del_st = user_t.delete().where(user_t.c.l_name == 'Hello')    
#        conn.delete(movie_title == 'Tangled')  
#        conn.execute() 
#
#        result = conn.execute("select count(*) from movie")
#        return result 

#=======================================



 
api.add_resource(Director_Meta, '/Director_Meta')
api.add_resource(Country_imdb_meta, '/countryname/<string:country_name>')
api.add_resource(Sample_movie_meta, '/moviedata/<string:limit_count>')

#api.add_resource(delete_movie_data, '/delete_movie/<string:movie_name>')






if __name__ == '__main__':
     app.run(debug=True, port=7778)






