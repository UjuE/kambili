import json
import os

import jsonpickle as jsonpickle

from .weekplandataaccess import WeekMenuDataAccess
from .menudatasource import MenuDataSource
from flask import Flask
from flask_restful import Resource, Api
from .kamrie import Kamrie
from flask_cors import CORS
from flask import request

__name__ = '__main__'
app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/menus/*": {"origins": "*"}})
menu_data_source = MenuDataSource(user=os.getenv('NEO_4J_USERNAME', 'Not found'),
                                  password=os.getenv('NEO_4J_PASSWORD', 'Not found'),
                                  host=os.getenv('NEO_4J_URL', 'Not found'),
                                  port=os.getenv('NEO_4J_BOLT_PORT', 'Not found'))
week_menu_data_access = WeekMenuDataAccess(os.getenv("MONGO_DB_URL", 'Not found'),
                                           os.getenv("MONGO_DB_NAME", 'Not found'),
                                           os.getenv("MONGO_DB_COLLECTION", 'Not found'))
kamrie = Kamrie(menu_data_source, week_menu_data_access)


class Menus(Resource):
    def get(self, year_week):
        week_menu = kamrie.get_week_menu(request.headers.get(""), year_week)
        return json.loads(jsonpickle.encode(week_menu, keys=True, unpicklable=False))

    def post(self, year_week):
        week_menu = kamrie.generate_week_menu()
        kamrie.store_week_menu(request.headers.get(""), year_week, week_menu)
        return json.loads(jsonpickle.encode(week_menu, keys=True, unpicklable=False))


api.add_resource(Menus, '/menus/<path:year_week>')

if __name__ == '__main__':
    app.run(debug=True)
