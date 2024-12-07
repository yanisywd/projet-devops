from utils import *


def kn_documents(document: str, k: int, f: str, descripteur=bow_occurences, distance=distance_manhattan, stopwords=None):
    """
    Récupère les k plus proches documents par rapport à un document dans
    d'autres documents.
    """

    doc = f'{f if f.endswith(sentence_punctuation) else f"{f}."}{document}'
    tokens = get_tokens(doc)
    tokens = enlever_doublons(clean_tokens(tokens, stopwords))

    bow_matrix = descripteur(document, tokens)
    distances = []

    for i in range(len(bow_matrix)):
        d1 = []
        for j in range(len(bow_matrix)):
            d1.append(distance(bow_matrix[i], bow_matrix[j]))
        distances.append(d1)

    distances_i = sorted(range(len(distances)), key=lambda x: distances[x])[1:(k + 1)] # Index des phrases les plus proches

    phrases = get_sentences(doc)

    return [ (phrases[i], distances[i]) for i in distances_i ]


def kf_documents(document: str, k: int, f: str, descripteur=bow_occurences, distance=distance_manhattan, stopwords=None):
    """
    Récupère les k plus lointains documents par rapport à un document dans
    d'autres documents.
    """

    doc = f'{f if f.endswith(sentence_punctuation) else f"{f}."}{document}'
    tokens = get_tokens(doc)
    tokens = enlever_doublons(clean_tokens(tokens, stopwords))

    bow_matrix = descripteur(document, tokens)
    distances = []

    for i in range(len(bow_matrix)):
        d1 = []
        for j in range(len(bow_matrix)):
            d1.append(distance(bow_matrix[i], bow_matrix[j]))
        distances.append(d1)

    distances_i = sorted(range(len(distances)), key=lambda x: distances[x], reverse=True)[:k] # Index des phrases les plus proches

    phrases = get_sentences(doc)

    return [ (phrases[i], distances[i]) for i in distances_i ]


if __name__ == '__main__':
    pass
