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

def get_data2(quarter):
    conn = psycopg2.connect(
        database="Candidate_List",
        user="postgres",
        password=os.getenv("DB_PASSWORD"),
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    if quarter == 'q1':
        cursor.execute("SELECT Gender, COUNT(*) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 1 AND 3 GROUP BY Gender;")
    elif quarter == 'q2':
        cursor.execute("SELECT Gender, COUNT(*) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 4 AND 6 GROUP BY Gender;")
    elif quarter == 'q3':
        cursor.execute("SELECT Gender, COUNT(*) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 7 AND 9 GROUP BY Gender;")
    elif quarter == 'q4':
        cursor.execute("SELECT Gender, COUNT(*) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 10 AND 12 GROUP BY Gender;")
    else:
        cursor.execute("SELECT Gender, COUNT(*) FROM list GROUP BY Gender;")
    rows = cursor.fetchall()

    male_count = 0
    female_count = 0
    for row in rows:
        gender, count = row
        if gender == 'male':
            male_count = count
        elif gender == 'female':
            female_count = count

    cursor.close()
    conn.close()

    cols = [
        {"id": "", "label": "Gender Ratio", "pattern": "", "type": "string"},
        {"id": "", "label": "Male VS Female", "pattern": "", "type": "number"}
    ]
    rows = [
        {"c": [{"v": "Male", "f": None}, {"v": male_count, "f": None}]},
        {"c": [{"v": "Female", "f": None}, {"v": female_count, "f": None}]}
    ]

    data = {
        "cols": cols,
        "rows": rows
    }

    return convert_to_float(data)

if __name__ == '__main__':
    quarter = sys.argv[1] if len(sys.argv) > 1 else ''
    data = get_data2(quarter)
    json_data = json.dumps(data)
    print(json_data)
