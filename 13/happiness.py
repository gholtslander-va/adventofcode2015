"""
--- Day 13: Knights of the Dinner Table ---

In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83
After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?
"""
import unittest
from itertools import permutations

testinput = [
    'Alice would gain 54 happiness units by sitting next to Bob.',
    'Alice would lose 81 happiness units by sitting next to Carol.',
    'Alice would lose 42 happiness units by sitting next to David.',
    'Alice would gain 89 happiness units by sitting next to Eric.',
    'Alice would lose 89 happiness units by sitting next to Frank.',
    'Alice would gain 97 happiness units by sitting next to George.',
    'Alice would lose 94 happiness units by sitting next to Mallory.',
    'Alice would gain 0 happiness units by sitting next to Graham.',
    'Bob would gain 3 happiness units by sitting next to Alice.',
    'Bob would lose 70 happiness units by sitting next to Carol.',
    'Bob would lose 31 happiness units by sitting next to David.',
    'Bob would gain 72 happiness units by sitting next to Eric.',
    'Bob would lose 25 happiness units by sitting next to Frank.',
    'Bob would lose 95 happiness units by sitting next to George.',
    'Bob would gain 11 happiness units by sitting next to Mallory.',
    'Bob would gain 0 happiness units by sitting next to Graham.',
    'Carol would lose 83 happiness units by sitting next to Alice.',
    'Carol would gain 8 happiness units by sitting next to Bob.',
    'Carol would gain 35 happiness units by sitting next to David.',
    'Carol would gain 10 happiness units by sitting next to Eric.',
    'Carol would gain 61 happiness units by sitting next to Frank.',
    'Carol would gain 10 happiness units by sitting next to George.',
    'Carol would gain 29 happiness units by sitting next to Mallory.',
    'Carol would gain 0 happiness units by sitting next to Graham.',
    'David would gain 67 happiness units by sitting next to Alice.',
    'David would gain 25 happiness units by sitting next to Bob.',
    'David would gain 48 happiness units by sitting next to Carol.',
    'David would lose 65 happiness units by sitting next to Eric.',
    'David would gain 8 happiness units by sitting next to Frank.',
    'David would gain 84 happiness units by sitting next to George.',
    'David would gain 9 happiness units by sitting next to Mallory.',
    'David would gain 0 happiness units by sitting next to Graham.',
    'Eric would lose 51 happiness units by sitting next to Alice.',
    'Eric would lose 39 happiness units by sitting next to Bob.',
    'Eric would gain 84 happiness units by sitting next to Carol.',
    'Eric would lose 98 happiness units by sitting next to David.',
    'Eric would lose 20 happiness units by sitting next to Frank.',
    'Eric would lose 6 happiness units by sitting next to George.',
    'Eric would gain 60 happiness units by sitting next to Mallory.',
    'Eric would gain 0 happiness units by sitting next to Graham.',
    'Frank would gain 51 happiness units by sitting next to Alice.',
    'Frank would gain 79 happiness units by sitting next to Bob.',
    'Frank would gain 88 happiness units by sitting next to Carol.',
    'Frank would gain 33 happiness units by sitting next to David.',
    'Frank would gain 43 happiness units by sitting next to Eric.',
    'Frank would gain 77 happiness units by sitting next to George.',
    'Frank would lose 3 happiness units by sitting next to Mallory.',
    'Frank would gain 0 happiness units by sitting next to Graham.',
    'George would lose 14 happiness units by sitting next to Alice.',
    'George would lose 12 happiness units by sitting next to Bob.',
    'George would lose 52 happiness units by sitting next to Carol.',
    'George would gain 14 happiness units by sitting next to David.',
    'George would lose 62 happiness units by sitting next to Eric.',
    'George would lose 18 happiness units by sitting next to Frank.',
    'George would lose 17 happiness units by sitting next to Mallory.',
    'George would gain 0 happiness units by sitting next to Graham.',
    'Graham would gain 0 happiness units by sitting next to Alice.',
    'Graham would gain 0 happiness units by sitting next to Bob.',
    'Graham would gain 0 happiness units by sitting next to Carol.',
    'Graham would gain 0 happiness units by sitting next to David.',
    'Graham would gain 0 happiness units by sitting next to Eric.',
    'Graham would gain 0 happiness units by sitting next to Frank.',
    'Graham would gain 0 happiness units by sitting next to George.',
    'Graham would gain 0 happiness units by sitting next to Mallory.',
    'Mallory would lose 36 happiness units by sitting next to Alice.',
    'Mallory would gain 76 happiness units by sitting next to Bob.',
    'Mallory would lose 34 happiness units by sitting next to Carol.',
    'Mallory would gain 37 happiness units by sitting next to David.',
    'Mallory would gain 40 happiness units by sitting next to Eric.',
    'Mallory would gain 18 happiness units by sitting next to Frank.',
    'Mallory would gain 7 happiness units by sitting next to George.',
    'Mallory would gain 0 happiness units by sitting next to Graham.',
]


# testinput = [
#     'Alice would gain 54 happiness units by sitting next to Bob.',
#     'Alice would lose 79 happiness units by sitting next to Carol.',
#     'Alice would lose 2 happiness units by sitting next to David.',
#     'Bob would gain 83 happiness units by sitting next to Alice.',
#     'Bob would lose 7 happiness units by sitting next to Carol.',
#     'Bob would lose 63 happiness units by sitting next to David.',
#     'Carol would lose 62 happiness units by sitting next to Alice.',
#     'Carol would gain 60 happiness units by sitting next to Bob.',
#     'Carol would gain 55 happiness units by sitting next to David.',
#     'David would gain 46 happiness units by sitting next to Alice.',
#     'David would lose 7 happiness units by sitting next to Bob.',
#     'David would gain 41 happiness units by sitting next to Carol.',
# ]


def calculate_route_distance(route, distances):
    distance = 0

    destinations = route.split(',')

    stop = destinations[0]

    for counter in range(1, len(destinations)):
        next_stop = destinations[counter]
        distance += distances[stop + ',' + next_stop]
        stop = next_stop

    return distance


def calculate_route_distances(routes, distances):
    return {route: calculate_route_distance(route, distances) for route in routes}


def calculate_two_way_happiness(routes, distances):
    twoways = {}
    for route in routes:
        there = calculate_route_distance(route, distances)
        back = calculate_route_distance(','.join(route.split(',')[::-1]), distances)
        twoways[route] = there + back

    return twoways


def calculate_possible_destination_routes(locations):
    return [','.join(route) for route in permutations(locations)]


def add_ends(routes):
    """ Need to add the last "seat" as it were. """
    new_routes = []
    for route in routes:
        route_split = route.split(',')
        route_split.append(route_split[0])
        route_list = ','.join(route_split)
        new_routes.append(route_list)

    return new_routes


def parse_lines(lines=testinput):
    people = []
    happiness = {}

    for line in lines:
        happyfactor = parse_happiness(line)
        if happyfactor['from'] not in people:
            people.append(happyfactor['from'])
        if happyfactor['to'] not in people:
            people.append(happyfactor['to'])
        happiness[happyfactor['from'] + ',' + happyfactor['to']] = happyfactor['happiness']

    return people, happiness


def parse_happiness(line):
    splitup = line.split(' ')
    return {
        'from': splitup[0],
        'to': splitup[10][:-1],
        'happiness': -(int(splitup[3])) if splitup[2] == 'lose' else int(splitup[3])
    }


# class SantaTests(unittest.TestCase):
#     lines = [
#         'Alice would gain 54 happiness units by sitting next to Bob.',
#         'Alice would lose 79 happiness units by sitting next to Carol.',
#         'Alice would lose 2 happiness units by sitting next to David.',
#         'Bob would gain 83 happiness units by sitting next to Alice.',
#         'Bob would lose 7 happiness units by sitting next to Carol.',
#         'Bob would lose 63 happiness units by sitting next to David.',
#         'Carol would lose 62 happiness units by sitting next to Alice.',
#         'Carol would gain 60 happiness units by sitting next to Bob.',
#         'Carol would gain 55 happiness units by sitting next to David.',
#         'David would gain 46 happiness units by sitting next to Alice.',
#         'David would lose 7 happiness units by sitting next to Bob.',
#         'David would gain 41 happiness units by sitting next to Carol.'
#     ]
#
#     def test_breaking_up_distance_works(self):
#         info = parse_happiness(self.lines[0])
#         self.assertEqual('Alice', info['from'])
#         self.assertEqual('Bob', info['to'])
#         self.assertEqual(54, info['happiness'])
#         info = parse_happiness(self.lines[1])
#         self.assertEqual('Alice', info['from'])
#         self.assertEqual('Carol', info['to'])
#         self.assertEqual(-79, info['happiness'])
#
#     def test_parse_lines_returns_four_people_with_four_lines(self):
#         self.assertEqual(4, len(parse_lines(lines=self.lines)[0]))  # (people, distances)[0]
#
#     def test_calculate_possible_destination_routes_returns_possible_routes(self):
#         routes = calculate_possible_destination_routes(parse_lines(self.lines)[0])
#         self.assertEqual(24, len(routes))
#
#     def test_calculate_route_distance_returns_correct_value(self):
#         _, distances = parse_lines(self.lines)
#         self.assertEqual(148, calculate_route_distance('Alice,Bob,Carol,David,Alice', distances))
#
#     def test_add_ends_works(self):
#         routes = add_ends(['Alice,Bob,Carol,David'])
#         self.assertEqual('Alice,Bob,Carol,David,Alice', routes[0])
#
#     def test_calculate_route_distances_returns_correct_value(self):
#         locations, distances = parse_lines(self.lines)
#         routes = calculate_possible_destination_routes(locations)
#         routes = add_ends(routes)
#         distances = calculate_route_distances(routes, distances)
#         print distances
#         self.assertEqual(24, len(distances))
#         self.assertEqual('Bob,Alice,David,Carol,Bob', max(distances, key=distances.get))
#
#     def test_calculate_two_way_happiness_returns_proper_value(self):
#         locations, distances = parse_lines(self.lines)
#         routes = calculate_possible_destination_routes(locations)
#         routes = add_ends(routes)
#         distances = calculate_two_way_happiness(routes, distances)
#         self.assertEqual(330, distances[max(distances, key=distances.get)])


def main():
    locations, distances = parse_lines(testinput)
    routes = calculate_possible_destination_routes(locations)
    routes = add_ends(routes)
    distances = calculate_two_way_happiness(routes, distances)

    longest = max(distances, key=distances.get)
    print 'Most happiness is', distances[longest]
    print 'Happiest arrangement being:', longest
    print 'All arrangements:', distances


main()
