# Part 3: Database Query using MySQL 
## 20. Create the followign table products and write queries given below: 

| Pcode | Pname | Qty | Price | Company | 
|:-:|:-:|:-:|:-:|:-:|
| P1001 | iPad | 120 | 15000 | Apple | 
| P1002 | LED TV | 100 | 85000 | Sony | 
| P1003 | DSLR Camera | 10 | 25000 | Philips | 
| P1004 | iPhone | 50 | 95000 | Apple | 
| P1005 | LED TV | 20 | 45000 | MI | 
| P1006 | Bluetooth Speaker | 100 | 2000 | Ahuja | 

- Constraints: 
    1. **Pcode:** Primary key
    2. **Pname:** Not null

```mysql
create table products(
    pno varchar(5) primary key,
    pname varchar(25) not null, 
    qty int(3),
    price int(5),
    company varchar(15)
);

insert into products values( "P1001", "iPad", 120, 15000, "Apple"),
insert into products values( "P1002", "LED TV", 100, 85000, "Sony"),
insert into products values( "P1003", "DSLR Camera", 10, 25000, "Philips"),
insert into products values( "P1004", "iPhone", 50, 95000, "Apple"),
insert into products values( "P1005", "LED TV", 20, 45000, "MI"),
insert into products values( "P1006", "Bluetooth Speaker", 100, 2000, "Ahuja"),
```

### 1. To join product and company and display in tabular form like - <pname> manufactured by <company> 
```mysql
select concat(pname, concat( " manufactured by ", company)) from products;
```

### 2. Convert all product name into capital.
```mysql
select ucase(pname) from products;
```

### 3. Display the cube of products quantity for more than or 100 in quantity.
```mysql
select qty, pow(qty,3) from products where qty>=100;
```

### 4. Divide the price by 3 and display the result with 1 fraction digit for price of more than 40,000. 
```mysql
select round((price/3),1) from products where price>40000;
```

### 5. Display pname (last four letters only), qty, price with 2 decimal points and company for price in between 30000 and 80000. 
```mysql
select right(pname, 4), qty, round(price,2), company from products where price between 30000 and 80000.
```

### 6. Display maximum price of products. 
```mysql
select max(price) from products; 
```

### 7. Display the total quantities of all products. 
```mysql
select sum(qty) from products;
```

### 8. Display the average price of LED TV and Apple products. 
```mysql
select avg(price) from products where pname="LED TV" or company="Apple";
```

### 9. Find the difference between maximum price and minimum price from the table. 
```mysql 
select max(price)-min(price) from products; 
```

### 10. Display unique products from the table.
```mysql 
select distinct(pname) from products;
```

### 11. Count the unique company from products. 
```mysql 
select count(distinct(company)) from products;
```

### 12. Display the product number, product name and company in the descending order of their price. 
```mysql 
select pno, pname, company, price from products order by price desc;
```

### 14. Display product number and product names in their ascending order of names.
```mysql 
select pno, pname from products order by pname;

```

### 15. Display maximum price of products manufactured by apple.
```mysql 
select company, max(price) from products group by company having company="Apple";
```
