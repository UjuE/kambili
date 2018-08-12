import json
import os

import jsonpickle as jsonpickle
from flask import Flask
from flask_restful import Resource, Api

from libs.datasource import MenuDataSource
from libs.kamrie import Kamrie

app = Flask(__name__)
api = Api(app)
kamrie = Kamrie(MenuDataSource(user=os.getenv('NEO_4J_USERNAME', 'Not found'),
                               password=os.getenv('NEO_4J_PASSWORD', 'Not found'),
                               host=os.getenv('NEO_4J_URL', 'Not found'),
                               port=os.getenv('NEO_4J_BOLT_PORT', 'Not found')))


class Menus(Resource):
    def get(self):
        weekMenu = kamrie.generate_week_menu()
        return json.loads(jsonpickle.encode(weekMenu, keys=True,  unpicklable=False))


api.add_resource(Menus, '/menus')

if __name__ == '__main__':
    app.run(debug=True)
