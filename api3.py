# -*- coding: utf-8 -*-


from flask import Flask, request,jsonify,abort,request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from sqlalchemy.orm import sessionmaker
import jsonify





# https://impythonist.wordpress.com/2015/07/12/build-an-api-under-30-lines-of-code-with-python-and-flask/

e = create_engine('sqlite:///movie_metadata.db')

# http://docs.sqlalchemy.org/en/latest/orm/session_basics.html
Session = sessionmaker(bind=e)
session = Session()

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



@app.route('/del/<string:country_name>', methods=['GET','POST','DELETE'])
### NEED TO INCLUDE GET, POST method as well when uding DELETE or other  REST command
### https://www.youtube.com/watch?v=q5rIxpE3fjA
def deleteProduct(country_name):
    print ('start')
    conn = e.connect()
    conn.execute("delete from movie where country ='%s' "%country_name)
    session.commit()
    print ('Delete success!')
    return "OK delete country data done"


#class delete_country_data(Resource):
#    def delete(self, country_name):
#        print ('start')
#        conn = e.connect()
#        conn.execute("delete from movie where country = '%s'"%country_name)
#        session.commit()
#       #result = conn.execute("select count(*) from movie")
#        return jsonify( { 'result': True } )
 

#=======================================



 
api.add_resource(Director_Meta, '/Director_Meta')
api.add_resource(Country_imdb_meta, '/countryname/<string:country_name>')
api.add_resource(Sample_movie_meta, '/moviedata/<string:limit_count>')

#api.add_resource(delete_country_data, '/delete_country/<string:country_name>')






if __name__ == '__main__':
     app.run(debug=True, port=7778)






