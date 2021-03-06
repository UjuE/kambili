from functools import reduce

from neomodel import config, OUTGOING, Traversal
from .datatypes import Meal, Meal_Type
from .menutypes import MenuPlan


class MenuDataSource:
    def __init__(self, host, port, user, password):
        config.DATABASE_URL = 'bolt://%s:%s@%s:%s' % (user, password, host, port)

    def get_menu_plans(self):
        return reduce(lambda left, right: left + right, list(self.retrieve_menu_plan(x) for x in Meal.nodes), [])

    def get_meal_types(self):
        return list(str(x.name) for x in Meal_Type.nodes)

    @staticmethod
    def retrieve_menu_plan(meal):
        definition = dict(node_class=Meal_Type, direction=OUTGOING, relation_type=None, model=None)
        all_relations = Traversal(meal, meal.__label__, definition).all()
        return list(MenuPlan(str(x.name), str(meal.name)) for x in all_relations)
