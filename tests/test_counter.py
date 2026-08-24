import unittest

from wordtools.counter import count_words


class CounterTests(unittest.TestCase):
    def test_count_words_two_words_returns_two(self) -> None:
        self.assertEqual(count_words("hello world"), 2)
