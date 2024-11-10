import stanza
import pandas as pd
import random
from sklearn.cluster import KMeans
import numpy as np
import spacy

# Download the English model for stanza
# stanza.download('en')
# nlp = stanza.Pipeline('en')
nlp = spacy.load('en_core_web_md')

# Define words list
words = [
    "ruby", "apple", "c++", "rose",
    "banana", "lily", "carrot", "java",
    "grape", "daisy", "python", "tomato",
    "lettuce", "tulip", "cucumber", "orange"
]

# Function to analyze words and extract relevant linguistic features using Stanza
def analyze_words(word_list):
    analyzed_words = []
    for word in word_list:
        doc = nlp(word)
        features = {'word': word}
        # features['lemma'] = doc.sentences[0].words[0].lemma
        # features['pos'] = doc.sentences[0].words[0].upos
        # features['head'] = doc.sentences[0].words[0].head
        features['vector'] = doc.vector
        analyzed_words.append(features)
    return analyzed_words

# Function to convert analyzed words to a vector form suitable for clustering
def create_word_vectors(word_data):
    word_vectors = []
    for word_features in word_data:
        # Use lemma and POS as features (this is just a simple example)
        vector = [0] * 100  # Initialize a vector of length 100 (or choose your length)
        
        # For simplicity, we just create a dummy vector based on POS and lemma
        vector[0] = word_features['lemma']
        vector[1] = word_features['pos']
        # vector[2] = word_features['ner']
        vector[3] = word_features['head']
        # vector[4] = word_features['morph']
        # vector[5] = word_features['vector']

        word_vectors.append(vector)
    
    return np.array(word_vectors)

# Function to group words into clusters (2D array) using KMeans
def group_words_by_clustering(word_data, num_groups=4):
    word_vectors = create_word_vectors(word_data)
    
    # Use KMeans clustering to group words
    kmeans = KMeans(n_clusters=num_groups)
    kmeans.fit(word_vectors)
    
    # Get the labels (clusters) and group words accordingly
    labels = kmeans.labels_
    
    # Create a dictionary to store words by cluster
    grouped_words = {i: [] for i in range(num_groups)}
    for idx, label in enumerate(labels):
        grouped_words[label].append(word_data[idx]['word'])
    
    # Convert dictionary to a 2D list (groups)
    grouped_words_list = [group for group in grouped_words.values()]
    
    return grouped_words_list

# Main model function for the Connections game
def model(words, strikes, isOneAway, correctGroups, previousGuesses, error):
    # Analyze words and group them using clustering
    word_data = analyze_words(words)
    grouped_words = group_words_by_clustering(word_data, num_groups=4)  # Group words into 4 groups
    
    # Initialize guesses list and guessed groups set
    guesses = []
    
    # Iterate through the groups and select one word from each group to form a guess
    for group in grouped_words:
        # Ensure we only select one word per group
        for word in group:
            if word not in previousGuesses:
                guesses.append(word)
                previousGuesses.append(word)  # Mark this word as guessed
                break  # Only add one word per group
    
    # If fewer than 4 guesses, add random guesses from the remaining words
    while len(guesses) < 4:
        guess = random.choice(words)
        if guess not in guesses:
            guesses.append(guess)
    
    # Return 1D array with 4 words (a guess) and whether the turn should end
    current_guess = guesses[:4]  # Ensure it returns exactly 4 words
    endTurn = strikes >= 3  # End the turn if 3 or more strikes
    
    return current_guess, endTurn

# Initialize game parameters
strikes = 0
isOneAway = False
correctGroups = []
previousGuesses = []
error = "0"

# Call the model to get a guess and check if the turn ends
guess, endTurn = model(words, strikes, isOneAway, correctGroups, previousGuesses, error)

# Print the results
print("Guess:", guess)
print("End Turn:", endTurn)
