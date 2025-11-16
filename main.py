import csv
from fastapi import FastAPI

# get city data from csv file
filename = "world_table_city.csv"
with open(filename, "r", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    data_city = [{k: v for (k, v) in zip(headers, row)} for row in csv_reader]

# create FastAPI instance
app = FastAPI()

# root endpoint
@app.get("/")
async def read_root() -> dict:
    return {"message": "Hello there"}

# endpoint to get city by name (path parameter)
@app.get("/world/city/{name}")
async def read_city(name: str) -> dict:
    for row in data_city:
        if row["Name"].lower() == name.lower():
            return {"result": row}
    return {"result": {}}

   
