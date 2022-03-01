from django.db import models


class Quote(models.Model):
    quote = models.TextField()
    no_of_letters = models.IntegerField()
    no_of_vowels = models.IntegerField()
    no_of_consonants = models.IntegerField()
    count_of_all_letters = models.JSONField()
    avg_len_of_words = models.DecimalField(decimal_places=2, max_digits=10)
    three_longest_words = models.CharField(max_length=250)
