

from flask import Flask, request
from flask_restful import Resource, Api, reqparse,fields, marshal_with, abort
from collections import OrderedDict




app = Flask(__name__)
api = Api(app)


#================================


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}



#================================

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        print ('request = ', request)
        print ('todos[todo_id] = ' , todos[todo_id])
        return {todo_id: todos[todo_id]}


#================================

#parser = reqparse.RequestParser()
#parser.add_argument('rate', type=int, help='Rate to charge for this resource')
#args = parser.parse_args()


################  ################
#================================



resource_fields = { 'task':   fields.String,
				    'uri':    fields.Url('todo_ep')}

class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'

class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')

#================================



TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201



#================================



api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/todo/<string:todo_id>', endpoint='todo_ep')
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


#================================



if __name__ == '__main__':
    app.run(debug=True, port=9999)







