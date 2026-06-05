from item import Item

class Knapsack_Solver:
    def __init__(self, capacity: int , items: list[Item]):
        self.capacity = capacity
        self.items = items
        self.n = len(items)
        

