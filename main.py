import requests
from vocabulary.vocabulary import Vocabulary as vb

# Users requests the definition of a word
def definition_request(word):

    response = vb.meaning(word)
    print(response)

# User requests synonyms of a word
def synonym_request(word):

    response = vb.synonym(word)
    print(response)


# Test here

# Valid word
definition_request('hello')
synonym_request('hello')

# Invalid word
definition_request('sdifsdf')
synonym_request('sdifsdf')
