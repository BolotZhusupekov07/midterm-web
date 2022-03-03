from rest_framework import serializers

from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    """Serializer of Quote model."""

    class Meta:
        model = Quote
        fields = [
            "quote",
            "no_of_letters",
            "no_of_vowels",
            "no_of_consonants",
            "count_of_all_letters",
            "avg_len_of_words",
            "three_longest_words",
        ]
