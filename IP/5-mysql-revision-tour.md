# MySQL Revision Tour 

## 7. What is Foreign key? How do you define a foreign key in your table? 
A foreign key is a field in one table that uniquely identifies a row of another table. It establishes a link between the data in the two tables.

To define a foreign key:

```
ALTER TABLE child-table
ADD CONSTRAINT foreign-key 
FOREIGN KEY (foreign_key_column)
REFERENCES parent_table(primary_key_column);
```

## 8. How is FOREIGN KEY command different from PRIMARY KEY command? 
A primary key uniquely identifies each record in a table and ensures no duplicates or NULL values.  
Whereas a foreign key creates a link between two tables, ensuring referential integrity by matching a primary key in another table.

## 9. How is FOREIGN KEY commands related to the PRIMARY KEY? 
PRIMARY KEY commands define and enforce the PRIMARY KEY constraint, ensuring each record in a table is unique and non-NULL. 

## 10. What are table constraints? What are column constraints? How are these two different? 
Table constraints apply to the entire table and can involve multiple columns, such as primary keys, foreign keys and unique constraints.  
Column constraints apply to individual columns, specially rules like NOT NULL, UNIQUE or DEFAULT values.  
Table constraints affect multiple columns or relationships between tables, while column constraints affect only single columns. 

## 11. Insert all those records of table Accounts into table _Pending_ where amt_outstanding is more than 10000. 
```
INSERT INTO Pending
SELECT *
FROM Accounts
WHERE amt_outstanding > 10000;
```

## 12. Increase salary of employee records by 10% (table employee). 
```
UPDATE employee
SET salary = salary * 1.10;
```

## 13. Add a constraint (NN-Grade) in table Empl that declares column Grade not null. 
```
ALTER TABLE Empl
MODIFY Grade VARCHAR(column_length) NOT NULL;
```

## 14. Drop table Empl. 
```
DROP TABLE Empl;
```

## 15. Differentiate between: 
1. DROP TABLE, DROP DATABASE 
    - DROP TABLE only deletes a table while DROP DATABASE deletes the whole database where tables are kept. 
2. DROP TABLE, DROP clause of ALTER TABLE. 
    - DROP TABLE deletes a table while DROP clause of ALTER TABLE deletes a specific column, constraint, or index from an existing table without deleting the entire table or its other data.

## 16. Mr. Mittal is using a table with following columns: `Name, Class, Stream:Id, Stream_name`. He needs to display names of students who have not assigned any stream or have been assigned stream_name that ends with "computers". He wrote the following command, which did not give the desired result. `SELECT Name, Class FROM Students WHERE Stream_name = NULL or Stream_name="%computers";`. Help Mr. Mittal to run the query by removing the error and write the correct query. 
```
SELECT Name, Class
FROM Students
WHERE Stream_name IS NULL
   OR Stream_name LIKE '%computers';
``` 