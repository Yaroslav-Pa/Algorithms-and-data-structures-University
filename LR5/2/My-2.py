class State:
    def __init__(self, left_bank, boat, right_bank):
        self.left_bank = set(left_bank)
        self.boat = set(boat)
        self.right_bank = set(right_bank)

    def __eq__(self, other):
        return self.left_bank == other.left_bank and self.boat == other.boat and self.right_bank == other.right_bank

    def __hash__(self):
        return hash((frozenset(self.left_bank), frozenset(self.boat), frozenset(self.right_bank)))


def display_state(state):
    print("Left Bank:", state.left_bank)
    print("Boat:", state.boat)
    print("Right Bank:", state.right_bank)
    print("-------------------------------")


def check_game_over(state):
    dangerous_combinations = [
        {"вовк1", "собака"},
        {"вовк2", "собака"},
        {"собака", "коза"},
        {"коза", "капуста"}
    ]
    for combination in dangerous_combinations:
        if combination.issubset(state.left_bank) or combination.issubset(state.right_bank):
            return True
    return False


def get_possible_moves(state):
    possible_moves = []
    items_on_boat = list(state.boat)

    for i in range(len(items_on_boat) + 1):
        for combination in itertools.combinations(items_on_boat, i):
            if check_valid_move(state, combination):
                possible_moves.append(combination)

    return possible_moves


def check_valid_move(state, items_to_move):
    if len(items_to_move) > 2:
        return False

    if not all(item in state.boat for item in items_to_move):
        return False

    new_left_bank = state.left_bank - set(items_to_move)
    new_boat = set(items_to_move)
    new_right_bank = state.right_bank.union(set(items_to_move))

    new_state = State(new_left_bank, new_boat, new_right_bank)
    return not check_game_over(new_state)


def depth_first_search(current_state, visited):
    if not current_state or current_state in visited:
        return None

    display_state(current_state)
    visited.add(current_state)

    if not current_state.left_bank:
        print("Вітаємо, ви перемогли!")
        return current_state

    possible_moves = get_possible_moves(current_state)
    for move in possible_moves:
        new_left_bank = current_state.left_bank.union(set(move))
        new_boat = current_state.boat.difference(set(move))
        new_right_bank = current_state.right_bank.union(set(move))
        next_state = State(new_left_bank, new_boat, new_right_bank)

        if check_valid_move(next_state, move) and next_state not in visited:
            result = depth_first_search(next_state, visited)
            if result:
                return result

    return None


def main():
    start_state = State({"вовк1", "вовк2", "собака", "коза", "капуста"}, set(), set())
    visited_states = set()

    result = depth_first_search(start_state, visited_states)

    if not result:
        print("Ви програли! Неможливо знайти рішення без небезпеки.")
    else:
        print("Розв'язок знайдено!")


if __name__ == "__main__":
    main()
