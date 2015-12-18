"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of
locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly
once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.
"""
import unittest
from itertools import permutations


lines = [
    'Tristram to AlphaCentauri = 34',
    'Tristram to Snowdin = 100',
    'Tristram to Tambi = 63',
    'Tristram to Faerun = 108',
    'Tristram to Norrath = 111',
    'Tristram to Straylight = 89',
    'Tristram to Arbre = 132',
    'AlphaCentauri to Snowdin = 4',
    'AlphaCentauri to Tambi = 79',
    'AlphaCentauri to Faerun = 44',
    'AlphaCentauri to Norrath = 147',
    'AlphaCentauri to Straylight = 133',
    'AlphaCentauri to Arbre = 74',
    'Snowdin to Tambi = 105',
    'Snowdin to Faerun = 95',
    'Snowdin to Norrath = 48',
    'Snowdin to Straylight = 88',
    'Snowdin to Arbre = 7',
    'Tambi to Faerun = 68',
    'Tambi to Norrath = 134',
    'Tambi to Straylight = 107',
    'Tambi to Arbre = 40',
    'Faerun to Norrath = 11',
    'Faerun to Straylight = 66',
    'Faerun to Arbre = 144',
    'Norrath to Straylight = 115',
    'Norrath to Arbre = 135',
    'Straylight to Arbre = 127'
]


# lines = [
#     'London to Dublin = 464',
#     'London to Belfast = 518',
#     'Dublin to Belfast = 141'
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


def calculate_possible_destination_routes(locations):
    return [','.join(route) for route in permutations(locations)]


def parse_lines(lines=lines):
    locations = []
    distances = {}

    for line in lines:
        distance = parse_distance(line)
        if distance['from'] not in locations:
            locations.append(distance['from'])
        if distance['to'] not in locations:
            locations.append(distance['to'])
        distances[distance['from'] + ',' + distance['to']] = distance['distance']
        distances[distance['to'] + ',' + distance['from']] = distance['distance']

    return locations, distances


def parse_distance(line):
    splitup = line.split(' ')
    return {
        'from': splitup[0],
        'to': splitup[2],
        'distance': int(splitup[4])
    }


class SantaTests(unittest.TestCase):
    lines = [
        'London to Dublin = 464',
        'London to Belfast = 518',
        'Dublin to Belfast = 141'
    ]

    def test_breaking_up_distance_works(self):
        info = parse_distance(self.lines[0])
        self.assertEqual('London', info['from'])
        self.assertEqual('Dublin', info['to'])
        self.assertEqual(464, info['distance'])

    def test_parse_lines_returns_three_items_with_three_lines(self):
        self.assertEqual(3, len(parse_lines(self.lines)[0]))

    def test_calculate_possible_three_destination_routes_returns_possible_routes(self):
        routes = calculate_possible_destination_routes(parse_lines(self.lines)[0])
        self.assertEqual(6, len(routes))

    def test_calculate_route_distance_returns_correct_value(self):
        _, distances = parse_lines(self.lines)
        self.assertEqual(605, calculate_route_distance('London,Dublin,Belfast', distances))

    def test_calculate_route_distances_returns_correct_value(self):
        locations, distances = parse_lines(self.lines)
        routes = calculate_possible_destination_routes(locations)
        distances = calculate_route_distances(routes, distances)
        self.assertEqual(6, len(distances))
        self.assertEqual('Belfast,Dublin,London', min(distances, key=distances.get))


def main():
    locations, distances = parse_lines(lines)
    routes = calculate_possible_destination_routes(locations)
    distances = calculate_route_distances(routes, distances)

    shortest = min(distances, key=distances.get)
    longest = max(distances, key=distances.get)
    print 'Shortest distance is', distances[shortest]
    print 'Longest distance is', distances[longest]


main()
