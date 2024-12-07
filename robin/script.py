from utils import *


def kn_documents(document: str, k: int, f: str, descripteur=bow_occurences, distance=distance_cosinus):
    """
    Récupère les k plus proches documents par rapport à un document dans
    d'autres documents.
    """
    phrases = get_sentences(document)
    
    if k > len(phrases):
        raise ValueError('k est supérieur au nombre de phrases.')
    
    if k <= 0:
        raise ValueError('k est égal à 0 ou inférieur à 0.')
    
    if not isinstance(document, str) or not isinstance(f, str):
        raise TypeError('document et f doivent être des chaînes de caractères.')

    if document == '' or f == '':
        raise TypeError('document et f doivent être des chaînes de caractères non-vides.')

    doc = f'{f if f.endswith(sentence_punctuation) else f"{f}."}{document}'
    tokens = get_tokens(doc)
    tokens = enlever_doublons(clean_tokens(tokens))

    bow_matrix = descripteur(doc, tokens)
    distances = []

    for i in range(len(bow_matrix)):
        d1 = []
        for j in range(len(bow_matrix)):
            d1.append(distance(bow_matrix[i], bow_matrix[j]))
        distances.append(d1)

    distances_i = sorted(range(len(distances)), key=lambda x: distances[x])[1:] # Index des phrases les plus proches


    return [ (phrases[i - 1], distances[i]) for i in distances_i[:k] ]


def kf_documents(document: str, k: int, f: str, descripteur=bow_occurences, distance=distance_cosinus):
    """
    Récupère les k plus lointains documents par rapport à un document dans
    d'autres documents.
    """
    phrases = get_sentences(document)
    
    if k > len(phrases):
        raise ValueError('k est supérieur au nombre de phrases.')
    
    if k <= 0:
        raise ValueError('k est égal à 0 ou inférieur à 0.')
    
    if not isinstance(document, str) or not isinstance(f, str):
        raise TypeError('document et f doivent être des chaînes de caractères.')

    if document == '' or f == '':
        raise TypeError('document et f doivent être des chaînes de caractères non-vides.')

    doc = f'{f if f.endswith(sentence_punctuation) else f"{f}."}{document}'
    tokens = get_tokens(doc)
    tokens = enlever_doublons(clean_tokens(tokens))

    bow_matrix = descripteur(document, tokens)
    distances = []

    for i in range(len(bow_matrix)):
        d1 = []
        for j in range(len(bow_matrix)):
            d1.append(distance(bow_matrix[i], bow_matrix[j]))
        distances.append(d1)

    distances_i = sorted(range(len(distances)), key=lambda x: distances[x], reverse=True)[:k] # Index des phrases les plus lointaines

    return [ (phrases[i], distances[i]) for i in distances_i ]
