import pandas as pd
import re
from collections import Counter

def count_groups(file_path, sheet_name="Input Data sheet"):
   
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    print("Available columns:", df.columns)

    
    if "Additional comments" not in df.columns:
        print("Error: 'Additional comments' column not found.")
        return

 
    group_list = []

    for comment in df["Additional comments"].dropna():
        match = re.search(r"Groups :\s*(.*)", comment)  
        if match:
            groups = match.group(1).split(",")  
            cleaned_groups = [re.sub(r"\[/?code\]|\<I\>|\</I\>", "", g.strip()) for g in groups]  
            group_list.extend(cleaned_groups)

   
    group_counts = Counter(group_list)

    
    result_df = pd.DataFrame(group_counts.items(), columns=["Group name", "Number of occurrences"])

    
    print(result_df)


file_path = "C://Users//shalu//OneDrive//Desktop//test and task//DIGITAL TASK//coding challenge test (1) (1).xlsx"
count_groups(file_path)
