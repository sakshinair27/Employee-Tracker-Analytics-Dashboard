# 📊 Employee Tracker & Analytics Dashboard

> A full-stack HR analytics system that manages employee data and delivers real-time insights through 6 interactive dashboards — built with Flask, PostgreSQL, and Google Charts.

---

## 🎯 Project Overview

The **Employee Tracker & Analytics System** is a Flask-based web application that helps companies manage and visualize employee data efficiently. Organizations often rely on manual Excel processes for HR analytics — slow, error-prone, and disconnected from real-time data.

This system replaces those workflows with a **scalable, role-based analytics platform** that provides actionable insights through dynamic dashboards. With **PostgreSQL for reliable storage** and **Google Charts for visualization**, the platform serves Admin and User roles differently — protecting sensitive data while enabling data-driven HR decisions.

---

## ✨ Key Features

- 🔐 **Role-Based Access Control** — Admin and User views with different permissions
- 📊 **6 Interactive Dashboards** — Real-time HR insights
- 🗄️ **Relational Database Design** — 5 tables with proper constraints
- 📈 **Quarterly + Full-Data Analysis** — View metrics by Q1–Q4 or annually
- 🔄 **Live SQL Queries** — Dashboards update from the database in real-time
- 🎨 **Clean, Responsive UI** — Built with HTML, CSS, and JavaScript

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| **Backend** | Python (Flask) |
| **Database** | PostgreSQL |
| **Frontend** | HTML, CSS, JavaScript |
| **Visualization** | Google Charts |
| **Architecture** | MVC pattern, role-based routing |

---

## 📊 Available Dashboards

| Dashboard | Description |
|---|---|
| **Marital Status** | Pie, bar, and column views of married vs single distribution |
| **Gender Ratio** | Visualizes male-to-female employee distribution |
| **Part-time vs Full-time** | Workforce composition analysis |
| **Grade Levels** | Grade distribution across the organization |
| **Designation Count** | Frequency of each job designation |
| **Department Count vs CTC** | Department size compared to total compensation |

Each dashboard supports **quarterly filtering (Q1, Q2, Q3, Q4)** and **full-data view**.

---

## 🗄️ Database Schema

The system uses **5 normalized tables** with proper constraints:

| Table | Purpose | Key Attributes |
|---|---|---|
| **usermode** | Stores user details | userid (PK), username |
| **userrole** | Maps users to roles | userid (FK), roleid |
| **menu** | Stores menu options | menuid (PK), menudescription |
| **rolemenu** | Role-to-menu access mapping | menuid (FK), roleid (FK), status |
| **list** | Stores employee data | empid (PK), doj, gender, department, designation, enter_ctc, employee_category |

**Relationships:**
- One-to-Many: `usermode → userrole`, `menu → rolemenu`
- Many-to-Many: Resolved through `rolemenu`
- Constraints: Primary keys, Foreign keys, NOT NULL, BOOLEAN status flags

---

## 👥 My Contributions

This was a **3-person team project**. My specific contributions:

- 🎨 **Designed and implemented Graph4** — Grade vs CTC vs Level visualization
- 💻 **UI Development Assistance** — Helped build the responsive dashboard interface
- 🔍 **SQL Query Development** — Wrote aggregation queries for grade-level analysis

```
Sample of my Graph4 SQL query:
SELECT grade, MIN(enter_ctc), level FROM list GROUP BY grade, level_;
```

---

## 🚀 How to Run

Set up and run the project locally:

`git clone https://github.com/sakshinair27/Employee-Tracker-Analytics-Dashboard.git`

`cd Employee-Tracker-Analytics-Dashboard`

`pip install -r requirements.txt`

Set up PostgreSQL and create the database:

`createdb Candidate_List`

Run the SQL scripts to create tables and load data:

`psql -d Candidate_List -f schema.sql`

Start the Flask application:

`python app.py`

Visit `http://localhost:5000` in your browser.

---

## 📁 Project Structure

```
Employee-Tracker-Analytics-Dashboard/
├── app.py                            # Main Flask application
├── graph3.py                         # Employee category analysis (teammate)
├── graph4.py                         # Grade vs CTC vs Level (my contribution)
├── graph5.py                         # Designation count (teammate)
├── graph6.py                         # Department count & CTC (teammate)
├── templates/                        # HTML templates
│   ├── menuAdmin.html
│   ├── menuUser.html
│   └── ...
├── static/                           # CSS, JS, and image assets
├── data/                             # Sample CSV files
│   ├── Candidate_List.csv
│   ├── menu.csv
│   ├── rolemenu.csv
│   ├── usermode.csv
│   └── userrole.csv
├── schema.sql                        # PostgreSQL table creation scripts
├── requirements.txt                  # Python dependencies
├── saknair_Final_Project_Part1.pdf   # Project proposal document
├── saknair_Final_Project_Part2.pdf   # Final implementation report
└── README.md
```

---

## 🎯 Key Outcomes

- ✅ Replaced **manual Excel-based HR processes** with a scalable analytics platform
- ✅ Implemented **role-based access** ensuring data security across user types
- ✅ Built **6 dynamic dashboards** powered by live PostgreSQL queries
- ✅ Designed a **normalized relational database** with proper constraints
- ✅ Demonstrated full-stack development from database design to frontend UI

---

## 🌟 What I Learned

- Designing **relational databases** with proper normalization and constraints
- Implementing **role-based access control** in web applications
- Writing **complex SQL queries** for analytical use cases
- Integrating **Flask backends** with frontend visualization libraries
- Collaborating effectively in a **multi-developer team** with shared codebases

---

## 🚀 Future Improvements

- 🤖 Add **predictive analytics** for attrition forecasting
- 📱 Build a **mobile-responsive design**
- 🔍 Implement **advanced filtering** by date range, department, or designation
- 📤 Add **export to Excel/PDF** functionality for reports
- 🔐 Enhance security with **password hashing** and **session management**

---

## 👥 Team

Built collaboratively as a 3-person team for the **SP25 Applied Database Technologies** course at Indiana University:

- **Lokesh Reddy Elluri** — Database Design, ERD, Graphs 3 & 6
- **Rujula Nitin Patil** — Flask Web Application, Backend Logic, Graph 5
- **Sakshi Nair** — Graph 4 (Grade vs CTC vs Level), UI Assistance

---

## 📫 Connect With Me

**Sakshi Nair** — MS Data Science @ Indiana University

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/sakshinair27)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:sakshinair086@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/sakshinair27)
