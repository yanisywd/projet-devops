import math
import re
import string

from typing import Callable


TOKENIZER = 'custom'
sentence_punctuation = ('.', '?', '!')
token_regex = re.compile(f'[ \n{re.escape(string.punctuation)}]')
sentence_regex = re.compile(r'(\\.+|[\\.!?])')


def get_tokens(document: str):
    """
    Récupère tous les mots d'une chaîne de caractère.
    """
    return re.split(token_regex, document)


def clean_tokens(tokens: list[str], stopwords: str | None = None):
    """
    Nettoie tous les tokens, en filtrant les stopwords si nécessaire.
    """
    tokens = [ t.lower() for t in tokens if t is not None and t != '' ]

    return tokens


def enlever_doublons(tokens: list[str]):
    """
    Enlève tous les doublons d'une liste.

    Fonction copiée du code de Raphaëlle pour qu'on ait les mêmes résultats.
    """
    s = set()
    ta = []
    for t in tokens:
        if t not in s:
            s.add(t)
            ta.append(t)

    return ta


def get_sentences(document: str):
    """
    Récupère toutes les phrases d'un corpus.
    """
    # Supprime les phrases vides, puis sépare les phrases et enlève les caractères superflus.
    s1 = re.split(sentence_regex, document)
    
    # Puisqu'on a voulu garder la ponctuation dans notre expression régulière,
    # on a une liste avec les phrases et leur ponctuation de fin. On veut
    # rassembler ces paires.
    s2 = [ y for i in range(len(s1) // 2) if (y := ''.join(s1[(i * 2):(i * 2 + 2)]).strip()) != '' ]

    return s2


def get_clean_sentences(document: str):
    """
    Récupère toutes les phrases d'un corpus, avec des tokens nettoyés.
    """
    # Supprime les phrases vides, puis sépare les phrases et enlève les caractères superflus.
    return [ clean_tokens(get_tokens(sentence)) for sentence in get_sentences(document) ]


def count_sentences(document: str):
    """
    Compte le nombre de phrases dans un corpus donné.
    """
    return len(get_sentences(document))


def compter_mots_dans_phrase(phrase: str):
    """
    Compte le nombre de mots distincts et leur nombre d'occurences dans une
    phrase donnée.
    """
    d = {}
    for sentence in get_sentences(phrase):
        for mot in sentence.split(' '):
            mot = mot.strip(string.punctuation)
            if mot not in d:
                d[mot] = 0
            d[mot] += 1
    
    return d


def compter_mots_dans_phrases(document: str):
    """
    Compte le nombre de mots distincts et leur nombre d'occurences dans chaque
    phrase du corpus donné.
    """
    return [ compter_mots_dans_phrase(phrase) for phrase in get_sentences(document) ]


def bow(document: str, tokens: list[str], evaluator: Callable[[str, list[str]], int]):
    """
    Fonction générique qui génère une matrice (liste de vecteurs) pour chaque
    phrase du corpus et chaque mot différent du corpus.
    """
    table = []
    for sentence in get_sentences(document):
        words = clean_tokens(get_tokens(sentence))
        table.append([ evaluator(t, words) for t in tokens ])
    
    return table


def bow_occurences(document: str, tokens: list[str]):
    """
    Génère une matrice qui compte le nombre d'occurences de chaque mot
    différent trouvé dans le corpus dans chaque phrase du corpus.
    """
    return bow(document, tokens, lambda t, w: w.count(t))


def bow_binaire(document: str, tokens: list[str]):
    """
    Génère une matrice qui détermine si chacun des mots trouvés dans le corpus
    sont présents dans chacune des phrases du corpus.
    """
    return bow(document, tokens, lambda t, w: int(t in w))


def bow_proba(document: str, tokens: list[str]):
    """
    Génère une matrice qui calcule la fréquence d'apparition de chaque token
    dans chacune des phrases du corpus.
    """
    return bow(document, tokens, lambda t, w: w.count(t) / len(w))


def tf_idf(document: str, tokens: list[str], evaluator: Callable[[str, list[str]], int]):
    """
    TF-IDF.
    """
    apparitions = {}
    for sentence in (sentences := get_clean_sentences(document)):
        # Avec les bag-of-words, on calculait le nombre d'apparitions de chaque
        # tokens au sein d'une seule et même phrase. Ici, on veut calculer le
        # nombre de phrases dans lesquels apparaît chaque token, on ne comptant
        # qu'une seule fois le même token pour chacune des phrases.
        for token in enlever_doublons(sentence):
            if token not in apparitions:
                apparitions[token] = 0
            if token in sentence:
                apparitions[token] += 1

    table = []
    for sentence in sentences:
        table.append([ evaluator(sentence, t) * math.log(len(sentences) / apparitions[t], 10) for t in tokens if t in apparitions ])
    
    return table


def tf_idf_binaire(document: str, tokens: list[str]):
    return tf_idf(document, tokens, lambda w, t: int(t in w))


def tf_idf_occurrences(document: str, tokens: list[str]):
    return tf_idf(document, tokens, lambda w, t: w.count(t))


def tf_idf_proba(document: str, tokens: list[str]):
    return tf_idf(document, tokens, lambda w, t: w.count(t) / len(w))


def tf_idf_new(document: str, tokens: list[str]):
    apparitions = {}
    for sentence in (sentences := get_clean_sentences(document)):
        for token in enlever_doublons(sentence):
            if token not in apparitions:
                apparitions[token] = 0
            if token in sentence:
                apparitions[token] += 1

    table = []
    for sentence in sentences:
        table.append([ (math.log2(1 + sentence.count(t)) / math.log2(len(sentence))) * math.log10(1 + len(sentences) / apparitions[t]) for t in tokens if t in apparitions ])
    
    return table


def bow_norme(document: str, tokens: list[str]):
    """
    Génère une matrice qui calcule la norme avec tous les tokens pour chacune
    des phrases du corpus.
    """
    table = []
    for sentence in get_sentences(document):
        words = clean_tokens(get_tokens(sentence))

        norme = math.sqrt(sum([ words.count(t) ** 2 for t in tokens ]))
        table.append([ words.count(t) / norme for t in tokens ])
    
    return table


def distance_euclidienne(v1: list[int], v2: list[int]):
    """
    Calcule la distance euclidienne entre deux vecteurs donnés.
    """
    return math.sqrt(sum([ (v1[k] - v2[k]) ** 2 for k in range(len(v1)) ]))


def distance_manhattan(v1: list[int], v2: list[int]):
    """
    Calcule la distance de Manhattan entre deux vecteurs donnés.
    """
    return sum([ abs(v1[k] - v2[k]) for k in range(len(v1)) ])


def distance_cosinus(v1: list[int], v2: list[int]):
    """
    Calcule la distance cosinus entre deux vecteurs donnés.
    """
    produit_scalaire = sum([ v1[i] * v2[i] for i in range(len(v1)) ])
    norme_v1 = math.sqrt(sum([ i ** 2 for i in v1 ]))
    norme_v2 = math.sqrt(sum([ i ** 2 for i in v2 ]))

    return (1 - produit_scalaire / (norme_v1 * norme_v2))


def distance_jaccard(v1: list[int], v2: list[int]):
    """
    Calcule la distance de Jaccard entre deux vecteurs donnés.
    """
    intersect = sum([ v1[i] > 0 and v2[i] > 0 for i in range(len(v1)) ])
    union = sum([ v1[i] > 0 or v2[i] > 0 for i in range(len(v1)) ])

    return 1 - (intersect / union)


def distance_hamming(v1: list[int], v2: list[int]):
    """
    Calcule la distance de Hamming entre deux vecteurs donnés.
    """
    return sum([ 1 for i in range(len(v1)) if v1[i] != v2[i] ])


def distance_bray_curtis(v1: list[int], v2: list[int]):
    """
    Calcule la distance de Bray-Curtis entre deux vecteurs donnés.
    """
    num = sum([ abs(v1[i] - v2[i]) for i in range(len(v1)) ])
    den = sum([ v1[i] + v2[i] for i in range(len(v1)) ])

    return num / den


def divergence_kullback_leibler(v1: list[int], v2: list[int]):
    """
    Calcule la divergence de Kullback-Leibler entre deux vecteurs donnés.
    """
    return sum([ v1[i] * math.log((v1[i] + 10 ** -5) / (v2[i] + 10 ** -5)) for i in range(len(v1)) ])
