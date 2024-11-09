# https://github.com/stanfordnlp/stanza/blob/main/demo/Stanza_Beginners_Guide.ipynb

import stanza
>>> stanza.download('en') # download English model
>>> nlp = stanza.Pipeline('en') # initialize English neural pipeline
>>> doc = nlp("Barack Obama was born in Hawaii.") # run annotation over a sentence

print ("Three little boys")
print('lAPJF n')
