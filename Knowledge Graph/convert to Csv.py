import os
import glob
import pandas as pd

# ==========================
# Configuration
# ==========================
INPUT_FOLDER = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Knowledge Graph\input Data Files\Concepts Files\Excel Files"
CSV_OUTPUT_FOLDER = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Knowledge Graph\input Data Files\Concepts Files\csv files"
UNION_OUTPUT_FILE = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Knowledge Graph\input Data Files\Concepts Files\Excel Files\Union_File2.xlsx"

# Create output folders if they don't exist
os.makedirs(CSV_OUTPUT_FOLDER, exist_ok=True)
os.makedirs(os.path.dirname(UNION_OUTPUT_FILE), exist_ok=True)

# Find all Excel files
excel_files = glob.glob(os.path.join(INPUT_FOLDER, "*.xlsx"))
excel_files += glob.glob(os.path.join(INPUT_FOLDER, "*.xls"))

if not excel_files:
    raise FileNotFoundError("No Excel files found in the input folder.")

all_data = []
expected_columns = None

print(f"Found {len(excel_files)} Excel file(s).\n")

for file in excel_files:
    print(f"Processing: {os.path.basename(file)}")

    # --------------------------
    # Read Excel
    # --------------------------
    df = pd.read_excel(file)

    # --------------------------
    # Normalize Column Names
    # --------------------------
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.lower()
    )

    # --------------------------
    # Standardize concept_level values
    # --------------------------
    if "concept_level" in df.columns:

        # Convert to lowercase and remove spaces
        df["concept_level"] = (
            df["concept_level"]
            .fillna("")
            .astype(str)
            .str.strip()
            .str.lower()
        )

        # Replace values
        df["concept_level"] = df["concept_level"].replace({
            "basic": "beginner",
            "beginner": "beginner",
            "medium": "intermediate",
            "intermidiate": "intermediate",
            "intermediate": "intermediate",
            "advance": "advanced",
            "advanced": "advanced"
        })

        # Validate values
        valid_values = {"beginner", "intermediate", "advanced"}

        invalid = df.loc[
            ~df["concept_level"].isin(valid_values),
            "concept_level"
        ].unique()

        if len(invalid) > 0:
            raise ValueError(
                f"\nInvalid concept_level values found in "
                f"{os.path.basename(file)}:\n{list(invalid)}"
            )

    # --------------------------
    # Validate Column Headers
    # --------------------------
    current_columns = list(df.columns)

    if expected_columns is None:
        expected_columns = current_columns
    else:
        if current_columns != expected_columns:
            raise ValueError(
                f"\nColumn header mismatch detected!\n\n"
                f"File: {os.path.basename(file)}\n\n"
                f"Expected:\n{expected_columns}\n\n"
                f"Found:\n{current_columns}"
            )

    # --------------------------
    # Save CSV
    # --------------------------
    csv_name = os.path.splitext(os.path.basename(file))[0] + ".csv"
    csv_path = os.path.join(CSV_OUTPUT_FOLDER, csv_name)

    df.to_csv(csv_path, index=False, encoding="utf-8-sig")

    # --------------------------
    # Add to Union List
    # --------------------------
    all_data.append(df)

# ==========================
# Create Union Excel
# ==========================
union_df = pd.concat(all_data, ignore_index=True)

union_df.to_excel(UNION_OUTPUT_FILE, index=False)

print("\n===================================")
print("Completed Successfully")
print(f"Processed Files : {len(excel_files)}")
print(f"CSV Folder      : {CSV_OUTPUT_FOLDER}")
print(f"Union Excel     : {UNION_OUTPUT_FILE}")
print("===================================")