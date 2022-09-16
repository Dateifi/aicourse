from BTtests.BinaryTree import BinaryTree
from collections import namedtuple

test_tree = BinaryTree()
Person = namedtuple('Person', ["Etternavn", "Fornavn", "Adresse", "Postnummer", "Poststed"])

with open("Personer15.dta", "r") as file:
    for line in file:
        test_person = Person(*line.strip().split(';'))
        test_tree.insert(value=test_person)


test_tree._root.prefixOrder()


"""Person(Etternavn='VESTLY SKIVIK', Fornavn='JAHN FREDRIK', Adresse='LINNGÅRD 22', Postnummer='1451',
                        Poststed='NESODDTANGEN'),
                 Person(Etternavn='NYMANN', Fornavn='ROY-ØYSTEIN', Adresse='HÅNESET 77', Postnummer='7033',
                        Poststed='TRONDHEIM'),
                 Person(Etternavn='ØSTBY', Fornavn='FRANK', Adresse='WÅRSETH 57', Postnummer='7414',
                        Poststed='TRONDHEIM'),
                 Person(Etternavn='LINNERUD', Fornavn='JOHNNY', Adresse='LÆRUM MELLEM 50', Postnummer='6507',
                        Poststed='KRISTIANSUND N'),
                 Person(Etternavn='REMLO', Fornavn='KIM ANDRE', Adresse='SANDFLATA 71', Postnummer='5648',
                        Poststed='HOLMEFJORD'),
                 Person(Etternavn='SKARSHAUG', Fornavn='ASBJØRN HARALD', Adresse='ALAPMO 72', Postnummer='7290',
                        Poststed='STØREN'),
                 Person(Etternavn='ELI', Fornavn='RITA HELEN', Adresse='MEHEIAVEGEN 80', Postnummer='4436',
                        Poststed='GYLAND'),
                 Person(Etternavn='ADOLFSEN', Fornavn='HACI', Adresse='VEDVIKA 94', Postnummer='1431', Poststed='ÅS'),
                 Person(Etternavn='HANSNES', Fornavn='ALF-EDVART', Adresse='FJÆRLIA 43', Postnummer='0349',
                        Poststed='OSLO'),
                 Person(Etternavn='TUVEN', Fornavn='FREDRIK FJELD', Adresse='JERVESTIEN 48', Postnummer='2822',
                        Poststed='BYBRUA'),
                 Person(Etternavn='MØRSVIK', Fornavn='RITA IREN', Adresse='RØEDSLETTA I 98', Postnummer='4460',
                        Poststed='MOI'),
                 Person(Etternavn='KVILE', Fornavn='JAN', Adresse='THOMASBRINKEN 56', Postnummer='3002',
                        Poststed='DRAMMEN')"""

