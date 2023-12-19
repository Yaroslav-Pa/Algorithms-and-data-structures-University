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


def main():
    start = {"вовк1", "вовк2", "собака", "коза", "капуста"}
    boat = set()
    end = set()

    while True:
        display_state(start, boat, end)

        if not start:
            print("Вітаємо, ви перемогли!")
            break

        action = input("(лівий берег) Що ви хочете взяти у човен? (Введіть через кому, наприклад: вовк1, собака): ")

        items_to_move = [item.strip() for item in action.split(',')]
        if action and (len(items_to_move) > 2 or not all(item in start for item in items_to_move)):
            print("Невірний ввід. Виберіть не більше двох об'єктів, які є на лівому березі.")
            continue

        if action:
            for item in items_to_move:
                start.remove(item)
                boat.add(item)

        display_state(start, boat, end)

        if check_game_over(start, end):
            print("Ви програли! Небезпечна ситуація.")
            break

        exchange_action = input("(правий берег) З чим ви хочете обміняти те, що залишилось у човні? (Введіть через кому): ")
    
        items_to_exchange = [item.strip() for item in exchange_action.split(',')]
        if exchange_action and (len(items_to_exchange) > 2 or not all(item in end for item in items_to_exchange)):
            print("Невірний ввід. Виберіть не більше двох об'єктів, які є на правому березі.")
            continue

        if exchange_action:
            for item in boat:
                end.add(item)
            boat.clear()
            for item in items_to_exchange:
                end.remove(item)
                boat.add(item)
                
        display_state(start, boat, end)

        move_back = input("(правий берег) Що ви хочете залишити на правому березі? (Введіть через кому): ")

        items_to_move_back = [item.strip() for item in move_back.split(',')]
        if move_back and (len(items_to_move_back) > 2 or not all(item in boat for item in items_to_move_back)):
            print("Невірний ввід. Виберіть не більше двох об'єктів, які є в човні.")
            continue

        if move_back:
            for item in items_to_move_back:
                boat.remove(item)
                end.add(item)


        display_state(start, boat, end)

        exchange_action = input("(лівий берег) З чим ви хочете обміняти те, що залишилось у човні? (Введіть через кому): ")
    
        items_to_exchange = [item.strip() for item in exchange_action.split(',')]
        if exchange_action and (len(items_to_exchange) > 2 or not all(item in start for item in items_to_exchange)):
            print("Невірний ввід. Виберіть не більше двох об'єктів, які є на лівому березі.")
            continue

        if exchange_action:
            for item in boat:
                start.add(item)
            boat.clear()
            for item in items_to_exchange:
                start.remove(item)
                boat.add(item)



if __name__ == "__main__":
    main()
