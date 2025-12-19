def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return 'un' + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended."""
    
    prefixo = vocab_words[0]
    lista = [prefixo]
    
    for word in vocab_words[1:]: 
        lista.append(prefixo + word)
    return ' :: '.join(lista)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind."""
    base = word[:-4]

    if base.endswith("i"):
        base = base[:-1] + "y"

    return base


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb"""

    new_sentence = sentence.split()[index]
    if new_sentence.endswith('.' or ',' or '!' or '?'):
        new_sentence = new_sentence[:-1]
    return new_sentence + 'en'
