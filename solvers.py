from item import Item

class Knapsack_Solver:
    def __init__(self, capacity: int , items: list[Item]):
        self.capacity = capacity
        self.items = items
        self.n = len(items)

    # Brute Force
    def solve_brute_force(self) -> tuple[int, list[Item]]:
        max_value = 0
        best_mask = 0

        # Wartość 1 << self.n jest rzędu 2^n (np. dla n=3 iterujemy od 0 do 7).
        for mask in range(1 << self.n):
            current_weight = 0
            current_value = 0

            # Wewnętrzna pętla iteruje po bitach wygenerowanej maski.
            for i in range(self.n):
                if mask & (1 << i):
                    current_weight += self.items[i].weight
                    current_value += self.items[i].value
            
            # Weryfikacja warunków brzegowych
            if current_weight <= self.capacity and current_value > max_value:
                    max_value = current_value
                    best_mask = mask
        
        return max_value,self._decode_mask(best_mask)
    
    def _decode_mask(self, mask: int) -> list[Item]:
        '''
        Pomocnicze. Wykorzystuje list comprehension 
        do translacji liczby całkowitej na fizyczną listę obiektów Item.
        '''
        return [self.items[i] for i in range(self.n) if (mask >> i) & 1]
    

    # Dynamic Programming
    def solve_dynamic_programming(self) -> tuple[int, list[Item]]:
        # macierz dp wymiaru (n+1) x (C+1) samymi zerami
        dp = [[0] * (self.capacity + 1) for _ in range(self.n + 1)]

        # Wypełnianie macierzy (Bottom-Up)
        for i in range(1, self.n + 1):
            item = self.items[i - 1]
            for w in range(self.capacity + 1):
                if item.weight <= w:
                    # Równanie Bellmana:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item.weight] + item.value)
                else:
                    dp[i][w] = dp[i - 1][w]
                    
        # Backtracking po macierzy
        chosen_items = []
        w = self.capacity   

        # Reverse iteration
        for i in range(self.n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:  
                chosen_items.append(self.items[i - 1])
                w -= self.items[i - 1].weight

        #[::-1] zwraca listę w oryginalnej kolejności w czasie O(n)
        return dp[self.n][self.capacity], chosen_items[::-1]

        
        
        