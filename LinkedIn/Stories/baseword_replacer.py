import pandas as pd
import re

# --------------------------------------
# READ FILES
# --------------------------------------

df = pd.read_csv(r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Stories\connections.csv")

base_df = pd.read_csv(
    r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Stories\base_word_dict.csv"
)

# --------------------------------------
# CREATE DICTIONARY
# --------------------------------------

base_dict = dict(
    zip(
        base_df['word'],
        base_df['base_word']
    )
)

# CLEAN FUNCTION

def clean_text(text):

    text = str(text).lower()

    text = re.sub(
        r'[^a-zA-Z0-9& \\s]',
        ' ',
        text
    )

    return text


# REPLACE BASE WORDS
def replace_base_words(text):

    text = clean_text(text)

    words = text.split()

    final_words = []

    for word in words:

        replaced = base_dict.get(
            word,
            word
        )

        final_words.append(replaced)

    return " ".join(final_words).title()



# CREATE COLUMN

df.insert(
    loc=df.columns.get_loc('Position') + 1,
    column='Base_Role',
    value=df['Position'].apply(replace_base_words)
)



df.to_csv("Updated Connection.csv")
print("Update based word created at csv")