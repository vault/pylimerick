
from limerick import limerick
import unittest

poem1 = """\
A pointer to pointer to care,
got drunk one night on a dare.
Inverted its bits
and XOR'd its wits.
And points now to "memory err"."""


poem2 = """\
A pointer to pointer to char,
got drunk one night on a dare.
Inverted its bits
and XOR'd its wits.
And points now to "memory error"."""

poem3 = """\
The limerick packs laughs anatomical
In space that is quite economical.
But the good ones I've seen
So seldom are clean
And the clean ones so seldom are comical.
"""

poem4 = '''\
There was a young man of Japan
Whose limericks never would scan.
When asked why this was,
He replied "It's because
I always try to fit as many syllables \
into the last line as ever I possibly can."'''

poem5 = '''\
This is a poem
that is not a limerick
it is a haiku'''


class LimerickTest(unittest.TestCase):
    def setUp(self):
        self.poem1 = limerick(poem1)
        self.poem5 = limerick(poem5)

    def test_valid(self):
        self.assertTrue(self.poem1.valid)
        self.assertFalse(self.poem5.valid)


class MeterTest(unittest.TestCase):
    def setUp(self):
        self.poem1 = limerick(poem1)
        self.poem2 = limerick(poem2)
        self.poem3 = limerick(poem3)
        self.poem4 = limerick(poem4)

    def test_good_meter(self):
        self.assertFalse(self.poem4.good_meter)
        self.assertTrue(self.poem1.good_meter)

    def test_bad_lines(self):
        self.assertEqual(self.poem4.bad_lines, [5])
        self.assertEqual(self.poem1.bad_lines, [])


class RhymeTest(unittest.TestCase):
    def setUp(self):
        self.poem1 = limerick(poem1)
        self.poem2 = limerick(poem2)
        self.poem3 = limerick(poem3)
        self.poem4 = limerick(poem4)

    def test_good_rhyme(self):
        self.assertTrue(self.poem1.good_rhyme)
        self.assertTrue(self.poem3.good_rhyme)
        self.assertFalse(self.poem2.good_rhyme)
        self.assertTrue(self.poem3.good_rhyme)

    def test_bad_rhymes(self):
        self.assertTrue((1, 2) in self.poem2.rhyme_violations)
        self.assertTrue((1, 5) in self.poem2.rhyme_violations)
        self.assertEqual(self.poem1.rhyme_violations, [])


if __name__ == '__main__':
    unittest.main()
