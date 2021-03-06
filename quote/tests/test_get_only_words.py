import pytest

from ..services import get_only_words
from .quotes import (
    empty_quote,
    long_quote,
    normal_quote,
    punctuation_quote,
    short_quote,
)


@pytest.mark.django_db
class TestGetOnlyWords:
    def test_normal_quote(self):
        result = get_only_words(normal_quote)
        assert result == [
            "Keep",
            "your",
            "nose",
            "out",
            "the",
            "sky",
            "keep",
            "your",
            "heart",
            "to",
            "god",
            "and",
            "keep",
            "your",
            "face",
            "to",
            "the",
            "rising",
            "sun",
        ]

    def test_long_quote(self):
        result = get_only_words(long_quote)
        assert result == [
            "To",
            "talk",
            "of",
            "the",
            "size",
            "of",
            "a",
            "thought",
            "is",
            "odd",
            "perhaps",
            "but",
            "to",
            "say",
            "that",
            "someone",
            "is",
            "thinking",
            "big",
            "thoughts",
            "is",
            "not",
            "without",
            "meaning",
            "I",
            "want",
            "you",
            "all",
            "to",
            "come",
            "to",
            "my",
            "birthday",
            "party",
            "is",
            "a",
            "bigger",
            "thought",
            "than",
            "I",
            "want",
            "only",
            "some",
            "of",
            "you",
            "to",
            "come",
            "Bodhicitta",
            "is",
            "theoretically",
            "the",
            "biggest",
            "thought",
            "anyone",
            "can",
            "think",
            "because",
            "of",
            "the",
            "number",
            "of",
            "beings",
            "involved",
            "what",
            "it",
            "wants",
            "them",
            "to",
            "have",
            "and",
            "the",
            "length",
            "of",
            "time",
            "it",
            "must",
            "last",
            "before",
            "its",
            "motivating",
            "power",
            "dies",
            "out",
            "Since",
            "the",
            "duration",
            "of",
            "a",
            "thought",
            "is",
            "a",
            "variable",
            "of",
            "the",
            "aim",
            "in",
            "the",
            "sense",
            "that",
            "the",
            "actions",
            "motivated",
            "by",
            "a",
            "thought",
            "cease",
            "when",
            "the",
            "aim",
            "is",
            "attained",
            "one",
            "can",
            "conceive",
            "of",
            "thoughts",
            "that",
            "last",
            "longer",
            "and",
            "longer",
            "Bodhicitta",
            "necessarily",
            "lasts",
            "until",
            "the",
            "last",
            "living",
            "being",
            "reaches",
            "the",
            "state",
            "free",
            "of",
            "suffering",
            "because",
            "it",
            "is",
            "only",
            "then",
            "that",
            "the",
            "aim",
            "is",
            "finally",
            "achieved",
            "This",
            "explains",
            "the",
            "prayer",
            "of",
            "Samantabhadra",
            "at",
            "the",
            "end",
            "of",
            "the",
            "Gandavy??ha",
            "section",
            "of",
            "the",
            "Avata???saka",
            "S??tra",
            "which",
            "the",
            "Dalai",
            "Lama",
            "often",
            "invokes",
            "For",
            "as",
            "long",
            "as",
            "space",
            "endures",
            "may",
            "I",
            "remain",
            "to",
            "work",
            "for",
            "the",
            "benefit",
            "of",
            "living",
            "beings",
        ]

    def test_short_quote(self):
        result = get_only_words(short_quote)
        assert result == ["Speak", "God's", "truth", "to", "power"]

    def test_punctuation_quote(self):
        result = get_only_words(punctuation_quote)
        assert result == []

    def test_empty_quote(self):
        result = get_only_words(empty_quote)
        assert result == []
