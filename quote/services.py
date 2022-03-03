import logging
import re
from collections import Counter
from string import punctuation
from typing import List

from .models import Quote

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("quote_services.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def remove_punc_and_space(text: str) -> str:
    """Return string without punctuation signs and spaces."""
    return re.sub(r"[^\w]", "", text)


def get_only_words(text: str) -> list:
    """Return string as list of words removing all punctuations."""
    words = [word.strip(punctuation) for word in text.split()]
    if len(words) == 1 and words[0] == "":
        return []
    return words


def get_no_of_vowels(freq_of_letters: dict) -> int:
    """Return count of vowels in a string."""
    count = 0
    for vowel in "aeiou":
        if vowel in freq_of_letters:
            count += freq_of_letters[vowel]
    return count


def get_no_of_consonants(freq_of_letters: dict) -> int:
    """Return count of consonants in a string."""
    count = 0
    for consonant in "bcdfghjklmnpqrstvwxyz":
        if consonant in freq_of_letters:
            count += freq_of_letters[consonant]
    return count


def get_avg_length_of_words(words: List[str]) -> float:
    """Return average length of words in a list."""
    len_of_words = [len(word) for word in words]
    if len_of_words:
        return sum(len_of_words) / len(len_of_words)
    return 0


def get_three_longest_words(words: List[str]) -> str:
    """Return three longest words in a list as a string."""
    words = list(set(words))
    words.sort(key=lambda item: (-len(item), item))
    result = ""
    if len(words) > 3:
        for place, word in enumerate(words[:3], start=1):
            result += f"{place}. {word}; "
    else:
        for place, word in enumerate(words, start=1):
            result += f"{place}. {word}; "
    return result.strip()


def get_or_create_quote(quote: str) -> Quote:
    """Return existing quote and its analysis or create and return."""
    if q := Quote.objects.filter(quote=quote).first():
        logger.info(f"Returned existing quote from database.: {quote}")
        return q

    try:
        words = get_only_words(quote)
        logger.info(f"List of words in a quote: {words}")

        modified_quote = remove_punc_and_space(quote).lower()
        logger.info(
            f"Quote after removing all punctuations and spaces: {modified_quote}"
        )

        freq_of_letters = dict(Counter(modified_quote))
        logger.info(f"Frequency of letters in the quote: {freq_of_letters}")

        no_of_letters = len(modified_quote)
        logger.info(f"len({modified_quote}) -> {no_of_letters}")

        no_of_vowels = get_no_of_vowels(freq_of_letters)
        logger.info(f"Number of vowels in the quote -> {no_of_vowels}")

        no_of_consonants = get_no_of_consonants(freq_of_letters)
        logger.info(f"Number of consonants in the quote -> {no_of_consonants}")

        avg_len_of_words = get_avg_length_of_words(words)
        logger.info(
            f"Average length of words in the quote -> {avg_len_of_words}"
        )

        three_longest_words = get_three_longest_words(words)
        logger.info(
            f"Three longest words in the quote -> {three_longest_words}"
        )

        q = Quote.objects.create(
            quote=quote,
            no_of_letters=no_of_letters,
            no_of_vowels=no_of_vowels,
            no_of_consonants=no_of_consonants,
            count_of_all_letters=freq_of_letters,
            avg_len_of_words=avg_len_of_words,
            three_longest_words=three_longest_words,
        )
        logger.info(f"Created quote analysis for quote: {quote}")

        return q

    except Exception as e:
        logger.exception(e)
        raise e
