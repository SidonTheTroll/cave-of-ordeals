# Part 1: Plotting with Pyplot
## A. Choose the Correct Option 
1. Matplotlib 
2. To plot data points 
3. title()
4. Solid line 
5. show()
6. plot(x,y,'o')
7. xlabel()
8. To add a legend to the plot
9. hist()
10. bar(x,y)

## B. Short Question Answers

### 1. What is the purpose of the pyplot function "figure()"? 
The `figure()` function in pyplot creates a new figure or activates an existing figure, allowing you to set its size, resolution, and other properties before plotting.

### 2. How do you add a label to the y-axis in pyplot?
`ylabel()` is used to label in y-axis. 

### 3. What is the difference between the plot() and scatter() functions in pyplot?
`plot()` creates line plots, connecting data points with lines. `scatter()` creates scatter plots, displaying individual data points without connecting lines.

### 4. How do you add a title to the plot in pyplot?
`title()` is used to add a title to a plot. 

### 5. What is the purpose of the show() function in pyplot?
The `show()` function in pyplot displays the plot on the screen.

## C. Programming 

1. Plot the data in the table below using a bar chart and do the following:
    1. Add labels to the x and y axes
    2. Add a title

| <center> X | <center> Y | 
|-|-|
| 1 | 10 | 
| 2 | 20 | 
| 3 | 30 | 
| 4 | 40 | 

``` py
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

# Create bar chart
plt.bar(x, y)

# Add labels to the axes
plt.xlabel('X')
plt.ylabel('Y')

# Add a title
plt.title('Bar Chart of X vs Y')

# Display the plot
plt.show()
```

2. Create a histogram of the data given below. 

| <center> X |
|-| 
| 10 | 
| 20 | 
| 30 | 
| 40 | 
| 50 | 

```py 
import matplotlib.pyplot as plt

# Data
x = [10, 20, 30, 40, 50]

# Create histogram
plt.hist(x)

# Display the plot
plt.show()
```


# Part 2: MySQL 
## A. Choose the Correct Answer 
1. To manage relational databases
2. CREATE DATABASE
3. To define a unique identifier for a table 
4. SELECT
5. To define a relationship between two tables
6. ALTER TABLE
7. To filter records based on conditions 
8. DELETE 
9. To improve query performance
10. CREATE TABLE LIKE

## B. Short Question Answers: 

### 1. What is the difference between the WHERE and HAVING clauses in MySQL?
**WHERE** filters rows before grouping, while **HAVING** filters groups after aggregation.

### 2. How do you create a relationship between two tables in MySQL? 
To create a relationship between two tables in MySQL, you use a **foreign key constraint**. This is done by defining a foreign key in one table that references the primary key of another table.

### 3. What is the purpose of the ORDER BY clause in MySQL?
The **ORDER BY** clause sorts the result set by one or more columns.

### 4. How do you retrieve data from multiple tables in MySQL?
To retrieve data from multiple tables, use a **JOIN** clause (e.g., INNER JOIN, LEFT JOIN) to combine rows based on related columns.

### 5. What is the purpose of the LIMIT clause in MySQL? 
The **LIMIT** clause restricts the number of rows returned by a query.

# C. Programming: 

###  Create a new database called "school" and create a table called "students" with fields for name, roll number, and grade.

```sql 
CREATE DATABASE school; 
USE school; 
CREATE TABLE students (Name char(20), Roll int, Grade char(1)); 
```

1. Insert five records into the 'students' table.

```sql
INSERT INTO students VALUES ('Ravi', 1, 'A'), ('Ajay', 2, 'A'), ('Bipul', 3, 'A'), ('Sanjay', 4, 'B'), ('Gobind', 5, 'B');
```

2. Retrieve the names and grades of all students in the "students" table. 

```sql
SELECT name, grade FROM students;
```

3. Update the grade of a student with roll number 1 to "A".

```sql 
UPDATE stuents SET grade = 'A' WHERE roll = 1; 
```

4. Delete the record of a student with roll number 3.

```sql 
DELETE FROM students WHERE roll = 3;
```

5. Create a new table called "teachers" with fields for name, subject, and salary.

```sql 
CREATE TABLE teachers(Name char(20), Subject char(10), Salary int);
```

6. Insert three records into the "teachers" table.

```sql 
INSERT INTO teachers VALUES ('Siva', 'Eco', 20000), ('UTTAM', 'Maths', 25000), ('Sandeep', 'Eng', 25000); 
```

7. Retrieve the names and subjects of all teachers in the "teachers" table.

```sql
SELECT name, subjcect FROM teachers; 
```

8. Create a relationship between the "students" and "teachers" tables based on the subject field.

```sql 
ALTER TABLE students
ADD COLUMN subject CHAR(10);

ALTER TABLE teachers
ADD CONSTRAINT unique_subject UNIQUE (subject);

ALTER TABLE students
ADD CONSTRAINT fk_subject
FOREIGN KEY (subject) REFERENCES teachers(subject);
```

9.  Retrieve the names of all students and their corresponding teachers based on the subject field.

```sql 
SELECT 
    students.name AS student_name,
    teachers.name AS teacher_name,
    students.subject
FROM 
    students
JOIN 
    teachers
ON 
    students.subject = teachers.subject;
```