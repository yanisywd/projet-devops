# Rapport de Robin BOURACHOT

## Description du code

On a dans `script.py` deux fonctions :
- `kn_documents` : cherche les `k` phrases les plus proches de `f` parmi les phrases du `document` ;
- `kn_documents` : cherche les `k` phrases les plus lointaines de `f` parmi les phrases du `document`.

Le fichier `utils.py` comporte toutes les fonctions utilitaires qui permettent à ces deux fonctions d'être exécutées, mais elles ne sont pas testées.

## Automatisation

L'exécution des tests requiert Python.

Les tests unitaires peuvent être executés avec la commande suivante :
```bash
python ./unit_tests.py -v # dans le dossier robin/
python robin/unit_tests.py -v # à la racine du projet
```

Un hook Git `pre-commit` est configuré de la manière suivante dans `.git/hooks/pre-commit`
```bash
python robin/unit_tests.py -v
```

## Tests unitaires

Soit le document constitué des phrases suivantes :
```
1. "Ceci est un point."
2. "Ceci est un autre point."
3. "Là, c'est une interrogation ?"
```

1. Pour la fonction `kn_documents`, on veut que la phrase la plus proche de la phrase 1 soit la phrase 2.
2. Pour la fonction `kf_documents`, on veut que la phrase la plus lointaine de la phrase 1 soit la phrase 3.
3. Pour la fonction `kn_documents`, on veut que la phrase la plus proche d'une nouvelle phrase "interrogation" soit la phrase 3.
4. Pour les fonctions `kn_documents` et `kf_documents`, on veut retourner au maximum les k plus proches/lointains voisins.
5. Pour les fonctions `kn_documents` et `kf_documents`, on veut obtenir une erreur `ValueError` lorsque k est supérieur au nombre de phrases dans le document.
5. Pour les fonctions `kn_documents` et `kf_documents`, on veut obtenir une erreur `TypeError` lorsque le document ou la phrase à recherche est de type invalide ou est une chaîne de caractères vide.

## Renforcements de code

- Les fonctions `kn_documents` et `kf_documents` ne gèrent pas un paramètre `k` invalide. (5)
- Les fonctions `kn_documents` et `kf_documents` ne gèrent pas des paramètres `document` ou `f` invalides. (6)
