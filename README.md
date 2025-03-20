Files Included :-
h1.py → The main Python script that processes the data
Solution_submission.txt → The test results showing extracted groups and their counts

- Read the Input Excel File and Used pandas to load the Excel sheet.
- Extract Group Information and Searched for patterns like Groups: [code]<I>XXXX</I>[/code] using regular expressions.
- Split multiple groups if separated by commas and Count Unique Group Occurrences
- Used a dictionary to keep track of how often each group appears.
- The script reads data from the "Input Data sheet" in the provided Excel file.  
- It extracts relevant group names from the "Additional comments" column.  
- The script counts the occurrences of each unique group and displays them in tabular format.  
- The output matches the expected format as provided in the test instructions.  

Output the Results:-
The script prints the results and saves them in Solution_submission.txt.

Install dependencies:
- pip install pandas openpyxl
Run the script:
- python h1.py

Sample Output:-
Group Name	               Number of Occurrences
Huntingdon and Liz areas	        2
SML Group GMs                   	1
Eastend GMs                     	3

- The script is scalable and can handle large datasets.
- If the input file structure changes, update the column name accordingly.
