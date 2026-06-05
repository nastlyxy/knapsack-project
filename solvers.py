from item import Item

class Knapsack_Solver:
    def __init__(self, capacity: int , items: list[Item]):
        self.capacity = capacity
        self.items = items
        self.n = len(items)


    def solve_brute_force(self) -> tuple[int, list[Item]]:
        '''
        Nasz algorytm bedzie opierał sie na masce 
        bitowej która będzie reprezentować które przedmioty bierzemy a które nie.
        Dla każdego możliwego ustawienia maski (od 0 do 2^n)
        '''
        
        
        max_value = 0
        best_mask = 0

        for mask in range(1 << self.n):
            current_weight = 0
            current_value = 0

            for i in range(self.n):
                if mask & (1 << i):
                    current_weight += self.items[i].weight
                    current_value += self.items[i].value
            
            if current_weight <= self.capacity and current_value > max_value:
                    max_value = current_value
                    best_mask = mask
        
        return max_value,self._decode_mask(best_mask)
    
    