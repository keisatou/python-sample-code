import counter

import pytest


class TestCounter(object):
    """test counter."""

    @pytest.mark.parametrize(('value', 'expected'), [
        (['hoge', 'hoge', 'hoge', 'fuga', 'fuga'], [('hoge', 3)]),
        (['a', 'a', 'b', 'b', 'a', 'a', 'c'], [('a', 4)]),
    ])
    def test_most_common(self, value, expected):
        result = counter.most_common(value)
        assert result == expected
