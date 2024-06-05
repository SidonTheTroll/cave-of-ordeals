# Section A 
1. While creating a Series from scalar value ...... is mandatory. 
    1. NaN 
    2. range()
    3. index
    4. None of these 

2. How many elements well be there in the series named 'S1'?   
    `>>> S1 = pd.Series(range(5))`  
    `>>> print(S1)`  
    1. 5 
    2. 4 
    3. 6 
    4. None of the above 

3. To get the transpose of a dataframe D1, you can write
    1. D1.T
    2. D1.Transpose 
    3. D1.swap 
    4. All of these 

4. The command to display last 3 rows from series named 'week' is ...... 
    1. print(week.tail(3))
    2. print(week.Tail(3))
    3. print(week.Tails(3))
    4. print(week.tails(3))

5. To display the dimension of DataFrame df, you may write 
    1. df.dim 
    2. df.panel
    3. df.ndim 
    4. None of these 

6. Wow can we add a missing data in a Series? 

7. Write code to create a Series object using the python sequence (51,61,71,81). Assume that pandas is imported as alias name pd. 

8. How does a dataframe object species indexes to its data rows. 

9. What is DataFrame? 

10. Given a series object `ser1` having area in km for different states. Write a statement to print the areas which are more than 50000 km. 

# Series B 
11. Carefully observe the following code:   
    `import pandas as pd`  
    `y1={'P1':5000,'P2':800,'P3':1200,'P4':1800}`  
    `y2={'P':1300,'Q':1400,'R':1200`  
    `total = {1:y1,2:y2}`  
    `df = df.DataFrame(total)`  
    `print(df)`  
    Answer the following:  
    1. List the index of the DataFrame.
    2. List the column names of DataFrame.

12. Write a Python code to create a DataFrame with appropriate column heading from the list given below:  
    `[[101,'Gurman',98],[102,'Rajveer',95],[103,'Samar',96],[104,'Yuvraj',88]]`

13. What will be the output of the following program:   
    `import pandas as pd`  
    `s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])`  
    `print(s*3)`  
    `print(s>2)`  
    `s['e']=6`  
    `print(s)`

# Section C 

14. Create the following Data Frame: df  

| | **Name** | **DOB** | **GENDER** | **MOBILE** | **Height** | **Weight** | 
|-|-|-|-|-|-|-|
| **0** | ADITYA PAUL | 01/12/2002 | M | 9876543210 | 5.8 | 55 | 
| **1** | PALAK AGRAWAL | 08/11/2002 | F | 9987654321 | 5.0 | 45 | 
| **2** | KULDEEP SINGH | 12/02/2003 | M | 9998765432 | 5.3 | 48 | 
| **3** | NEHA | 02/05/2003 | F | 9999765432 | 5.3 | 50 | 
| **4** | PRAVESH | 03/05/2002 | M | 8886963212 | 5.5 | 5.4 | 
| **5** | SUMIT PACHORI | 05/03/2001 | M | 8956664232 | 5.6 | 56 | 
| **6** | TANUSHKA | 02/02/2002 | F | 9856472362 | 5.1 | 50 | 

What the following statement is doing?  
1. `df['city']=['Gwalior','Indore','Agra','Dewas','Gwalior','Indore','Delhi']`
2. `df.loc[7]=['NANDITA','01/01/2002','F',99988877766,5.3,51]`
3. `df.loc[2,:]`
4. `df.loc[3:5,:]`
5. Add one more column 'FName' with suitable contents to the above DataFrame. 