import pytest

from ..services import remove_punc_and_space
from .quotes import (
    empty_quote,
    long_quote,
    normal_quote,
    punctuation_quote,
    short_quote,
)


@pytest.mark.django_db
class TestRemovePuncAndSpace:
    def test_normal_quote(self):
        result = remove_punc_and_space(normal_quote)
        assert (
            result
            == "Keepyournoseouttheskykeepyourhearttogodandkeepyourfacetotherisingsun"
        )

    def test_long_quote(self):

        result = remove_punc_and_space(long_quote)
        assert (
            result
            == """TotalkofthesizeofathoughtisoddperhapsbuttosaythatsomeoneisthinkingbigthoughtsisnotwithoutmeaningIwantyoualltocometomybirthdaypartyisabiggerthoughtthanIwantonlysomeofyoutocomeBodhicittaistheoreticallythebiggestthoughtanyonecanthinkbecauseofthenumberofbeingsinvolvedwhatitwantsthemtohaveandthelengthoftimeitmustlastbeforeitsmotivatingpowerdiesoutSincethedurationofathoughtisavariableoftheaiminthesensethattheactionsmotivatedbyathoughtceasewhentheaimisattainedonecanconceiveofthoughtsthatlastlongerandlongerBodhicittanecessarilylastsuntilthelastlivingbeingreachesthestatefreeofsufferingbecauseitisonlythenthattheaimisfinallyachievedThisexplainstheprayerofSamantabhadraattheendoftheGandavyūhasectionoftheAvataṃsakaSūtrawhichtheDalaiLamaofteninvokesForaslongasspaceenduresmayIremaintoworkforthebenefitoflivingbeings"""
        )

    def test_short_quote(self):
        result = remove_punc_and_space(short_quote)
        assert result == "SpeakGodstruthtopower"

    def test_punctuation_quote(self):
        result = remove_punc_and_space(empty_quote)
        assert result == ""

    def test_empty_quote(self):
        result = remove_punc_and_space(punctuation_quote)
        assert result == ""
