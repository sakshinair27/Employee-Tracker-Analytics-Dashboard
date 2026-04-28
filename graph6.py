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


def get_data6(quarter):
    conn = psycopg2.connect(
        database="Candidate_List",
        user="postgres",
        password=os.getenv("DB_PASSWORD"),
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    if quarter == 'q1':
        cursor.execute(
            "SELECT department, COUNT(department) AS Dcount, SUM(enter_ctc) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 1 AND 3 GROUP BY department;"
        )
    elif quarter == 'q2':
        cursor.execute(
            "SELECT department, COUNT(department) AS Dcount, SUM(enter_ctc) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 4 AND 6 GROUP BY department;"
        )
    elif quarter == 'q3':
        cursor.execute(
            "SELECT department, COUNT(department) AS Dcount, SUM(enter_ctc) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 7 AND 9 GROUP BY department;"
        )
    elif quarter == 'q4':
        cursor.execute(
            "SELECT department, COUNT(department) AS Dcount, SUM(enter_ctc) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 10 AND 12 GROUP BY department;"
        )
    else:
        cursor.execute(
            "SELECT department, COUNT(department) AS Dcount, SUM(enter_ctc) FROM list GROUP BY department;"
        )

    rows = cursor.fetchall()
    data = [['Department', 'Count of Departments', 'CTC']]
    for row in rows:
        data.append(list(row))

    cursor.close()
    conn.close()

    chart_data = {
        "cols": [
            {"id": "", "label": "Department", "pattern": "", "type": "string"},
            {"id": "", "label": "Count", "pattern": "", "type": "number"},
            {"id": "", "label": "CTC", "pattern": "", "type": "number"}
        ],
        "rows": [
            {"c": [{"v": row[0], "f": None}, {"v": row[1], "f": None}, {"v": row[2], "f": None}]} for row in data
        ]
    }

    return convert_to_float(chart_data)


if __name__ == '__main__':
    quarter = sys.argv[1] if len(sys.argv) > 1 else ''
    data = get_data6(quarter)
    json_data = json.dumps(data)
    print(json_data)
