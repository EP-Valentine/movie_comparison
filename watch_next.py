import spacy
nlp = spacy.load("en_core_web_md")

# ===== FUNCTIONS =====
# Watch_next Function: takes the decpription of a film as an argument and returns title of most similar movie.
def watch_next(last_watched):

    # Empty score list to store similarity scores in the order of films in the movies list.
    score = []

    # For each item in movies_nlp, append similarity score to score list
    for item in movies_nlp:
        score.append(round(item.similarity(last_watched),2))
        
    # Sorted variant of score list to find highest compatibility score.
    sorted_score = sorted(score.copy())

    # Highest similarity variable to find the index of the highest compatibility movie in the original list order.
    highest_similarity = score.index(sorted_score[-1])

    # Print watch next suggestion to user.
    print (f"You might like {(movies[highest_similarity])[:7]}")

# 'Planet hulk' variable with movie description converted to nlp object.
planet_hulk = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

# Empty movies list to store movie descriptions read and appended from 'movies.txt'.
movies = []
with open("movies.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "")
        movies.append(line)

# For each item in movies, convert the string descriptions to nlp objects.
movies_nlp = [nlp(item) for item in movies]

# Call watch_next() function with 'planet_hulk' as its argument to assess movie similarities.
watch_next(planet_hulk)