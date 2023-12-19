from collections import deque

def display_state(start, boat, end):
    print("Start:", start)
    print("Boat:", boat)
    print("End:", end)
    print("-------------------------------")


def check_game_over(start, end):
    dangerous_combinations = [
        {"вовк1", "собака"},
        {"вовк2", "собака"},
        {"собака", "коза"},
        {"коза", "капуста"}
    ]
    for combination in dangerous_combinations:
        if combination.issubset(start) or combination.issubset(end):
            return True
    return False


def is_valid_move(state):
    start, boat, end = state
    return not check_game_over(start, end)


def generate_next_states(state):
    next_states = []
    start, boat, end = state

    for item1 in start:
        for item2 in start:
            if item1 != item2:
                new_boat = set(boat)
                new_boat.add(item1)
                new_boat.add(item2)
                new_start = start - new_boat
                new_state = (new_start, new_boat, end)
                if is_valid_move(new_state):
                    next_states.append(new_state)

    return next_states


def bfs():
    start = {"вовк1", "вовк2", "собака", "коза", "капуста"}
    boat = set()
    end = set()
    initial_state = (start, boat, end)

    queue = deque([initial_state])

    while queue:
        current_state = queue.popleft()
        display_state(*current_state)

        if not current_state[0] and not current_state[1]:
            print("Вітаємо, ви перемогли!")
            break

        next_states = generate_next_states(current_state)
        for next_state in next_states:
            queue.append(next_state)

        if check_game_over(*current_state[0:2]):  # Pass only start and end states
            print("Ви програли! Небезпечна ситуація.")
            queue.clear()


if __name__ == "__main__":
    bfs()
