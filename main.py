import time
import sys
import os
from data_manager import DataManager
from solvers import Knapsack_Solver

def run_full_benchmarks():
    # Stała pojemność plecaka (C) dla eksperymentu t = f(n)
    fixed_C = 100 
    
    # Rozszerzona lista testów. Zauważ skok po n=20.
    test_sizes = [5, 10, 15, 20, 50, 100, 250, 500, 1000]
    
    # Próg odcięcia dla Brute Force (powyżej n=20 zajmuje to zbyt dużo czasu)
    BF_LIMIT = 20
    
    print(f"{'n':<5} | {'C':<5} | {'Max (BF)':<10} | {'Max (DP)':<10} | {'Czas BF (s)':<12} | {'Czas DP (s)':<12} | {'Zgodność'}")
    print("-" * 85)

    for n in test_sizes:
        filename = f"test_data_{n}.txt"
        
        # Ciche generowanie danych (Pythonic Way)
        sys.stdout = open(os.devnull, 'w')
        DataManager.generate_data(filename, fixed_C, n, max_weight=30, max_value=100)
        sys.stdout = sys.__stdout__
        
        capacity, items = DataManager.load_data(filename)
        solver = Knapsack_Solver(capacity, items)
        
        val_bf = "-"
        time_bf_str = "POMINIĘTO"
        
        # 1. Test algorytmu siłowego (Brute Force)
        if n <= BF_LIMIT:
            start_bf = time.perf_counter()
            val_bf, _ = solver.solve_brute_force()
            time_bf = time.perf_counter() - start_bf
            time_bf_str = f"{time_bf:.6f}"
            
        # 2. Test Programowania Dynamicznego (DP)
        start_dp = time.perf_counter()
        val_dp, _ = solver.solve_dynamic_programming()
        time_dp = time.perf_counter() - start_dp
        time_dp_str = f"{time_dp:.6f}"
        
        # 3. Weryfikacja logiczna (Cross-check)
        if n <= BF_LIMIT:
            is_match = "TAK" if val_bf == val_dp else "NIE!"
        else:
            is_match = "N/A"
            
        print(f"{n:<5} | {capacity:<5} | {str(val_bf):<10} | {str(val_dp):<10} | {time_bf_str:<12} | {time_dp_str:<12} | {is_match}")

if __name__ == "__main__":
    run_full_benchmarks()