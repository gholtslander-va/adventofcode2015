"""
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right
 balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you
 could use to finish the recipe (your puzzle input) and their properties per teaspoon:

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce
 your results in the future. The total score of a cookie can be found by adding up each of the properties (negative
 totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient
 must add up to 100) would result in a cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76
Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which
 happens to be the best score possible given these ingredients. If any properties had produced a negative total, it
 would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you
 can make?
"""
import itertools

test_input = [
    'Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5',
    'Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8',
    'Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6',
    'Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1'
]

test_input_dict = {
    'frosting': {
        'capacity': 4,
        'durability': -2,
        'flavor': 0,
        'texture': 0,
        'calories': 5
    },
    'candy': {
        'capacity': 0,
        'durability': 5,
        'flavor': -1,
        'texture': 0,
        'calories': 8
    },
    'butterscotch': {
        'capacity': -1,
        'durability': 0,
        'flavor': 5,
        'texture': 0,
        'calories': 6
    },
    'sugar': {
        'capacity': 0,
        'durability': 0,
        'flavor': -2,
        'texture': 2,
        'calories': 1
    },
}

test_input_dict = {
    'butterscotch': {
        'capacity': -1,
        'durability': -2,
        'flavor': 6,
        'texture': 3,
        'calories': 8
    },
    'cinnamon': {
        'capacity': 2,
        'durability': 3,
        'flavor': -2,
        'texture': -1,
        'calories': 3
    },
}


INGREDIENT_PROPERTIES = [
    'capacity', 'durability', 'flavor', 'texture', 'calories'
]


def calculate_property(ingredient_property, num_frosting, num_candy, num_butterscotch, num_sugar):
    return sum([
        num_frosting * test_input_dict['frosting'][ingredient_property],
        num_candy * test_input_dict['candy'][ingredient_property],
        num_butterscotch * test_input_dict['butterscotch'][ingredient_property],
        num_sugar * test_input_dict['sugar'][ingredient_property]
    ])


def calculate_test_property(ingredient_property, num_butterscotch, num_cinnamon):
    return sum([
        num_butterscotch * test_input_dict['butterscotch'][ingredient_property],
        num_cinnamon * test_input_dict['cinnamon'][ingredient_property]
    ])


def main():
    ingredient_combinations = itertools.combinations_with_replacement(test_input_dict.keys(), 100)
    scores = []
    for combination in ingredient_combinations:
        num_frosting = combination.count('frosting')
        num_candy = combination.count('candy')
        num_butterscotch = combination.count('butterscotch')
        num_sugar = combination.count('sugar')
        # num_cinnamon = combination.count('cinnamon')
        # capacity = calculate_test_property('capacity', num_butterscotch, num_cinnamon)
        # durability = calculate_test_property('durability', num_butterscotch, num_cinnamon)
        # flavor = calculate_test_property('flavor', num_butterscotch, num_cinnamon)
        # texture = calculate_test_property('texture', num_butterscotch, num_cinnamon)

        capacity = calculate_property('capacity', num_frosting, num_candy, num_butterscotch, num_sugar)
        durability = calculate_property('durability', num_frosting, num_candy, num_butterscotch, num_sugar)
        flavor = calculate_property('flavor', num_frosting, num_candy, num_butterscotch, num_sugar)
        texture = calculate_property('texture', num_frosting, num_candy, num_butterscotch, num_sugar)

        capacity = capacity if capacity > 0 else 0
        durability = durability if durability > 0 else 0
        flavor = flavor if flavor > 0 else 0
        texture = texture if texture > 0 else 0

        total = capacity * durability * flavor * texture
        # if calculate_test_property('calories', num_butterscotch, num_cinnamon) == 500:
        if calculate_property('calories', num_frosting, num_candy, num_butterscotch, num_sugar) == 500:
            scores.append(total)
        else:
            scores.append(0)

    print max(scores)


if __name__ == '__main__':
    main()
