import time
import sys
import os
from data_manager import DataManager
from solvers import Knapsack_Solver

def run_short_bf_test():
    # Złożoność BF to O(n * 2^n). Zatrzymujemy się na n=20, 
    # aby test trwał sekundy, a nie minuty.
    test_sizes = [5, 10, 15, 18, 20]
    fixed_C = 50
    
    print(f"{'n':<5} | {'C':<5} | {'Max Wartość':<12} | {'Czas BF (s)'}")
    print("-" * 50)

    for n in test_sizes:
        filename = f"test_bf_{n}.txt"
        
        # Wyciszenie logów z generatora (Pythonic Way z os.devnull)
        sys.stdout = open(os.devnull, 'w')
        DataManager.generate_data(filename, fixed_C, n, max_weight=20, max_value=50)
        sys.stdout = sys.__stdout__
        
        capacity, items = DataManager.load_data(filename)
        solver = Knapsack_Solver(capacity, items)
        
        start_time = time.perf_counter()
        max_val, chosen_items = solver.solve_brute_force()
        elapsed_time = time.perf_counter() - start_time
        
        print(f"{n:<5} | {capacity:<5} | {max_val:<12} | {elapsed_time:.6f}")

if __name__ == "__main__":
    run_short_bf_test()