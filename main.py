from data_manager import DataManager
from solvers import Knapsack_Solver


def main():
    filename = "knapsack_data.txt"

    capacity = 50
    num_items = 5
    

    #Generowanie danych
    DataManager.generate_data(filename, num_items, capacity,max_weight=30, max_value=100)

    #Wczytywanie danych
    C,items = DataManager.load_data(filename)

    #Przekazanie danych do solvera
    solver = Knapsack_Solver(C, items)

    #Brute Force
    print("Brute Force Solution:")
    val_bf, chosen_bf =solver.solve_brute_force()
    print(f"Max Value: {val_bf}")
    print(f"Wybrane przedmioty (ID): {[item.id for item in chosen_bf]}")


