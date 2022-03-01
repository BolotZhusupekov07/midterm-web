import re
from string import ascii_lowercase, punctuation
from typing import List

from .models import Quote


def remove_punc_and_space(text: str) -> str:
    return re.sub(r"[^\w]", "", text)


def get_only_words(text: str) -> list:
    return [word.strip(punctuation) for word in text.split()]


def get_no_of_vowels(text: str) -> int:
    count = 0
    for vowel in "aeiou":
        count += text.count(vowel)
    return count


def get_no_of_consonants(text: str) -> int:
    count = 0
    for consonants in "bcdfghjklmnpqrstvwxyz":
        count += text.count(consonants)
    return count


def get_count_of_all_letters(text: str) -> dict:
    count_of_letters = {}
    for letter in ascii_lowercase:
        count_of_letters[letter] = text.count(letter)
    return count_of_letters


def get_avg_length_of_words(words: List[str]) -> float:
    len_of_words = [len(word) for word in words]
    return sum(len_of_words) / len(len_of_words)


def get_three_longest_words(words: List[str]) -> str:
    words = sorted(set(words), reverse=True, key=len)
    result = ""
    if len(words) > 3:
        for place, word in enumerate(words[:3], start=1):
            result += f"{place}. {word}; "
    else:
        for place, word in enumerate(words, start=1):
            result += f"{place}. {word}; "
    return result.strip()


def get_or_create_quote(quote: str) -> Quote:
    if q := Quote.objects.filter(quote=quote).first():
        return q

    words = get_only_words(quote)
    modified_quote = remove_punc_and_space(quote).lower()
    q = Quote.objects.create(
        quote=quote,
        no_of_letters=len(modified_quote),
        no_of_vowels=get_no_of_vowels(modified_quote),
        no_of_consonants=get_no_of_consonants(modified_quote),
        count_of_all_letters=get_count_of_all_letters(modified_quote),
        avg_len_of_words=get_avg_length_of_words(words),
        three_longest_words=get_three_longest_words(words),
    )
    return q
