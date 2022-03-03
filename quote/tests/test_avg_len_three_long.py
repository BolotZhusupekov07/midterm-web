import pytest

from ..services import (
    get_avg_length_of_words,
    get_only_words,
    get_three_longest_words,
)
from .quotes import (
    empty_quote,
    long_quote,
    normal_quote,
    punctuation_quote,
    short_quote,
)


@pytest.mark.django_db
class TestAverageLenAndThreeLongestWords:
    def test_normal_quote(self):
        words = get_only_words(normal_quote)
        average_length = get_avg_length_of_words(words)
        three_longest_words = get_three_longest_words(words)

        assert round(average_length, 2) == 3.58
        assert three_longest_words == "1. rising; 2. heart; 3. Keep;"

    def test_long_quote(self):
        words = get_only_words(long_quote)
        average_length = get_avg_length_of_words(words)
        three_longest_words = get_three_longest_words(words)

        assert round(average_length, 2) == 4.35
        assert (
            three_longest_words
            == "1. Samantabhadra; 2. theoretically; 3. necessarily;"
        )

    def test_short_quote(self):
        words = get_only_words(short_quote)
        average_length = get_avg_length_of_words(words)
        three_longest_words = get_three_longest_words(words)

        assert round(average_length, 2) == 4.40
        assert three_longest_words == "1. God's; 2. Speak; 3. power;"

    def test_punctuation_quote(self):
        words = get_only_words(punctuation_quote)
        average_length = get_avg_length_of_words(words)
        three_longest_words = get_three_longest_words(words)

        assert round(average_length, 2) == 0
        assert three_longest_words == ""

    def test_empty_quote(self):
        words = get_only_words(empty_quote)
        average_length = get_avg_length_of_words(words)
        three_longest_words = get_three_longest_words(words)

        assert round(average_length, 2) == 0
        assert three_longest_words == ""
