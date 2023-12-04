def parse_data(input_data):
    games = {}
    for line in input_data:
        game_id_str, subsets_str = line.split(':')
        game_id = int(game_id_str.split()[1])
        subsets = []
        for subset_str in subsets_str.strip().split(';'):
            subset = {}
            for cube in subset_str.split(','):
                parts = cube.split()
                quantity, color = int(parts[0]), parts[1]
                subset[color] = quantity
            subsets.append(subset)
        games[game_id] = subsets
    return games

def is_possible(game, target_counts):
    for cube in game:
        for color in target_counts:
            if cube.get(color, 0) > target_counts[color]:
                return False
    return True

def possible_games(games, target_counts):
    possible_game_ids = []
    for game_id, subsets in games.items():
        if is_possible(subsets, target_counts):
            possible_game_ids.append(game_id)
    return possible_game_ids

def fewest_cubes_set(subsets):
    min_set = {"red": 0, "green": 0, "blue": 0}
    for subset in subsets:
        for color, count in subset.items():
            if count > min_set[color]:
                min_set[color] = count    
    return min_set

def calculate_power(cubes_set):
    return cubes_set["red"] * cubes_set["green"] * cubes_set["blue"]

def min_power_sum(games):
    min_power = 0
    for subsets in games.values():
        min_set = fewest_cubes_set(subsets)
        min_power += calculate_power(min_set)
    return min_power

def main():
    print("Sample:")
    input_data = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    target_counts = {"red": 12, "green": 13, "blue": 14}

    games = parse_data(input_data)
    possible_ids = possible_games(games, target_counts)
    min_power = min_power_sum(games)

    print("\tPossible game IDs:", possible_ids)
    print("\tSum of IDs (part one):", sum(possible_ids))
    print("\tMin Power Sum (part two):", min_power)
    
    print("Input file:")

    input_data = open('input-02.txt').readlines()

    games = parse_data(input_data)
    possible_ids = possible_games(games, target_counts)
    min_power = min_power_sum(games)

    print("\tPossible game IDs:", str(possible_ids).replace(' ', ''))
    print("\tSum of IDs (part one):", sum(possible_ids))
    print("\tMin Power Sum (part two):", min_power)

if __name__ == "__main__":
    main()
