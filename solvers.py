from item import Item

class Knapsack_Solver:
    '''
    Klasa ktora rozwiazuje nasz problem plecakowy
    za pomoca dwóch algorytmów: Brute Force oraz Programowania Dynamicznego.
    '''
    def __init__(self, capacity: int , items: list[Item]):
        self.capacity = capacity
        self.items = items
        self.n = len(items)

    # Brute Force
    def solve_brute_force(self) -> tuple[int, list[Item]]:
        '''
        Nasz algorytm bedzie opierał sie na masce 
        bitowej która będzie reprezentować które przedmioty bierzemy a które nie.
        Dla każdego możliwego ustawienia maski (od 0 do 2^n)
        '''
        
        
        max_value = 0
        best_mask = 0

        # Zewnętrzna pętla generuje każdą możliwą kombinację przedmiotów.
        # Wartość 1 << self.n jest rzędu 2^n (np. dla n=3 iterujemy od 0 do 7).
        for mask in range(1 << self.n):
            current_weight = 0
            current_value = 0

            # Wewnętrzna pętla iteruje po bitach wygenerowanej maski.
            for i in range(self.n):
                if mask & (1 << i): # Bit zapalony (1) oznacza wybranie i-tego przedmiotu
                    current_weight += self.items[i].weight
                    current_value += self.items[i].value
            
            # Weryfikacja warunków brzegowych: kombinacja musi się mieścić w plecaku
            # i zapewniać lepszy zysk niż dotychczasowe optimum globalne.
            if current_weight <= self.capacity and current_value > max_value:
                    max_value = current_value
                    best_mask = mask
        
        return max_value,self._decode_mask(best_mask)
    
    def _decode_mask(self, mask: int) -> list[Item]:
        '''
        Pomocnicza metoda (Pythonic Way). Wykorzystuje list comprehension 
        do translacji liczby całkowitej na fizyczną listę obiektów Item.
        '''
        return [self.items[i] for i in range(self.n) if (mask >> i) & 1]
    

    # Dynamic Programming
    def solve_dynamic_programming(self) -> tuple[int, list[Item]]:
        '''
        Rozwiązuje problem plecakowy metodą Programowania Dynamicznego (Tabulation).
        '''

        # Inicjalizacja macierzy dp wymiaru (n+1) x (C+1) samymi zerami.
        # Wiersze reprezentują dostępne przedmioty, kolumny - pojemności plecaka.
        dp = [[0] * (self.capacity + 1) for _ in range(self.n + 1)]

        # Wypełnianie macierzy (Bottom-Up)
        for i in range(1, self.n + 1):
            item = self.items[i - 1]
            for w in range(self.capacity + 1):
                if item.weight <= w:
                    # Równanie Bellmana (State Transition):
                    # Sprawdzamy co się bardziej opłaca - pominąć przedmiot czy go wziąć.
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item.weight] + item.value)
                else:
                    # Przedmiot jest fizycznie za ciężki dla danej wagi 'w', dziedziczymy poprzedni stan.
                    dp[i][w] = dp[i - 1][w]
                    
        # Odtwarzanie decyzji (Backtracking po macierzy)
        chosen_items = []
        w = self.capacity   

        # Iterujemy od końca macierzy w górę (reverse iteration)
        for i in range(self.n, 0, -1):
            # Jeżeli stan uległ zmianie względem wiersza wyżej, to oznacza,
            # że w tej komórce podjęliśmy decyzję o dodaniu przedmiotu.
            if dp[i][w] != dp[i - 1][w]:  
                chosen_items.append(self.items[i - 1])
                w -= self.items[i - 1].weight # Aktualizujemy resztę wolnego miejsca
        

        # Pythonic Way: [::-1] zwraca listę w oryginalnej kolejności w czasie O(n)
        return dp[self.n][self.capacity], chosen_items[::-1]

        
        
        