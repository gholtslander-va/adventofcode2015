"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy.
Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole
seconds in either state.

For example, suppose you have the following Reindeer:

Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while
Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a
total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second,
 when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer
has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the
winning reindeer traveled?
"""
import unittest

testinput = [
    'Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.',
    'Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.',
    'Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.',
    'Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.',
    'Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.',
    'Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.',
    'Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.',
    'Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.',
    'Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.'
]
race_seconds = 2503


def parse_line(line):
    split_line = line.split(' ')
    return {
        'name': split_line[0],
        'speed': int(split_line[3]),
        'time_running': int(split_line[6]),
        'rest': int(split_line[13]),
        'cycle_time': int(split_line[6]) + int(split_line[13])
    }


def calculate_distance_travelled(reindeer, race_time=race_seconds):
    total_distance = 0
    for second in range(0, race_time):
        total_distance += reindeer['speed'] if activity_at_second(reindeer, second) else 0

    return total_distance


def calculate_points_gathered(reindeer, race_time=race_seconds):
    # Reset point totals
    points = {reind['name']: 0 for reind in reindeer}
    distance = {reind['name']: 0 for reind in reindeer}
    for second in range(0, race_time):
        for reind in reindeer:
            distance[reind['name']] += reind['speed'] if activity_at_second(reind, second) else 0

        # Check for leaders.
        highest = [max(distance, key=distance.get)]
        for rein in distance.iterkeys():
            if distance[rein] > distance[highest[0]]:
                highest.remove(highest[0])
                highest.append(rein)
            elif distance[rein] == distance[highest[0]] and rein not in highest:
                highest.append(rein)

        for leader in highest:
            points[leader] += 1
        print second, points

    return points


def activity_at_second(reindeer, second):
    point_in_cycle = second % reindeer['cycle_time']
    if point_in_cycle < reindeer['time_running']:
        return True
    return False


class ReindeerTests(unittest.TestCase):
    def setUp(self):
        self.reindeer = parse_line('Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.')

    def test_parse_line_returns_correct_info(self):
        self.assertEqual('Vixen', self.reindeer['name'])
        self.assertEqual(18, self.reindeer['speed'])
        self.assertEqual(5, self.reindeer['time_running'])
        self.assertEqual(84, self.reindeer['rest'])

    def test_activity_at_second(self):
        self.assertTrue(activity_at_second(self.reindeer, 0))
        self.assertTrue(activity_at_second(self.reindeer, 4))
        self.assertFalse(activity_at_second(self.reindeer, 87))  # Running again

    def test_track_activity(self):
        reindeer = parse_line('Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.')
        distance = calculate_distance_travelled(reindeer, 1000)
        self.assertEqual(1056, distance)


# testinput = [
#     'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
#     'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'
# ]
# race_seconds = 1000
reindeer = [parse_line(line) for line in testinput]
# distances = {rein['name']: calculate_distance_travelled(rein, race_seconds) for rein in reindeer}
# print distances[max(distances, key=distances.get)]
points = calculate_points_gathered(reindeer, race_seconds)
print points
