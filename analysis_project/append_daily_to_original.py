import csv


def append_csv(source_file, target_file):
    with open(source_file, 'r', newline='') as source_csvfile:
        with open(target_file, 'a', newline='') as target_csvfile:
            reader = csv.reader(source_csvfile)
            writer = csv.writer(target_csvfile)

            # Skip the header row if necessary
            next(reader, None)

            # Append each row from the source file to the target file
            for row in reader:
                writer.writerow(row)


# tran_dtl_daily   ---->>>>>  tran_dtl:
append_csv(r'C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_dtl_daily.csv',
           r'C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_dtl.csv')

# tran_hdr_daily  ---->>>>>  tran_hdr:
append_csv(r'C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_hdr_daily.csv',
           r'C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_hdr.csv')

print("Data")