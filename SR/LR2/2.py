import random
from anytree import Node, RenderTree
from variables2 import subscriber_data


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
            return None

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
                min_value = self.right.findMinValue()
                self.value = min_value
                self.right = self.right.delete(min_value.number)
        return self

    def findMinValue(self):
        if self.left is not None:
            return self.left.findMinValue()
        return self.value




def main():
    root = None
    for subscriber in subscriber_data:
        if root is None:
            root = BTree(subscriber)
        else:
            root.insert(subscriber)

    # Змініть символи тут
    custom_symbols = {"vertical": "|", "horizontal": "--", "up_down": "|-", "down": "L"}
    
    root_node = root.toAnytree()
    for pre, _, node in RenderTree(root_node):
        custom_pre = pre.replace("│", custom_symbols["vertical"]).replace("──", custom_symbols["horizontal"])
        custom_pre = custom_pre.replace("├", custom_symbols["up_down"]).replace("└", custom_symbols["down"])
        print(f"{custom_pre}{node.name}")

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
        custom_pre = pre.replace("│", custom_symbols["vertical"]).replace("──", custom_symbols["horizontal"])
        custom_pre = custom_pre.replace("├", custom_symbols["up_down"]).replace("└", custom_symbols["down"])
        print(f"{custom_pre}{node.name}")

if __name__ == "__main__":
    main()