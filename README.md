# Highest Profit

The challenge I'm completing is the "highest profit" challenge where I have to clean a CSV file to remove all the non-numeric data from the "profit" column and convert the resulting Dataframe to a JSON file and print the top 20 rows with the highest profit values.

## Source: 
* CSV file titled "data.csv"

## To run:
* Click on run.bat

## Process Description:
1. Imported the libraries to use - pandas and json
2. Read the csv file and made a copy. A copy was made so the original remained unchanged (minimizes errors when updating and prevents accidental irreversible changes)
3. Printed the length of the copied Dataframe using len(), which gives the number of rows (*1st number output*)
4. Did a quick visual inspection of the "profit" column by converting the series to a list and saw the non-numeric value was the string "N.A."
5. Created a mask that pulled the rows that didn't have the string "N.A."
6. Applied the mask to the copied Dataframe and printed the number of rows (length) using len() again (*2nd number output*)
7. Next converted every value in the "profit" column of copied Dataframe to a numerical value (float)
8. Made a JSON file with updated info from copied Dataframe called data2.json
9. Sorted the "profit" column from highest to lowest and then printed the first 20 rows corresponding to the highest profit values
