-- 1
SELECT country_name FROM countries;

-- 2
SELECT email, phone_number FROM employees;

-- 3
SELECT * FROM employees WHERE last_name='Fay';

-- 4
SELECT hire_date FROM employees WHERE last_name IN ('Grant','Whalen');

-- 5
SELECT CONCAT(first_name,' ',last_name)
FROM employees e JOIN jobs j ON e.job_id=j.job_id
WHERE job_title='Shipping Clerk';

-- 6
SELECT first_name, department_id FROM employees WHERE department_id='8';

-- 7
SELECT department_name FROM departments ORDER BY department_name DESC;

-- 8
SELECT first_name FROM employees WHERE last_name LIKE 'K%';

-- 9
SELECT first_name FROM employees WHERE YEAR(hire_date) BETWEEN 1995 AND 1997;

-- 10
SELECT job_title FROM jobs WHERE max_salary <= 5000;

-- 11
SELECT LOWER(email) FROM employees;

-- 12
SELECT first_name FROM employees WHERE YEAR(hire_date)=1995;

-- 13
INSERT INTO employees VALUES (207,'Paul','Newton','paul@gmail.com','123','1997-07-17',2,12000,101,11);

-- 14
DELETE FROM departments WHERE department_name='Shipping';

-- 15
SELECT first_name FROM employees WHERE DAYNAME(hire_date)='Thursday';