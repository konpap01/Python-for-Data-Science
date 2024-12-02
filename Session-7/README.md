# This folder contains the content and exercises we went through in Session 7

# Exercises :
1. Create a lambda function to classify flowers based on their petal length.
2. Use map to convert the Species column into numeric values:
3. Use value_counts on the Species column to count how many entries belong to each species.
4. Use drop_duplicates to remove any duplicate rows based on SepalLengthCm and PetalLengthCm.
5. Use astype to convert the SepalLengthCm column to a string type, then back to a float type. Gracefully handle any errors during the conversion.
6. Save the modified DataFrame to a CSV file using to_csv, ensuring the index is included.
7. Count the number of missing values in each column.
8. Replace missing values in the department column with "Unknown".
9. Use fillna to fill missing values in the age column with the average age.
10. Drop rows where the professor column is missing.
11. Create a new column called professor_last_name by extracting the last name from the professor column.