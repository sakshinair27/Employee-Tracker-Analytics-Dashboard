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

def get_data3(quarter):
    conn = psycopg2.connect(
        database="Candidate_List",
        user="postgres",
        password=os.getenv("DB_PASSWORD"),
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    if quarter == 'q1':
        cursor.execute("SELECT Employee_Category, COUNT(Employee_Category) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 1 AND 3 GROUP BY Employee_Category;")
    elif quarter == 'q2':
        cursor.execute("SELECT Employee_Category, COUNT(Employee_Category) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 4 AND 6 GROUP BY Employee_Category;")
    elif quarter == 'q3':
        cursor.execute("SELECT Employee_Category, COUNT(Employee_Category) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 7 AND 9 GROUP BY Employee_Category;")
    elif quarter == 'q4':
        cursor.execute("SELECT Employee_Category, COUNT(Employee_Category) FROM list WHERE EXTRACT(MONTH FROM Doj) BETWEEN 10 AND 12 GROUP BY Employee_Category;")
    else:
        cursor.execute("SELECT Employee_Category, COUNT(Employee_Category) FROM list GROUP BY Employee_Category;")
    
    rows = cursor.fetchall()
    category_counts = {
        'Consultant': 0,
        'Contract': 0,
        'Freelancers': 0,
        'Interns': 0,
        'Permanent': 0,
        'Probationary': 0
    }
    
    for row in rows:
        category, count = row
        category_counts[category] = count

    cursor.close()
    conn.close()

    cols = [
        {"id": "", "label": "Employee Category", "pattern": "", "type": "string"},
        {"id": "", "label": "Count", "pattern": "", "type": "number"}
    ]
    rows = [
        {"c": [{"v": "Permanent", "f": None}, {"v": category_counts["Permanent"], "f": None}]},
        {"c": [{"v": "Contract", "f": None}, {"v": category_counts["Contract"], "f": None}]},
        {"c": [{"v": "Consultant", "f": None}, {"v": category_counts["Consultant"], "f": None}]},
        {"c": [{"v": "Probationary", "f": None}, {"v": category_counts["Probationary"], "f": None}]},
        {"c": [{"v": "Freelancers", "f": None}, {"v": category_counts["Freelancers"], "f": None}]},
        {"c": [{"v": "Interns", "f": None}, {"v": category_counts["Interns"], "f": None}]}
    ]

    data = {
        "cols": cols,
        "rows": rows
    }

    return convert_to_float(data)

if __name__ == '__main__':
    quarter = sys.argv[1] if len(sys.argv) > 1 else ''
    data = get_data3(quarter)
    json_data = json.dumps(data)
    print(json_data)
