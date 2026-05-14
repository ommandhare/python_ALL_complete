import csv

rolesPath= r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Stories\connections.csv"

baseWordPath= r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Stories\base_word_dict.csv"


def clean_text(txt):
    txt = str(txt)

    txt = txt.lower()

    # Remove corrupted UTF patterns
    txt = re.sub(r'â\S*', ' ', txt)

    # Normalize unicode
    txt = unicodedata.normalize('NFKD', txt)

    # Convert accented chars to ASCII
    txt = txt.encode('ascii', 'ignore').decode('utf-8')

    # Replace &
    txt = txt.replace("&", "and")

    # Keep only letters/numbers/spaces
    txt = re.sub(r'[^A-Za-z ]', '', txt)

    # Remove extra spaces
    txt = " ".join(txt.split())

    return txt


cnt=0
with open(rolesPath, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    for line in reader:
        if cnt == 0:
            cnt += 1
            continue

        First_Name, Last_Name, URL, Email_Address, Company, Position, Connected_On = line





# for datatuple in open(baseWordPath):
#     sr_no,word,base_word = datatuple.strip().split(",")