CREATE DATABASE company;
USE company;

CREATE TABLE jobs (
   job_id VARCHAR(10) PRIMARY KEY,
   job_title  VARCHAR(50),
   min_salary DOUBLE(10,2),
   max_salary DOUBLE(10,2)
   );
   
CREATE TABLE regions (
    region_id VARCHAR(10) PRIMARY KEY,
    region_name VARCHAR(50)
);

CREATE TABLE countries (
    country_id VARCHAR(10) PRIMARY KEY,
    country_name VARCHAR(50),
    region_id VARCHAR(10),
    FOREIGN KEY (region_id) REFERENCES regions(region_id)
);

CREATE TABLE locations (
    location_id VARCHAR(10) PRIMARY KEY,
    street_address VARCHAR(50),
    postal_code VARCHAR(50),
    city VARCHAR(50),
    state_province VARCHAR(50),
    country_id VARCHAR(10),
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

CREATE TABLE departments (
    department_id VARCHAR(10) PRIMARY KEY,
    department_name VARCHAR(50),
    location_id VARCHAR(10),
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

CREATE TABLE employees (
    employee_id VARCHAR(10) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    phone_number VARCHAR(50),
    hire_date DATE,
    job_id VARCHAR(10),
    salary DOUBLE(10,2),
    manager_id VARCHAR(10),
    department_id VARCHAR(10),
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (job_id) REFERENCES jobs(job_id),
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

CREATE TABLE dependents (
    dependent_id VARCHAR(10) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    relationship VARCHAR(50),
    employee_id VARCHAR(10),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

ALTER TABLE dependents RENAME TO dept;

ALTER TABLE employees MODIFY salary SMALLINT;
ALTER TABLE employees ADD commission VARCHAR(50);

INSERT INTO regions VALUES
('1','Europe'),
('2','Americas'),
('3','Asia'),
('4','Middle East and Africa');

INSERT INTO countries VALUES
('IN','India','3'),
('US','United States','2'),
('UK','United Kingdom','1');

INSERT INTO locations VALUES
('1400','Street 1','12345','City1','State1','US'),
('1500','Street 2','54321','City2','State2','IN');

INSERT INTO jobs VALUES
('1','Programmer',4000,10000),
('2','Manager',8000,20000);

INSERT INTO dept VALUES
('1','Administration','1400'),
('2','IT','1500');

INSERT INTO employees 
(employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id)
VALUES
('100','John','Doe','john@gmail.com','1234567890','2020-01-01','1',5000,NULL,'1');

INSERT INTO dependents VALUES
('1','Anna','Doe','Child','100');  
   
 
 