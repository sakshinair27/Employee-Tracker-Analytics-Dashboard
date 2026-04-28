-- ====================================================
-- Employee Tracker & Analytics System - Database Schema
-- ====================================================
-- PostgreSQL schema for the Employee Tracker project
-- Run this file to create all required tables
-- ====================================================

-- User authentication and details
CREATE TABLE usermode (
    userid SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL
);

-- User-to-Role mapping
CREATE TABLE userrole (
    userid INT REFERENCES usermode(userid),
    roleid INT NOT NULL
);

-- Menu options for the application
CREATE TABLE menu (
    menuid SERIAL PRIMARY KEY,
    menudescription VARCHAR(100) NOT NULL
);

-- Role-based menu access control
CREATE TABLE rolemenu (
    menuid INT REFERENCES menu(menuid),
    roleid INT NOT NULL,
    status BOOLEAN NOT NULL
);

-- Main employee data table
CREATE TABLE list (
    empid SERIAL PRIMARY KEY,
    doj DATE NOT NULL,
    gender VARCHAR(10),
    department VARCHAR(50),
    designation VARCHAR(50),
    enter_ctc INT,
    employee_category VARCHAR(50),
    marital_status VARCHAR(20),
    grade VARCHAR(20),
    level_ VARCHAR(20)
);
