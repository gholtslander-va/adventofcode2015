"""
--- Day 10: Elves Look, Elves Say ---

Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous
sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes
1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step,
take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit
itself (1).

For example:

1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).
Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?
"""
import unittest

test_input = '1113122113'


def look_say(number_string):
    number_string += ' '
    first = number_string[0]
    count = 1
    new_number = ''
    for number in list(number_string)[1:]:
        if first != number:
            new_number += str(count) + first
            count = 1
            first = number
        else:
            count += 1

    return new_number


class LookSayTests(unittest.TestCase):
    def test_one_becomes_one_one(self):
        self.assertEqual('11', look_say('1'))
        self.assertEqual('14', look_say('4'))

    def test_one_one_becomes_two_ones(self):
        self.assertEqual('21', look_say('11'))

    def test_two_one_becomes_one_two_two_ones(self):
        self.assertEqual('1211', look_say('21'))

    def test_other_scenarios(self):
        self.assertEqual('111221', look_say('1211'))
        self.assertEqual('312211', look_say('111221'))


# for i in range(0, 50):
#     test_input = look_say(test_input)
#
# print len(test_input)
