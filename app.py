# https://github.com/stanfordnlp/stanza/blob/main/demo/Stanza_Beginners_Guide.ipynb

import stanza
stanza.download('en') # download English model
nlp = stanza.Pipeline('en') # initialize English neural pipeline
doc = nlp("Barack Obama was born in Hawaii.") # run annotation over a sentence

print ("Three little boys")
print('lAPJF n')

# Load the CSV file
file_path = 'Connections_Data.csv'
data = pd.read_csv(file_path)

# Extract the words (assuming the third column contains the words) and groups (fourth column)
words = data.iloc[1:, 2].tolist()  # Adjusted to select the third column (words)
groups = data.iloc[1:, 3].tolist()  # Adjusted to select the fourth column (groups)



for (word, group) in zip(words, groups):

    print(str(word) + "\t" + str(group))

    print(f"Word: {feature['word']}, Group: {feature['group']}")

