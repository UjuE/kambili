import os
print("The Url for neo4j is:", os.getenv('NEO_4J_URL', 'Not found'))