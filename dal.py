from db import get_mysql_connection

def get_quality_target_movements_warning():
    query = """SELECT entity_id, target_name, priority_level, movement_distance_km
                      FROM targets WHERE (priority_level=1 or priority_level=2)
                   AND movement_distance_km > 5"""
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def get_aggregation_sources_count():
    query = """SELECT count(signal_type) as "total",signal_type FROM intel_signals
                   GROUP BY signal_type order by total desc;"""
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def get_new_targets():
    query = """SELECT entity_id, COUNT(signal_id) AS "total" FROM `intel_signals`
    WHERE priority_level = 99
    GROUP BY entity_id
    ORDER by total DESC
    LIMIT 3;"""
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def get_target_movements(entity_id):
    query = """SELECT reported_lat, reported_lon FROM `intel_signals` 
               WHERE entity_id = "TGT-013" ORDER BY reported_lat;"""
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result