def print_upper_words(words):
    """Print each word in a list, uppercased

      >>> print_upper_words(['dog', 'cat', 'bird', 'fish'])

      DOG
      CAT
      BIRD
      FISH
    """
    for word in words:
        print('word'.upper())


def print_upper_words_2(words):
    """Print each word in a list if it starts with E or e, uppercased

    >>> print_upper_words_2(['eagle', 'dog', 'cat', 'Emu'])

    EAGLE
    EMU
    """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """Print each word in a list if it starts with a given letter(s)

    >>> print_upper_words3(["eagle", "Edward", "Alfred", "zope"], must_start_with=["A", "E"])
          EDWARD
          ALFRED
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
