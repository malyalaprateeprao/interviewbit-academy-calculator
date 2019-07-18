import os

from flask import Flask
from flask import request
from flask import render_template
todo_store = {}
todo_store['depo']=['go for sleep','music']
todo_store['shivang']=['run','floc']

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def select_todos(name):
        global todo_store
        return todo_store[name]

    def insert_todos(name ,todo):
        global todo_store
        current_todos = todo_store[name]
        current_todos.append(todo)
        todo_store[name] = current_todos
        return
    def add_todo_by_name(name, todo):
        #call db function
        insert_todos(name,todo)
        return

    def get_todos_by_name(name):
        return select_todos(name)
   # a simple page that list my todos
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print(name)
        person_todo_list = get_todos_by_name(name)
        return render_template('todo_view.html',todos=person_todo_list)
    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        add_todo_by_name(name,todo)
        print(name)
        return 'added successfully'


    return app

