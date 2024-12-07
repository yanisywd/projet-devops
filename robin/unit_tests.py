import textwrap
import unittest

from script import *


document = textwrap.dedent('''
    Ceci est un point.
    Ceci est un autre point.
    Là, c'est une interrogation ?
''')

class TestMethods(unittest.TestCase):
    def test_1_phrase_plus_proche(self):
        assert kn_documents(document, 2, 'Ceci est un point.')[1][0] == 'Ceci est un autre point.'

    def test_2_phrase_plus_lointaine(self):
        assert kf_documents(document, 1, 'Ceci est un point.')[0][0] == 'Là, c\'est une interrogation ?'

    def test_3_phrase_plus_proche_hors_document(self):
        assert kn_documents(document, 1, 'interrogation')[0][0] == 'Là, c\'est une interrogation ?'

    def test_4_maximum_k_voisins(self):
        for k in range(1, 4):
            assert len(kn_documents(document, k, 'point')) == k
    
    def test_5_valueerror_k_invalide(self):
        for fonction in [kn_documents, kf_documents]:
            for k in [0, 4]:
                with self.assertRaises(ValueError):
                    fonction(document, k, 'Autre phrase')

    def test_6_valueerror_phrase_invalide(self):
        for fonction in [kn_documents, kf_documents]:
            for phrase in [0, '']:
                with self.assertRaises(TypeError):
                    fonction(document, 1, phrase)


if __name__ == '__main__':
    unittest.main()
