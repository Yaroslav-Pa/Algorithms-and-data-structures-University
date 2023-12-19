import random
class Subscriber:
    def __init__(self, number, last_name, first_name, tariff_plan, connected_tariffs=None):
        self.number = number
        self.last_name = last_name
        self.first_name = first_name
        self.tariff_plan = tariff_plan
        if (connected_tariffs is None):
            self.connected_tariffs = random.randint(1, 255)
        else:
            self.connected_tariffs = connected_tariffs
        

    def __repr__(self):
        return f"{self.number}, {self.last_name}, {self.first_name}, {self.tariff_plan}, {self.connected_tariffs}"
    
subscriber_data = [
    Subscriber(101, "Smith", "John", "Plan1"),
    Subscriber(102, "Johnson", "Mary", "Plan2"),
    Subscriber(103, "Brown", "David", "Plan1"),
    Subscriber(104, "Jones", "Emily", "Plan3"),
    Subscriber(105, "Williams", "Michael", "Plan2", 81),
    Subscriber(106, "Davis", "Linda", "Plan2"),
    Subscriber(107, "Williams", "Linda", "Plan3"),
    Subscriber(108, "Davis", "Boris", "Plan3"),
    Subscriber(109, "Brown", "Goro", "Plan3"),
    Subscriber(110, "Smith", "Lusy", "Plan1"),
    Subscriber(111, "Brown", "Karl", "Plan1"),
    Subscriber(112, "Davis", "Boris", "Plan3"),
    Subscriber(113, "Jarvis", "Hodorod", "Plan2"),
]