
import numpy as np
from nltk_contrib.readability import syllables_en as syllables
from nltk.corpus import cmudict
from string import lowercase


target_meter = np.array([8, 8, 5, 5, 8])
valid_chars = lowercase + " \n"
rhyme_dict = cmudict.dict()


class LimerickInfo(object):
    def __init__(self, lim):
        self.limerick = lim
        self.lines = to_lines(lim)
        self.meter_violations = list(bad_lines(self.lines))
        self.rhyme_violations = bad_rhymes(self.lines)
        self.good_meter = good_meter(self.lines)
        self.good_rhyme = good_rhyme(self.lines)
        self.valid = good_limerick(self.lines)


def limerick(lim):
    return LimerickInfo(lim)


def count_syllables(lines):
    """Syllables in a line for each line"""
    return np.array(list(syllables.count(l) for l in lines))


def bad_lines(lines):
    """Returns a list of which lines are bad

    A line is bad if it's more than 1 syllable away from the target"""
    meter = count_syllables(lines)
    offby = abs(target_meter - meter)
    bad = offby > 2
    return np.arange(1, 6)[bad]


def good_meter(lines):
    return len(bad_lines(lines)) == 0


def do_rhyme(word1, word2):
    """Returns true if any combination of word pronuncations rhyme"""
    try:
        pron1 = rhyme_dict[word1.lower()]
        pron2 = rhyme_dict[word2.lower()]
    except KeyError:
        return False
    return any([prons_rhyme(p1, p2) for p1 in pron1 for p2 in pron2])


def prons_rhyme(pron1, pron2, count=2):
    """Returns true if a specific set of pronuncations rhyme"""
    suf1 = pron1[-1:-(1+count):-1]
    suf2 = pron2[-1:-(1+count):-1]
    return suf1 == suf2


def last_words(lines):
    return [line.split(' ')[-1] for line in lines]


def bad_rhymes(lines):
    ends = last_words(lines)
    bad = []
    if not do_rhyme(ends[2], ends[3]):
        bad.append((2, 3))
    if not do_rhyme(ends[0], ends[1]):
        bad.append((0, 1))
    if not do_rhyme(ends[1], ends[4]):
        bad.append((1, 4))
    if not do_rhyme(ends[0], ends[4]):
        bad.append((0, 4))
    return bad


def good_rhyme(lines):
    return len(bad_rhymes(lines)) == 0


def good_limerick(lines):
    if len(lines) != 5:
        return False
    if not good_rhyme(lines):
        return False
    if not good_meter(lines):
        return False
    return True


def normalize_text(text):
    return filter(lambda c: c in valid_chars, text.lower())


def to_lines(text):
    lines = normalize_text(text).splitlines()
    return [line.strip() for line in lines if len(line) > 4]
