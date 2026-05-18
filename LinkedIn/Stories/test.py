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
        r'[^a-zA-Z0-9 &\\s]',
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


# Extract, filter, and count
words = df['Base_Role'].str.split().explode()
words_2 = words[words.str.len() == 2]
words_3 = words[words.str.len() == 3]
# Count
count = len(words_2)
count_3 = len(words_3)

# Print words and count
print("2-letter words:")
words_2 = words_2.drop_duplicates()
print(words_2.to_list())


print("3-letter words:")
words_3=words_3.drop_duplicates()
print(words_3.to_list())

print("\nTotal count:", count)
print("\nTotal count:", count_3)


# df.to_csv("Updated Connection.csv")
