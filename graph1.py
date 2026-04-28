import os
import psycopg2
import json
from decimal import Decimal
import sys

def convert_to_float(data):
    if isinstance(data, dict):
        return {convert_to_float(key): convert_to_float(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_to_float(element) for element in data]
    elif isinstance(data, Decimal):
        return float(data)  # Convert Decimal to float
    return data

def get_data1(quarter):
    conn = psycopg2.connect(
        database="Candidate_List",
        user="postgres",
        password=os.getenv("DB_PASSWORD"),
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    if quarter == 'q1':
        cursor.execute("SELECT Marital_Status, COUNT(*) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 1 AND 3 GROUP BY Marital_Status;")
    elif quarter == 'q2':
        cursor.execute("SELECT Marital_Status, COUNT(*) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 4 AND 6 GROUP BY Marital_Status;")
    elif quarter == 'q3':
        cursor.execute("SELECT Marital_Status, COUNT(*) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 7 AND 9 GROUP BY Marital_Status;")
    elif quarter == 'q4':
        cursor.execute("SELECT Marital_Status, COUNT(*) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 10 AND 12 GROUP BY Marital_Status;")
    else:
        cursor.execute("SELECT marital_status, COUNT(*) FROM list GROUP BY marital_status;")
    rows = cursor.fetchall()

    married_count = 0
    single_count = 0
    for row in rows:
        status, count = row
        if status == 'Married':
            married_count = count
        elif status == 'Single':
            single_count = count

    cursor.close()
    conn.close()

    cols = [
        {"id": "", "label": "Marital Status", "pattern": "", "type": "string"},
        {"id": "", "label": "Married vs Unmarried", "pattern": "", "type": "number"}
    ]
    rows = [
        {"c": [{"v": "Married", "f": None}, {"v": married_count, "f": None}]},
        {"c": [{"v": "Single", "f": None}, {"v": single_count, "f": None}]}
    ]

    data = {
        "cols": cols,
        "rows": rows
    }

    return convert_to_float(data)

if __name__ == '__main__':
    quarter = sys.argv[1] if len(sys.argv) > 1 else ''
    data = get_data1(quarter)
    json_data = json.dumps(data)
    print(json_data)
