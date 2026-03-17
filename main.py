import mysql.connector
from fastapi import FastAPI

app = FastAPI()

config = {
  "host": "localhost",
  "port": 3306,
  "user": "root",
  "password": "root",
  "database": "digital_hunter"
}


db = mysql.connector.connect(**config)

cursor = db.cursor()








@app.get("/")
def get_quality_target_movements_warning():
  query = """SELECT entity_id, target_name, priority_level, movement_distance_km
                    FROM targets WHERE (priority_level=1 or priority_level=2)
                 AND movement_distance_km > 5"""
  cursor.execute(query)
  result = cursor.fetchall()
  for x in result:
    print(x)
  return result

@app.get("/df")
def get_quality_target_movements_warning():
  query = """SELECT * FROM `intel_signals`
WHERE HOUR("timestamp") < 20;"""
  cursor.execute(query)
  result = cursor.fetchall()
  for x in result:
    print(x)
  return result


# query = """SELECT count(signal_type) as "signal count",signal_type FROM  intel_signals
#                  GROUP BY signal_type"""


# SELECT entity_id, COUNT(signal_id) AS "total" FROM `intel_signals`
# WHERE priority_level = 99
# GROUP BY entity_id
# ORDER by total DESC
# LIMIT 3;










