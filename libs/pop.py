import os
from libs.datastore import MenuDataStore
import pandas as pd
from openpyxl import load_workbook

from libs.menutypes import MenuPlan

store = MenuDataStore(user=os.getenv('NEO_4J_USERNAME', 'Not found'),
                      password=os.getenv('NEO_4J_PASSWORD', 'Not found'),
                      host=os.getenv('NEO_4J_URL', 'Not found'),
                      port=os.getenv('NEO_4J_BOLT_PORT', 'Not found'))

xl = load_workbook('menu.xlsx')
count = 2
df1 = xl['Sheet1']

meal_name = df1['A'+str(count)].value
meal_type = df1['B'+str(count)].value

while meal_name is not None and meal_type is not None:
    for the_type in meal_type.split(","):
        store.create(MenuPlan(the_type.strip(), meal_name))
        count += 1
        meal_name = df1['A'+str(count)].value
        meal_type = df1['B'+str(count)].value

