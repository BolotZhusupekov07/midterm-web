from collections import Counter

import pytest

from ..services import (
    get_no_of_consonants,
    get_no_of_vowels,
    remove_punc_and_space,
)
from .quotes import (
    empty_quote,
    long_quote,
    normal_quote,
    punctuation_quote,
    short_quote,
)


@pytest.mark.django_db
class TestNoOfVowelsConsonantsLettersFreq:
    def test_normal_quote(self):
        modified_quote = remove_punc_and_space(normal_quote).lower()
        freq_of_letters = dict(Counter(modified_quote))
        no_of_vowels = get_no_of_vowels(freq_of_letters)
        no_of_consonants = get_no_of_consonants(freq_of_letters)
        no_of_letters = len(modified_quote)
        assert no_of_letters == 68
        assert no_of_vowels == 29
        assert no_of_consonants == 39
        assert freq_of_letters == {
            "a": 3,
            "c": 1,
            "d": 2,
            "e": 11,
            "f": 1,
            "g": 2,
            "h": 3,
            "i": 2,
            "k": 4,
            "n": 4,
            "o": 8,
            "p": 3,
            "r": 5,
            "s": 4,
            "t": 6,
            "u": 5,
            "y": 4,
        }

    def test_long_quote(self):
        modified_quote = remove_punc_and_space(long_quote).lower()
        freq_of_letters = dict(Counter(modified_quote))
        no_of_vowels = get_no_of_vowels(freq_of_letters)
        no_of_consonants = get_no_of_consonants(freq_of_letters)
        no_of_letters = len(modified_quote)
        assert no_of_letters == 810
        assert no_of_vowels == 314
        assert no_of_consonants == 493
        assert freq_of_letters == {
            "a": 79,
            "b": 18,
            "c": 20,
            "d": 18,
            "e": 85,
            "f": 23,
            "g": 26,
            "h": 58,
            "i": 67,
            "k": 6,
            "l": 26,
            "m": 19,
            "n": 55,
            "o": 63,
            "p": 7,
            "r": 25,
            "s": 51,
            "t": 101,
            "u": 20,
            "v": 13,
            "w": 9,
            "x": 1,
            "y": 16,
            "z": 1,
            "ū": 2,
            "ṃ": 1,
        }

    def test_short_quote(self):
        modified_quote = remove_punc_and_space(short_quote).lower()
        freq_of_letters = dict(Counter(modified_quote))
        no_of_vowels = get_no_of_vowels(freq_of_letters)
        no_of_consonants = get_no_of_consonants(freq_of_letters)
        no_of_letters = len(modified_quote)
        assert no_of_letters == 21
        assert no_of_vowels == 7
        assert no_of_consonants == 14
        assert freq_of_letters == {
            "a": 1,
            "d": 1,
            "e": 2,
            "g": 1,
            "h": 1,
            "k": 1,
            "o": 3,
            "p": 2,
            "r": 2,
            "s": 2,
            "t": 3,
            "u": 1,
            "w": 1,
        }

    def test_punctuation_quote(self):
        modified_quote = remove_punc_and_space(punctuation_quote).lower()
        freq_of_letters = dict(Counter(modified_quote))
        no_of_vowels = get_no_of_vowels(freq_of_letters)
        no_of_consonants = get_no_of_consonants(freq_of_letters)
        no_of_letters = len(modified_quote)
        assert no_of_letters == 0
        assert freq_of_letters == {}
        assert no_of_vowels == 0
        assert no_of_consonants == 0

    def test_empty_quote(self):
        modified_quote = remove_punc_and_space(empty_quote).lower()
        freq_of_letters = dict(Counter(modified_quote))
        no_of_vowels = get_no_of_vowels(freq_of_letters)
        no_of_consonants = get_no_of_consonants(freq_of_letters)
        no_of_letters = len(modified_quote)
        assert no_of_letters == 0
        assert freq_of_letters == {}
        assert no_of_vowels == 0
        assert no_of_consonants == 0
