# import os
# import unittest
# from libs.datasource import MenuDataSource
# from libs.kambili import Kambili
# TODO write integration test that puts in a number of meals in the database and generates a menu for the week
import os
from libs.datastore import MenuDataStore
import pandas as pd


store = MenuDataStore(user=os.getenv('NEO_4J_USERNAME', 'Not found'),
               password=os.getenv('NEO_4J_PASSWORD', 'Not found'),
               host=os.getenv('NEO_4J_URL', 'Not found'),
               port=os.getenv('NEO_4J_BOLT_PORT', 'Not found'))

xl = pd.ExcelFile('/Users/ujuezeoke/Desktop/jump.xlsx')
df1 = xl.parse('Sheet1')
print(df1)


