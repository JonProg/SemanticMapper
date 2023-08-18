import spacy
from scipy import spatial

nlp_pt = spacy.load("pt_core_news_sm")
nlp_en = spacy.load("en_core_web_sm")

doc_pt = nlp_pt("Esta é uma frase para amar e falar.")
doc_en = nlp_en(input("Digite alguma frase em ingles:"))

user_vector = doc_en.vector

items = [
    nlp_en("book"),
    nlp_en("movie"),
    nlp_en("game"),
    nlp_en("marvel"),
    nlp_en("programing"),
    nlp_en("animes"),
]

item_vectors = []
for item in items:
    item_vectors.append(item[0].vector)

similarities = []
for vector in item_vectors:
    similarities.append(1 - spatial.distance.cosine(user_vector, vector))

heighest_similarity = max(similarities)
recommend = items[similarities.index(heighest_similarity)]

print(f"Based on your interests, I recommend a {recommend}")


#print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])


