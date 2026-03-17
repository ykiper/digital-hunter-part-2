import mysql.connector
from fastapi import FastAPI
from dal import get_quality_target_movements_warning, get_aggregation_sources_count, get_new_targets

app = FastAPI()


@app.get("/quality_target_movements")
def get_quality_target_movements_endpoint():
    return get_quality_target_movements_warning()


@app.get("/aggregation_sources_count")
def get_aggregation_sources_count_endpoint():
    return get_aggregation_sources_count()


@app.get("/new_targets")
def get_new_targets_endpoint():
    return get_new_targets()

















