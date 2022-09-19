import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec


loaded_model = Word2Vec.load("models/version_0.2.model").wv


class DhivehiNewsClassifier:
    def vectorize(title):
        vocabulary = loaded_model.index_to_key
        w2v_word = np.zeros(100, dtype="float32")
        for word in title.split():
            if word in vocabulary:
                w2v_word = np.add(w2v_word, loaded_model[word])
        w2v_word = np.divide(w2v_word, len(title.split()))
        return w2v_word

    def compare_titles(original_title, comparing_titles):
        title_data = []
        for title in comparing_titles.strip().split("\n"):
            similarity = cosine_similarity(
                [DhivehiNewsClassifier.vectorize(original_title)],
                [DhivehiNewsClassifier.vectorize(title)],
            )
            # append title and similarity score to title_data
            title_data.append({"title": title, "similarity": float(similarity[0][0])})
        sorted_title_data = sorted(title_data, key=lambda y: y["similarity"], reverse=True)
        # update sorted_title_data to change similary to 2 decimal places
        for title in sorted_title_data:
            title["similarity"] = round(title["similarity"], 2)

        return sorted_title_data
