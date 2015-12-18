"""
--- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password
based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for
security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step;
if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz.
They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are
therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

For example:

hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement
(because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).
The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi...,
since i is not allowed.
Given Santa's current password (your puzzle input), what should his next password be?

Your puzzle input is cqjxjnds.
"""
import unittest

import re

puzzle_input = 'cqjxjnds'


def has_straight_string(password):
    straights = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop',
                 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']
    return any([straight in password for straight in straights])


def has_no_forbidden_chars(password):
    return all([char not in password for char in ['i', 'o', 'l']])


def has_two_repeating_pairs(password):
    return len([m.group() for m in re.finditer(r'((\w)\2)', password)]) >= 2


def is_secure(password):
    return all([
        has_straight_string(password),
        has_no_forbidden_chars(password),
        has_two_repeating_pairs(password)
    ])


def increment_string(string):
    rollover = True
    new_string = ''
    for char in string[::-1]:
        if rollover:
            if char == 'z':
                char = 'a'
            else:
                char = chr(ord(char) + 1)
                rollover = False

        new_string += char

    return new_string[::-1]


def get_next_secure_password(password):
    while not is_secure(password):
        # Increment password string
        password = increment_string(password)

    return password


class PasswordTests(unittest.TestCase):
    def test_has_straight_string(self):
        self.assertTrue(has_straight_string('hijklmmn'))
        self.assertFalse(has_straight_string('hkifjkflfmfmn'))

    def test_has_no_forbidden_chars(self):
        self.assertTrue(has_no_forbidden_chars('ghjaabcc'))
        self.assertFalse(has_no_forbidden_chars('ghjaabcic'))

    def test_has_two_repeating_pairs(self):
        self.assertTrue(has_two_repeating_pairs('abcdffaa'))
        self.assertFalse(has_two_repeating_pairs('abcdfaaa'))

    def test_is_secure(self):
        self.assertTrue(is_secure('abcdffaa'))
        self.assertFalse(is_secure('abcdeffg'))

    def test_increment_password(self):
        self.assertEqual('ghijklmo', increment_string('ghijklmn'))
        self.assertEqual('ghijklna', increment_string('ghijklmz'))

    # def test_security_function(self):
    #     self.assertEqual('abcdffaa', get_next_secure_password('abcdefgh'))


# print get_next_secure_password(puzzle_input)  # cqjxxyzz
# print get_next_secure_password('cqjxxzaa')
