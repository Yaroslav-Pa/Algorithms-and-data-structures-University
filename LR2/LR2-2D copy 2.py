import random
from anytree import Node, RenderTree

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

class BTree:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.size = 1

    def insert(self, value):
        if self.value is None:
            self.value = value
        elif value.connected_tariffs <= self.value.connected_tariffs:
            if self.left is None:
                self.left = BTree(value, parent=self)
            else:
                self.left.insert(value)
            self.size += 1
        else:
            if self.right is None:
                self.right = BTree(value, parent=self)
            else:
                self.right.insert(value)

    def search(self, number):
        if self.value is None:
            return None
        if self.value.number == number:
            return self.value
        if self.value.number > number:
            if self.left:
                return self.left.search(number)
        else:
            if self.right:
                return self.right.search(number)
        return None


    def toAnytree(self):
        name = repr(self.value)
        if self.parent:
            if self.parent.left == self:
                name += " Left"
            else:
                name += " Right"
        node = Node(name)
        if self.left:
            left_node = self.left.toAnytree()
            left_node.parent = node
        if self.right:
            right_node = self.right.toAnytree()
            right_node.parent = node
        return node
    
    def getTariffPlanCounts(self):
        tariff_counts = {}
        self.getTariffPlanCountsHelper(tariff_counts)
        return tariff_counts

    def getTariffPlanCountsHelper(self, tariff_counts):
        if self.value is not None:
            tariff_counts[self.value.tariff_plan] = tariff_counts.get(self.value.tariff_plan, 0) + 1
            if self.left is not None:
                self.left.getTariffPlanCountsHelper(tariff_counts)
            if self.right is not None:
                self.right.getTariffPlanCountsHelper(tariff_counts)
    

    def delete(self, number):
        if self.value is None:
            return self

        if number < self.value.number:
            if self.left is not None:
                self.left = self.left.delete(number)
        elif number > self.value.number:
            if self.right is not None:
                self.right = self.right.delete(number)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                max_left, new_left = self.left.findMaxValue()
                if new_left is not None:
                    self.value = max_left
                    self.left = new_left
                else:
                    self.value = max_left
                    self.left = None

        return self

    def findMaxValue(self):
        if self.right is not None:
            max_value, new_right = self.right.findMaxValue()
            return max_value, BTree(self.value, self.left, new_right)
        return self.value, self.left


def main():
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

    root = None
    for subscriber in subscriber_data:
        if root is None:
            root = BTree(subscriber)
        else:
            root.insert(subscriber)

    root_node = root.toAnytree()
    for pre, _, node in RenderTree(root_node):
        print(f"{pre}{node.name}")

    found_subscriber = root.search(101)
    if found_subscriber:
        print(f"\nFound subscriber with number 101: {found_subscriber}")
    else:
        print("\nSubscriber not found.")
    
    tariff_plan_counts = root.getTariffPlanCounts()
    print("\nNumber of subscribers per tariff plan:")
    for plan, count in tariff_plan_counts.items():
        print(f"{plan}: {count} subscribers")

    print("\nDeleting")
    numberToDelete = 101
    root.delete(numberToDelete)

    print(f"\nUpdated tree ({numberToDelete}):")
    root_node = root.toAnytree()
    for pre, _, node in RenderTree(root_node):
        print(f"{pre}{node.name}")

if __name__ == "__main__":
    main()