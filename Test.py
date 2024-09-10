import pandas as pd

# Load the data into a DataFrame
data = pd.read_csv(r'C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\analysis_project\daily_files\member.csv')

# Create new member_id range from 1001 to 1100
data['member_id'] = range(1001, 1100)

# Save the updated DataFrame back to a CSV file
data.to_csv(r'C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\analysis_project\daily_files\memberData.csv', index=False)
#member_id,first_name,last_name,store_id,reg_date